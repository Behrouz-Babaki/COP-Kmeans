#!/usr/bin/env python
# coding: utf-8

import sys
import csv
sys.path.append('../python')
from cop_kmeans import cop_kmeans, l2_distance

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

def cluster_quality(cluster):
    if len(cluster) == 0:
        return 0.0
       
    quality = 0.0
    for i in range(len(cluster)):
        for j in range(i, len(cluster)):
            quality += l2_distance(cluster[i], cluster[j])
    return quality / len(cluster)
    
def compute_quality(data, cluster_indices):
    clusters = dict()
    for i, c in enumerate(cluster_indices):
        if c in clusters:
            clusters[c].append(data[i])
        else:
            clusters[c] = [data[i]]
    return sum(cluster_quality(c) for c in clusters.values())
    

def run_iterate(datafile, consfile, k, n_runs=500):
    data = read_data(datafile)
    ml, cl = read_constraints(consfile)
    
    num_sat = 0
    best_quality = None
    for i in range(n_runs):
        result = cop_kmeans(data, k, ml, cl)
        if result != None:
            num_sat += 1
            clusters, centers = result
            quality = compute_quality(data, clusters)
            if not best_quality or quality < best_quality:
                best_quality = quality
    return (num_sat/n_runs*100), best_quality

def run_ckm(ds_name, cons_nums):
    results = []
    for c_num in cons_nums:
        sat, qual = run_iterate('../data/%s/%s.data'%(ds_name, ds_name), 
                                '../data/%s/constraints/%s.%d.cons'%(ds_name, ds_name, c_num), 
                                k=5, n_runs=500)
        results.append({'c': c_num, 'sat': sat, 'quality': qual})
    
    
    with open('./%s.resluts'%(ds_name), 'w') as f:
        w = csv.DictWriter(f, results[0].keys())
        w.writeheader()
        w.writerows(results)    


if __name__ == '__main__':
    iris_ncons = [2, 60, 100, 140, 200, 240, 300, 340, 400, 440, 500]
    run_ckm('iris', iris_ncons)
    
    wine_ncons = [240, 300, 340, 380, 420, 460, 500]
    run_ckm('wine', wine_ncons)




