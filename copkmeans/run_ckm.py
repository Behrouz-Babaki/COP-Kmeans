#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from cop_kmeans import cop_kmeans
import argparse


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
        result = result[0]
        with open(outfile, 'w') as f:
            for cluster in result:
                f.write('%d\n' %cluster)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run COP-Kmeans algorithm')
    parser.add_argument('dfile', help='data file')
    parser.add_argument('cfile', help='constraint file')
    parser.add_argument('k', type=int, help='number of clusters')
    parser.add_argument('--ofile', help='file to store the output', default=None)
    args = parser.parse_args()

    clusters = run(args.dfile, args.cfile, args.k, args.ofile)
    if not clusters:
        print('No solution was found!')
    else:
        print(' '.join(str(c) for c in clusters))
