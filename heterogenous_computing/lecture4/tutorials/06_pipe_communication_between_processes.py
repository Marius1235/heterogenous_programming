# source: Python multiprocessing - pipe communication between processes
# https://stackoverflow.com/questions/55110733/python-multiprocessing-pipe-communication-between-processes
#

from multiprocessing import Process, Pipe
from datetime import datetime

SENTINEL = 'SENTINEL'


def update_data(child_conn):

    result = []

    for msg in iter(child_conn.recv, SENTINEL):
        print(f'{datetime.now()} child received {msg}')
        result.append(msg)

    print(f'{datetime.now()} child received sentinel')
    result.append(['new data'])
    writer(child_conn, result)
    child_conn.close()


def writer(conn, data):
    conn.send(data)
    conn.send(SENTINEL)


if __name__=='__main__':

    parent_conn, child_conn = Pipe()  # default is duplex!
    update_data_process = Process(target=update_data, args=(child_conn,))
    update_data_process.start()

    data = ['0' for i in range(3)]
    writer(parent_conn, data)

    for msg in iter(parent_conn.recv, SENTINEL):
        print(f'{datetime.now()} parent received {msg}')

    print(f'{datetime.now()} parent received sentinel')
    parent_conn.close()
    update_data_process.join()