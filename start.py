# coding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from multiprocessing import Pool, Manager

from main.down import *

if __name__ == '__main__':
    pool = Pool(16)
    items = range(1, 2)
    pool.map(downLoad, items)
    pool.close()
    pool.join()
