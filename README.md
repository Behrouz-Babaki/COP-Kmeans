# cop-kmeans
An implementation of cop-kmeans algorithm

This is an implementations of the *Constrained K-means Algorithm*,
developed by Wagstaff et al. according to the description of algorithm
presented in [[1][1]].

![](./images/logo.svg)

## Why did I implement it?

In 2013-14, I was working on developing an integer linear programming
formulation for an instance of the constrained clustering problem. The
approach that I chose was *Branch-and-Price* (also referred to as
column-generation). 

In the initialization step of my algorithm, I needed another algorithm
that can produce solutions of reasonably good quality very
quickly. The algorithm **cop-kmeans** turned out to be exactly what I
was looking for.

Interested in knowing more about my own work? Go to my
[homepage][page], from where you can access my paper [[2][2]] and the
corresponding code.

# references

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
