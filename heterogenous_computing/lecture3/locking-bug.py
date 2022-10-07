'''
Standard example to display race condition & locking solution
'''

from threading import Thread, Lock
import time




# We will be using a global variable as a shared resource among the threads
shared_value = 0

def increase(amount: int, lock: Lock) -> None:
    # allows us to use the global value instead of local (function-limited) variable 
    global shared_value

    lock.acquire()

    # Copy over the shared_value to a local value
    local_val = shared_value
    # Increase local_val by the amount specified
    local_val+= amount

    # Let's make the thread sleep for half a second
    time.sleep(0.5)

    # Update shared_value 
    shared_value = local_val

    print("Value of shared_value is: ", shared_value)
    lock.release()


def decrease(amount: int, lock: Lock) -> None:
    # allows us to use the global value instead of local (function-limited) variable 
    global shared_value

    lock.acquire()

    # Copy over the shared_value to a local value
    local_val = shared_value
    # Increase local_val by the amount specified
    local_val -= amount

    # Let's make the thread sleep for half a second
    time.sleep(0.5)

    # Update shared_value 
    shared_value = local_val

    print("Value of shared_value is: ", shared_value)
    lock.release()




lock1 = Lock()
lock2 = Lock()


t1 = Thread(target= increase, args= (20,lock1))
t2 = Thread(target= decrease, args= (10,lock2))

# Start Threads
t1.start()
t2.start()

# Join the threads so we wait for them to complete
t1.join()
t2.join()

print("Final value of shared_value is: ", shared_value)

# We expect the solution to be 10 but we either get -10 or 20.
