#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from cop_kmeans import cop_kmeans, l2_distance
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

def run(datafile, consfile, k, n_rep, max_iter, tolerance):
    data = read_data(datafile)
    ml, cl = read_constraints(consfile)

    best_clusters = None
    best_score = None
    for _ in range(n_rep):
        clusters, centers = cop_kmeans(data, k, ml, cl,
                                       max_iter=max_iter,
                                       tol=tolerance)
        if clusters is not None and centers is not None:
            score = sum(l2_distance(data[j], centers[clusters[j]])
                        for j in range(len(data)))
            if best_score is None or score < best_score:
                best_score = score
                best_clusters = clusters

    return best_clusters

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run COP-Kmeans algorithm')
    parser.add_argument('dfile', help='data file')
    parser.add_argument('cfile', help='constraint file')
    parser.add_argument('k', type=int, help='number of clusters')
    parser.add_argument('--ofile', help='file to store the output', default=None)
    parser.add_argument('--n_rep', help='number of times to repeat the algorithm',
                        default=10, type=int)
    parser.add_argument('--m_iter', help='maximum number of iterations of the main loop',
                        default=300, type=int)
    parser.add_argument('--tol', help='tolerance for deciding on convergence',
                        default=1e-4, type=float)
    args = parser.parse_args()

    clusters = run(args.dfile, args.cfile, args.k,
                            args.n_rep, args.m_iter, args.tol)

    if args.ofile is not None and clusters is not None:
        with open(args.ofile, 'w') as f:
            for cluster in clusters:
                f.write('%d\n' %cluster)

    if not clusters:
        print('No solution was found!')
    else:
        print(' '.join(str(c) for c in clusters))
