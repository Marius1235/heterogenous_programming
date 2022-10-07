from multiprocessing import Process, Value, Array, Pool, current_process
import numpy as np
from multiprocessing import Manager
import time 
from typing import List


# Num processes at a time

NUM_Processes = 10

manager = Manager()
shared_dict = manager.dict()


# custom process class
class CustomProcess(Process):
    # override the constructor
    def __init__(self, row_index, row_val):
        # execute the base constructor
        Process.__init__(self)

        # Store the arguments to the process as shared variables
        self.row_index = Value('i',row_index)
        self.row_val = Array('i', row_val)

        # Create a shared variable to hold our result when computed
        self.result = Value('i', 0)
        
        # Non shared values
        self.min = 5
        self.max = 10

 

    # override the run function
    def run(self):
        process = current_process()
        print('process id of child', process.pid)
        sum_vals = 0
        # val = self.row_index.value
        row = list(self.row_val)
        for val in row:
            if self.min <= val <= self.max:
                sum_vals += 1

        self.result.value = sum_vals
        # self.dict[self.row_index] = sum_vals


if __name__ == '__main__':
    
    np.random.seed(0)
    
    arr = np.random.randint(0, 10, size=[500, 10])

    # Convert into lists of lists
    data = arr.tolist()

    # results dictionary 
    results_dict = {}
    
    for i in range(0,len(data),NUM_Processes):

        # A sub-list for processes 
        process_lst_sub = []

        for j in range(NUM_Processes):
            
            process = CustomProcess(i+j,data[i+j])
            process.start()
            process.run()
            process_lst_sub.append(process)

        # wait for them to join
        # iterate over the processes to retrieve their value and store it in the results_dict

        for process in process_lst_sub:
            process.join()
            results_dict[process.row_index.value] = process.result.value

    
    # Let us print out the first 10 values of the process_results dict 
    for i in range(10):
        print(f"For row index:{i}, value is: {results_dict[i]} ")


    # print(shared_dict)

    
