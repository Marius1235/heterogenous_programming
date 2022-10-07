# pipemp.py
# Source: http://www.dabeaz.com/usenix2009/concurrent/index.html
#
# Code adapted and modified suitably by Raghava (rrm.digi@cbs.dk)


import multiprocessing
from multiprocessing import current_process

End_mark = 'End'


def consumer(con_conn):
    print('consumer with pid:', current_process().pid, ' created')
    # p1.close()  # Close producer's end (not used)
    con_buffer = []

    for block in iter(con_conn.recv, End_mark):
        con_buffer.append(block)
        # print(block)

    print('consumer with pid:', current_process().pid,
          ' received: \n', con_buffer)  # Do other useful work here


def producer(sequence, pro_conn):
    print('producer with pid:', current_process().pid, ' created')
    for item in sequence:
        pro_conn.send(item)

    pro_conn.send(End_mark)

    print('producer with pid:', current_process().pid,
          ' sent: \n', sequence)  # Do other useful work here


if __name__ == '__main__':

    print('main process with pid:', current_process().pid)

    p_conn, c_conn = multiprocessing.Pipe()

    cons = multiprocessing.Process(
        target=consumer,
        args=(c_conn,))
    cons.start()

    sequence = range(100)  # Replace with useful data
    prod = multiprocessing.Process(
        target=producer,
        args=(sequence, p_conn))

    prod.start()


    # close the connections!
    cons.join()
    prod.join()
    p_conn.close()
    c_conn.close()
