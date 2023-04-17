from multiprocessing import Process
import os


def foo():
    print('hello,os')


if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()
