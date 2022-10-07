# pipemp.py
# Source: http://www.dabeaz.com/usenix2009/concurrent/index.html
# Code adapted and modified suitably by Raghava (rrm.digi@cbs.dk)


import multiprocessing
from multiprocessing import current_process


def consumer(p1, p2):
    print('consumer with pid:', current_process().pid, ' created')
    p1.close()  # Close producer's end (not used)
    con_buffer = []
    while True:
        try:
            item = p2.recv()
            con_buffer.append(item)
        except EOFError:
            break

    print('consumer with pid:', current_process().pid,
          ' received: \n', con_buffer)  # Do other useful work here


def producer(sequence, output_p):
    print('producer with pid:', current_process().pid, ' created')
    for item in sequence:
        output_p.send(item)
    print('producer with pid:', current_process().pid,
          ' sent: \n', sequence)  # Do other useful work here






if __name__ == '__main__':
    p1, p2 = multiprocessing.Pipe()

    cons = multiprocessing.Process(
        target=consumer,
        args=(p1, p2))
    cons.start()

    # Close the input end in the producer
    p2.close()

    # Go produce some data
    sequence = range(100)  # Replace with useful data
    producer(sequence, p1)

    # Close the pipe
    p1.close()
