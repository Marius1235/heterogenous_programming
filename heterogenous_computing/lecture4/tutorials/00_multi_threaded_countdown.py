# perf.py
#
# A performance problem with threads
# Source: http://www.dabeaz.com/usenix2009/concurrent/index.html
#
# Code adapted and modified suitably by Raghava (rrm.digi@cbs.dk)


import time
import threading

count_vals = 10000000

def count(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    start = time.time()
    count(count_vals)
    count(count_vals)
    count(count_vals)
    end = time.time()
    print ("Sequential", end-start)

    start = time.time()
    t1 = threading.Thread(target=count,args=(count_vals,))
    t2 = threading.Thread(target=count,args=(count_vals,))
    t3 = threading.Thread(target=count,args=(count_vals,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    end = time.time()
    print ("Multi Threaded version", end-start)

