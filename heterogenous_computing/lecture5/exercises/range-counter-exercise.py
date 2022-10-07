from multiprocessing import Process, Value, Array, Pool, current_process, Manager
import numpy as np 
import time 
from typing import List


# Num processes at a time

NUM_Processes = 10

# custom process class
class CustomProcess(Process):
    # override the constructor
    def __init__(self, row_index, row_val):
        # execute the base constructor
        Process.__init__(self)

        # Store the arguments to the process as shared variables TODO
        self.row_index = Value('i', row_index)
        self.row_val = Array('i', row_val)

        # Create a shared variable to hold our result when computed TODO
        self.count = Value('i', 0)

        # Non shared values
        self.min = 5
        self.max = 10
 

    # override the run function
    def run(self):
        process = current_process()
        print('process id of child', process.pid)

        temp = 0
        row = list(self.row_val)
        # Implement the range counter functionality 
        for element in row:
            if self.min <= element <= self.max:
                temp += 1

        # Store the result of the computation inside a shared variable TODO
        self.count.value = temp

if __name__ == '__main__':
    
    np.random.seed(0)
    
    arr = np.random.randint(0, 10, size=[500, 10])

    # Convert into lists of lists
    data = arr.tolist()

    # results dictionary to store results
    #manager = Manager()
    results_dict = {}
    
    for i in range(0,len(data),NUM_Processes):

        #with Pool(processes=10) as pool:

        # A sub-list for processes 
        process_lst_sub = []

        for j in range(NUM_Processes):
            p = CustomProcess(i+j, data[i+j])
            p.start()
            process_lst_sub.append(p)

        # iterate over the processes to retrieve their value and store it in the results_dict
        for process in process_lst_sub:
            process.join()
            results_dict[process.row_index.value] = process.count.value


        

    
    # Let us print out the first 10 values of the process_results dict 
    # Uncomment the following code to get the results from the processes

    for i in range(10):
        print(f"For row index:{i}, value is: {results_dict[i]} ")
        

    
