# COP-Kmeans

<p align="left">
	<img src="http://behrouz-babaki.github.io/copkmeans/images/diagram.svg"
	     width="200">
</p>

This is an implementations of the *Constrained K-means Algorithm*,
developed by Wagstaff et al. according to the description of algorithm
presented in [[1][1]].



## The COP-Kmeans algorithm 
This is the *COP-Kmeans* algorithm, as described in [[1][1]]:

<img src="http://behrouz-babaki.github.io/copkmeans/images/algo.svg" 
     width="550">

## Usage

```
 usage: run_ckm.py [-h] [--ofile OFILE] dfile cfile k

 Run COP-Kmeans algorithm

 positional arguments:
   dfile          data file
   cfile          constraint file
   k              number of clusters

 optional arguments:
   -h, --help     show this help message and exit
   --ofile OFILE  file to store the output

```

To see a run of the algorithm on example data and constraints, run the script `examples/runner.sh`.

## There's more ...

### Other implementations

[Mateusz Zawiślak](https://github.com/mateuszzawislak) has a [java implementation](https://github.com/mateuszzawislak/k-means-clustering) of the COP-Kmeans algorithm. 

### Exact algorithms for constrained clustering

In 2013-14, I was working on developing an integer linear programming
formulation for an instance of the constrained clustering problem. The
approach that I chose was *Branch-and-Price* (also referred to as
column-generation). 

In the initialization step of my algorithm, I needed another algorithm
that can produce solutions of reasonably good quality very
quickly. The algorithm **COP-Kmeans** turned out to be exactly what I
was looking for.

Interested in knowing more about my own work? Go to my
[homepage][page], from where you can access my paper [[2][2]] and the
corresponding code.

## References
1. Wagstaff, K., Cardie, C., Rogers, S., & Schrödl, S. (2001,
June). Constrained k-means clustering with background knowledge. In
ICML (Vol. 1, pp. 577-584).

2. Babaki, B., Guns, T., & Nijssen, S. (2014). Constrained clustering
using column generation. In Integration of AI and OR Techniques in
Constraint Programming (pp. 438-454). Springer International
Publishing.

[1]: https://web.cse.msu.edu/~cse802/notes/ConstrainedKmeans.pdf
[2]: https://lirias.kuleuven.be/bitstream/123456789/437301/3/Constrained_Clustering_using_Column_Generation.pdf
[page]: http://people.cs.kuleuven.be/~behrouz.babaki/#publications
