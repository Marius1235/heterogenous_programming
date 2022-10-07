# SuperFastPython.com
# example of a mutual exclusion (mutex) lock for processes
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Lock
from multiprocessing import current_process


# work function
def task(lock, identifier, value):
    print('producer with pid:', current_process().pid, ' created')
    # acquire the lock
    with lock:
        print(
            f'>process with id:{current_process().pid} and identifier: {identifier} got the lock, sleeping for {value}')
        sleep(value)
    print(f">process with id:{current_process().pid} exiting!")

# entry point
if __name__ == '__main__':
    # create the shared lock
    lock = Lock()
    # create a number of processes with different sleep times
    processes = [Process(target=task, args=(lock, i, random())) for i in range(10)]
    # start the processes
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()
