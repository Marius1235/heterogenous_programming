'''
A simple non-trivial parallel program
Ref : https://www.machinelearningplus.com/python/parallel-processing-python/
'''
import multiprocessing as mp
import time
from typing import List
import numpy as np
import matplotlib.pyplot as plt


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


def apply_range_counter_sequential(data: List[List[int]],
                                   min: int,
                                   max: int) -> List[int]:
    '''
    This function takes data and applies the range_counter function
    over all the rows in the data
    '''
    result = []
    for row in data:
        temp_result = range_counter(row, min, max)
        result.append(temp_result)
    return result



if __name__ == '__main__':

    # Providing a seed ensures we can get the same 'random' values
    #  generated each time (Good for testing)
    np.random.seed(0)

    # create a matrix with dimensions 200x5 (200 rows and 5 columns)
    arr = np.random.randint(0, 10, size=[50000, 10])

    ranges = [50_000, 500_000, 900_000, 3_000_000, 30_000_000]

    durations = []

    for range in ranges:
        arr = np.random.randint(0, 10, size=[range, 10])
        data = arr.tolist()
        times = []
    # Convert into lists of lists

    # timing the sequential solution
        start_sequential = time.perf_counter()

        seq_result = apply_range_counter_sequential(data, 5, 10)

        end_sequential = time.perf_counter()

        times.append(round(end_sequential - start_sequential, 5))

        print(f'Finished Sequential computation in range: {range}, in {round(end_sequential-start_sequential, 5)} seconds')

        print('First 10 results of the sequential result', seq_result[:10])

        # Performing the computation in parallel
        result_parallel = []

        start = time.perf_counter()

        with mp.Pool(4) as p:
            # temp_result = [p.apply(range_counter, args=(row, 4, 8)) for row in data]
            # print(temp_result[:10])
            result_parallel = p.map(range_counter, data)

        finish = time.perf_counter()
        times.append(round(finish - start, 5))
        durations.append(times)
        print(f'finished Parallel execution in range: {range}, in {round(finish-start, 2)} seconds')
        print('First 10 results of the parallel result', result_parallel[:10])

    plt.plot(durations[0], durations[1])
    plt.savefig("durations.png", dpi=500)
    plt.show()




