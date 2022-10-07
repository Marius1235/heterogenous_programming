import multiprocessing
import time
import hashlib
from multiprocessing import Array
from multiprocessing import Manager


# control the number of consumers
NUM_consumers = 3

# shared_hashmap = Array('u',10)
manager = Manager()
dict = manager.dict()

def producer(cond, queue, docs):

    process = multiprocessing.current_process()
    print('Startin producer: ', process.pid)
    print("Number of documents sent to producer: ", len(docs))

    # The producer places the documents in the queue to be hashed
    for doc in docs:
        queue.put(doc)

    # We use the sentinel method to end the consumers 
    # We place None into the queue.
    # If we have more than 1 consumer, we places a multiple number of Nones into the queue
    for i in range(NUM_consumers):
        queue.put(None)

    with cond:
        print('Producer is done and ready for consumers')
        cond.notify_all()


def consumer(cond, queue):
    process = multiprocessing.current_process()
    print('Starting consumer: ', process.pid)
    with cond:
        cond.wait()
    
    print(f'Consumer {process.pid} is starts working now!')
    while True:
        # get a document
        item = queue.get()
        # print(f"{process.pid} Got item: ", item)

        # check for stop
        if item is None:
            break
        hx_digest = hashlib.sha256(item.encode('utf-8')).hexdigest()
        # shared_hashmap[0] =hx_digest

        # dict[0] = dict[0] + [hx_digest]
        dict[hx_digest] = item

        print(f"The consumer finished hashing")


if __name__ == '__main__':

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
                                 args=(condition,queue, documents))
    consumer_processes = [
        multiprocessing.Process(
            name=f'consumer[{i}]',
            target=consumer,
            args=(condition,queue),
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

    # print(dict)

    for key,value in dict.items():
        print(value, ':', key)