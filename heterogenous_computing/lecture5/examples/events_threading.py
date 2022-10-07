
# event_barrier.py
#
# An example of using an event to set up a barrier
# synchronization
# source: http://www.dabeaz.com/usenix2009/concurrent/index.html
# Code adapted by Raghava

import threading
import time

init_event = threading.Event()

def worker():
    print (threading.currentThread().name,
           " : I'm worker waiting for the event!" )
    init_event.wait()        # Wait until initialized
    print (threading.currentThread().name,
           " : I'm worker and I am done with the event!" )


def initialize():
    print ("Initializing some data")
    time.sleep(10)
    print ("Unblocking the workers")
    init_event.set()


# entry point
if __name__ == '__main__':

    # Launch a bunch of worker threads
    threading.Thread(target=worker).start()
    threading.Thread(target=worker).start()
    threading.Thread(target=worker).start()
    threading.Thread(target=worker).start()

    # Go initialize and eventually unlock the workers
    initialize()

