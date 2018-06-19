# -*- coding: utf-8 -*-

from libc.stdlib cimport malloc, free, qsrot

def l2_distance(point1, point2):
    cdef int dim = len(point1)
    cdef double *p1 = <double*> malloc (dim * sizeof(double))
    cdef double *p2 = <double*> malloc (dim * sizeof(double))
    cdef int i = 0
    while i<dim:
        p1[i] = point1[i]
        p2[i] = point2[i]
        i += 1
    return _l2_distance(p1, p2, dim)

cdef double _l2_distance(double* point1, double* point2, int dim):
    cdef int i = 0
    cdef double total = 0.0
    while i < dim:
        diff = point1[i] - point2[i]
        total += (diff * diff)
        i += 1
    return total
    
cdef int cmpfunc(const void * a, const void * b):
    cdef double first = (<double*>a)[0]
    cdef double second = (<double*>b)[0]
    if first > second:
        return 1
    elif first < second:
        return -1
    else:
        return 0
    
def closest_clusters(centers, datapoint):
    cdef int k = len(centers)
    cdef int dim = len(datapoint)
    distances = [l2_distance(center, datapoint) for
                 center in centers]
    cdef double* d = <double*> malloc (k * sizeof(double))
    cdef int i = 0
    while i < k:
        d[i] = distances[i]
        i += 1
    qsort(d, k, sizeof(double), &cmpfunc)
    return sorted(range(len(distances)), key=lambda x: distances[x]), distances
