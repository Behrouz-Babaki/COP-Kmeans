# COP-Kmeans
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.831850.svg)](https://doi.org/10.5281/zenodo.831850)


<p align="left">
	<img src="https://cdn.rawgit.com/Behrouz-Babaki/COP-Kmeans/gh-pages/images/diagram.svg"
	     width="200">
</p>

This is an implementations of the *Constrained K-means* algorithm,
introduced by Wagstaff et al. This implementation is developed according 
to the description of algorithm as presented in [[1][1]].



## The COP-Kmeans algorithm 
This is the *COP-Kmeans* algorithm, as described in [[1][1]]:

<img src="https://cdn.rawgit.com/Behrouz-Babaki/COP-Kmeans/gh-pages/images/algo.svg" 
     width="550">

## Usage

```
usage: run_ckm.py [-h] [--ofile OFILE] [--n_rep N_REP] [--m_iter M_ITER] [--tol TOL] dfile cfile k

Run COP-Kmeans algorithm

positional arguments:
  dfile            data file
  cfile            constraint file
  k                number of clusters

optional arguments:
  -h, --help       show this help message and exit
  --ofile OFILE    file to store the output
  --n_rep N_REP    number of times to repeat the algorithm
  --m_iter M_ITER  maximum number of iterations of the main loop
  --tol TOL        tolerance for deciding on convergence
```

To see a run of the algorithm on example data and constraints, run the script `runner.sh` in the `examples` directory.

## Package install

Run this command to install this package.

```
% python setup.py install
```

Here is simple example to call this module

```python
import numpy
from copkmeans.cop_kmeans import cop_kmeans
input_matrix = numpy.random.rand(100, 500)
must_link = [(0, 10), (0, 20), (0, 30)]
cannot_link = [(1, 10), (2, 10), (3, 10)]
clusters, centers = cop_kmeans(dataset=input_matrix, k=5, ml=must_link,cl=cannot_link)
```

In the variable, `clusters`, you could see list of integer which has cluster number according to index of given data.


## Citing
If you want to cite this implementation, you can use the following bibtex entry (other formats are also [available](https://doi.org/10.5281/zenodo.275118)):

```
@misc{behrouz_babaki_2017_831850,
  author       = {Behrouz Babaki},
  title        = {COP-Kmeans version 1.5},
  month        = jul,
  year         = 2017,
  doi          = {10.5281/zenodo.831850},
  url          = {https://doi.org/10.5281/zenodo.831850}
}
```

## There's more ...

### Other implementations

- [Mateusz Zawiślak](https://github.com/mateuszzawislak) has a [java implementation](https://github.com/mateuszzawislak/k-means-clustering) of the COP-Kmeans algorithm.
- The R package [conclust](https://cran.r-project.org/web/packages/conclust/index.html) contains an implementation of COP-Kmeans, among a number of other constrained clustering algorithms.

### Other types of constraints

There is another version of constrained Kmeans that handles *size* constraints [[2][2]]. A python implementation of the algorithm (and its extensions) is available [here](https://github.com/Behrouz-Babaki/MinSizeKmeans).

### Exact algorithms for constrained clustering

In 2013-14, I was working on developing an integer linear programming
formulation for an instance of the constrained clustering problem. The
approach that I chose was *Branch-and-Price* (also referred to as
column-generation). In the initialization step of my algorithm, I needed another algorithm that can produce solutions of reasonably good quality very
quickly. The algorithm **COP-Kmeans** turned out to be exactly what I
was looking for. Interested in knowing more about my own work? Go to my
[homepage][page], from where you can access my paper [[3][3]] and the
corresponding code.

There is also a [body of work](https://cp4clustering.github.io/) on using constraint programming for exact constrained clustering. In particular, [[4][4]] is the state-of-the art in exact constrained clustering.

## References
1. Wagstaff, K., Cardie, C., Rogers, S., & Schrödl, S. (2001,
June). Constrained k-means clustering with background knowledge. In
ICML (Vol. 1, pp. 577-584).

2. Bradley, P. S., K. P. Bennett, and Ayhan Demiriz. "Constrained k-means clustering." Microsoft Research, Redmond (2000): 1-8.

3. Babaki, B., Guns, T., & Nijssen, S. (2014). Constrained clustering
using column generation. In Integration of AI and OR Techniques in
Constraint Programming (pp. 438-454). Springer International
Publishing.

4. Guns, Tias, Christel Vrain, and Khanh-Chuong Duong. "Repetitive branch-and-bound using constraint programming for constrained minimum sum-of-squares clustering." 22nd European Conference on Artificial Intelligence. 2016.

[1]: https://web.cse.msu.edu/~cse802/notes/ConstrainedKmeans.pdf
[2]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2000-65.pdf
[3]: https://lirias.kuleuven.be/bitstream/123456789/437301/3/Constrained_Clustering_using_Column_Generation.pdf
[4]: https://cp4clustering.github.io/ECAI16-CPRBBA.pdf
[page]: https://behrouz-babaki.github.io/#publications
