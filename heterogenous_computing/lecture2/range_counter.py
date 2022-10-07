'''
A simple non-trivial parallel program
Ref : https://www.machinelearningplus.com/python/parallel-processing-python/
'''

import time
from typing import List
import numpy as np 


def range_counter(row: List[int], min: int = 5, max: int = 10) -> int:
    '''
    Returns the number of values in the row that fall between the given range
        Args:
            i.   row : Lst of numbers
            ii.  min : minimum value of range
            iii. max : maximum values of range

        Returns: a count (int) of values that fall in the range
    '''
    count = 0
    for val in row:
        if min <= val <= max:
            count += 1
    return count


def apply_range_counter_sequential(data: List[List[int]]) -> List[int]:
    '''
    This function takes data and applies the range_counter function
    over all the rows in the data
    '''
    result = []
    for row in data:
        temp_result = range_counter(row)
        result.append(temp_result)
    return result


if __name__ == '__main__':

    # Providing a seed ensures we can get the same 'random' values
    #  generated each time (Good for testing)
    np.random.seed(0)

    # create a matrix with dimensions 200x5 (200 rows and 5 columns)
    arr = np.random.randint(0, 10, size=[200000, 10])

    # Convert into lists of lists
    data = arr.tolist()

    # timing the sequential solution
    start_sequential = time.perf_counter()

    seq_result = apply_range_counter_sequential(data)
    
    end_sequential = time.perf_counter()

    print(f'Finished Sequential computation in {round(end_sequential-start_sequential, 5)} seconds')

    print('First 10 results of the sequential result', seq_result[:10])

    