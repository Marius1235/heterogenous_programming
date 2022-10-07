# sema_signal.py
#
# An example of using a semaphore to signal

import threading
import time

done = threading.Semaphore(0)
item = None


def producer():
    global item
    print(threading.currentThread().name,
          "I'm the producer and I produce data.")
    print("Producer is going to sleep.")
    time.sleep(10)
    item = "Hello"
    print("Producer is alive. Signaling the consumer.")
    done.release()


def consumer():
    print(threading.currentThread().name, ": I'm a consumer and I wait for data.")
    print(threading.currentThread().name, ": Consumer is waiting.")
    done.acquire()
    print(threading.currentThread().name, ": Consumer got", item)
    done.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=producer)

    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t3 = threading.Thread(target=consumer)
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print('done with execution and exiting main thread!')
