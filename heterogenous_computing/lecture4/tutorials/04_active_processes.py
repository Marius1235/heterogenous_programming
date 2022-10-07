# SuperFastPython.com
# list all active child processes
# source: Python Multiprocessing: The Complete Guide https://superfastpython.com/multiprocessing-in-python/
# # Code adapted and modified suitably by Raghava (rrm.digi@cbs.dk)


import multiprocessing
from multiprocessing import active_children
from time import sleep


def task(i):
    sleep(i)


if __name__ == '__main__':
    context = multiprocessing.get_context('fork')

    pool = context.Pool(5)

    pool.apply(task, (1,))

    # get a list of all active child processes
    children = active_children()
    # report a count of active children
    print(f'Active Children Count: {len(children)}')
    # report each in turn
    for child in children:
        print(child)
