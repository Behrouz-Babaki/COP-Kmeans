# cop-kmeans
An implementation of cop-kmeans algorithm

This is an implementations of the *Constrained K-means Algorithm*,
developed by Wagstaff et al. according to the description of algorithm
presented in [[1][1]].

## Why did I implement it?

In 2013-14, I was working on developing an integer linear programming
formulation for an instance of the constrained clustering problem. The
approach that I chose was *Branch-and-Price* (also referred to as
column-generation). 

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">Column generation should not allowed to be that good</p>&mdash; P. Van Hentenryck (@PVanHentenryck) <a href="https://twitter.com/PVanHentenryck/status/536418044927410176">November 23, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

In the initialization step of my algorithm, I needed another algorithm
that can produce solutions of reasonably good solutions very
quickly. The algorithm **cop-kmeans** turned out to be exactly what I
was looking for.

Interested in knowing more about my work? Check the paper and try the
code [[2][2]]. 

# references

1. Wagstaff, K., Cardie, C., Rogers, S., & Schrödl, S. (2001,
June). Constrained k-means clustering with background knowledge. In
ICML (Vol. 1, pp. 577-584).

2. Babaki, B., Guns, T., & Nijssen, S. (2014). Constrained clustering
using column generation. In Integration of AI and OR Techniques in
Constraint Programming (pp. 438-454). Springer International
Publishing.

[1]: https://web.cse.msu.edu/~cse802/notes/ConstrainedKmeans.pdf
[2]: http://people.cs.kuleuven.be/~behrouz.babaki/#publications
