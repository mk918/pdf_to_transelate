#! /usr/bin/python
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    f = open('before.txt', 'r')
    fw = open('after.txt', 'w')
    for row in f:
        row = row.replace('-\n','')
        row = row.replace('\n',' ')
        fw.write(row)
    f.close()
    fw.close()