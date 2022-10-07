# SuperFastPython.com
# example of extending the Process class and adding shared attributes
# source: https://superfastpython.com/multiprocessing-in-python/
# Code adapted and modified suitably by Raghava (rrm.digi@cbs.dk)

from time import sleep
from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import current_process

# custom process class
class CustomProcess(Process):
    # override the constructor
    def __init__(self):
        # execute the base constructor
        Process.__init__(self)
        # initialize integer attribute
        self.data = Value('i', 10)

    # override the run function
    def run(self):
        print(f'Child reported value: {self.data.value}')
        # block for a moment
        sleep(1)
        # store the data variable
        self.data.value = 99
        # report stored value
        print(f'Child stored: {self.data.value}')
        process = current_process()
        print ('current process in child process:', process)
        print('process id of child', process.pid)


# entry point
if __name__ == '__main__':
    # create the process
    process = CustomProcess()
    # start the process
    process.start()
    # wait for the process to finish
    print('Waiting for the child process to finish')
    # block until child process is terminated
    process.join()
    # report the process attribute
    print(f'Parent got: {process.data.value}')

    # process.data.value = 125
    # # report the process attribute
    # print(f'Parent got: {process.data.value}')

    cur_process = current_process()
    print('current process in main process:', cur_process)
    print('process id of parent', cur_process.pid)
