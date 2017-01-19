# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from cop_kmeans import cop_kmeans

def read_data(datafile):
    data = []
    with open(datafile, 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                d = [float(i) for i in line.split()]
                data.append(d)
    return data

def read_constraints(consfile):
    ml, cl = [], []
    with open(consfile, 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                line = line.split()
                constraint = (int(line[0]), int(line[1]))
                c = int(line[2])
                if c == 1:
                    ml.append(constraint)
                if c == -1:
                    cl.append(constraint)
    return ml, cl

def run(datafile, consfile, k, outfile):
    data = read_data(datafile)
    ml, cl = read_constraints(consfile)
    result = cop_kmeans(data, k, ml, cl)
    if result != None:
        with open(outfile, 'w') as f:
            for cluster in result[0]:
                f.write('%d\n' %cluster)
    return result

def run_iterate(datafile, consfile, k, outfile, limit=1000):
    for _ in range(limit):
        result = run(datafile, consfile, int(k), outfile)
        if result != None:
            print ('done!')
            break

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('usage: %s [data file][constraint file][#clusters][output file]' %sys.argv[0])
        exit(1)
    run_iterate(*sys.argv[1:])
