"""
# 02_perfmp.py
# A performance test with processes
Source: http://www.dabeaz.com/usenix2009/concurrent/index.html

Code adapted and modified suitably by Raghava (rrm.digi@cbs.dk)
"""

import time
import multiprocessing
from multiprocessing import current_process


def count(n):
    while n > 0:
        n -= 1
        # if n % 1000000 == 0:
        #     print(current_process().pid, ': ', n)


if __name__ == '__main__':
    start = time.time()
    count(10000000)
    count(10000000)
    end = time.time()
    print("Time taken in sequential", end - start)

    start = time.time()

    # p1 = multiprocessing.Process(target=count,args=(10000000,))
    # p2 = multiprocessing.Process(target=count,args=(10000000,))
    # method = multiprocessing.get_start_method()
    # print('current start method', method)

    context = multiprocessing.get_context('spawn')
    p1 = context.Process(target=count, args=(10000000,))
    p2 = context.Process(target=count, args=(10000000,))


    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("Time taken in multiprocessing", end - start)
