"""
01_countdownp.py

Example of launching a process with the multiprocessing module
Source: http://www.dabeaz.com/usenix2009/concurrent/index.html

Code adapted and modified suitably by Raghava (rrm.digi@cbs.dk)
"""

import time
from multiprocessing import current_process
import multiprocessing


class CountdownProcess(multiprocessing.Process):
    def __init__(self, count):
        multiprocessing.Process.__init__(self)
        self.count = count

    def run(self):
        pid = current_process().pid
        print('child process with process id:', pid)
        while self.count > 0:
            print('child process:', pid, ",counting down ", self.count)
            self.count -= 1
            time.sleep(1)
        return


if __name__ == '__main__':
    p1 = CountdownProcess(5)  # Create the process object
    p1.start()  # Launch the process

    p2 = CountdownProcess(10)  # Create another process
    p2.start()  # Launch

    print('main process with process id:', current_process().pid)
