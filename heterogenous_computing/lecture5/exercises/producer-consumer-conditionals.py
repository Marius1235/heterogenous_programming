import multiprocessing
import time
import hashlib
from multiprocessing import Manager

# control the number of consumers
NUM_consumers = 3




def producer(cond, queue, docs):
    process = multiprocessing.current_process()
    print('Starting producer: ', process.pid)
    print("Number of documents sent to producer: ", len(docs))

    # Use queue for documents TODO
    for doc in docs:
        queue.put(doc)

    for i in range(NUM_consumers):
        queue.put(None)
    # producer is finished with their task and tells the consumers TODO
    with cond:
        cond.notify_all()


def consumer(cond, queue, sharedD):
    process = multiprocessing.current_process()
    print('Starting consumer: ', process.pid)

    temp = {}

    # wait until producer is completed with their work
    with cond:
        cond.wait()

    print(f'Consumer {process.pid} is running')

    while True:
        # get a document and produce its hex_digest TODO
        item = queue.get()

        if item is None:
            print(f"Consumer {process.pid} is breaking the loop")
            break

        hx_digest = hashlib.sha256(item.encode('utf-8')).hexdigest()

        sharedD[hx_digest] = item

        print(f"The consumer finished hashing")

    print(len(temp))


if __name__ == '__main__':
    manager = Manager()
    dict = manager.dict()

    # A list of documents to send the producer
    documents = [
        "This is a confidential document 1",
        "This is a confidential document 2",
        "This is a confidential document 3",
        "This is a confidential document 4",
        "This is a confidential document 5",
        "This is a confidential document 6",
        "This is a confidential document 7",
        "This is a confidential document 8",
        "This is a confidential document 9",
        "This is a confidential document 10"]

    condition = multiprocessing.Condition()
    queue = multiprocessing.Queue()

    producer_process = multiprocessing.Process(
        target=producer,
        args=(condition, queue, documents))

    # Create 'NUM_consumers' number of consumer processes and store in list TODO
    consumer_processes = [
        multiprocessing.Process(
            name=f'consumer{i}',
            target=consumer,
            args=(condition, queue, dict),
        )
        for i in range(NUM_consumers)
    ]

    for c in consumer_processes:
        c.start()

        time.sleep(1)
    producer_process.start()

    producer_process.join()
    for c in consumer_processes:
        c.join()

    for key, value in dict.items():
        print(key, ":", value, "\n")
