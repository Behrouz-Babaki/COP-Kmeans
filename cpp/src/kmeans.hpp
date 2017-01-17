#ifndef KMEANS_HPP
#define KMEANS_HPP

#include <vector>
#include <utility>
#include <algorithm>

using std::vector;
using std::pair;
using std::make_pair;
using std::sort;

inline double centroid_diff (const vector< vector< double > >& first, 
			     const vector< vector< double > >& second) {
  int k = first.size();
  int dim = first[0].size();
  double diff, abs_diff, total_diff;
  
  total_diff= 0;
  for (int i=0; i<k; i++) 
    for (int j=0; j<dim; j++) {
      diff = first[i][j] - second[i][j];
      abs_diff = diff > 0 ? diff : -diff;
      total_diff += abs_diff;
    }
   return total_diff;
}

inline double point_diff(const vector< double >& first, 
			 const vector< double >& second) {
  int dim = first.size();
  double diff, total_diff;
  
  total_diff = 0;
  for (int i=0; i<dim; i++) {
      diff = first[i] - second[i];
      total_diff += (diff * diff);
  }
  return total_diff;
}

inline void find_closest(const vector< double >& instance, 
			 const vector< vector< double > >& centroids,
			 int& cluster_id,
			 double& distance_to_centroid){
  int k = centroids.size();
  double diff = point_diff(instance, centroids[0]);
  double least_diff = diff;
  int closest = 0;
  
  for (int i=1; i<k; i++) {
    diff = point_diff(instance, centroids[i]);
    if (diff < least_diff) {
      least_diff = diff;
      closest = i;
    }
  }
  cluster_id = closest;
  distance_to_centroid = least_diff;
}

inline void kmeans(const vector< vector< double > >& data, 
		   int k,
		   const vector< int >& init, 
		   double tol,
		   vector< int >& clusters) {
  int n = data.size();
  int dim = data[0].size();

  vector< vector< double > > centroids(k);
  vector< vector< double > > old_centroids(k, vector< double >(dim));
  vector< int > cluster_sizes(k, -1);
  vector< pair< double, int > > min_distances(n);

  /* initialize centroids */
  for (int i=0; i<k; i++) 
    centroids[i] = data[init[i]];
  
  /* kmeans iterations */
  do {
    
    /* assign data points to closest clusters */
    cluster_sizes.assign(k, 0);
    for (int i=0; i<n; i++) {
      int cluster_id;
      double distance_to_centroid;
      find_closest(data[i], centroids, 
		   cluster_id, distance_to_centroid);
      cluster_sizes[cluster_id]++;
      clusters[i] = cluster_id;
      min_distances[i] = make_pair(distance_to_centroid, i);
    }
    
    /* copy the centroids */
    for (int i=0; i<k; i++)
      for (int j=0; j<dim; j++) {
	old_centroids[i][j] = centroids[i][j];
	centroids[i][j] = 0;
      }

    /* assigning furthest points to the empty clusters */  
    vector<int> empty_clusters;
    for (int i=0; i<k; i++)
      if (cluster_sizes[i] == 0)
	  empty_clusters.push_back(i);
    
    if (empty_clusters.size() > 0) {
      sort(min_distances.begin(), min_distances.end());
      for (int i=0, s=empty_clusters.size(); i<s; i++) {
	int point_id = min_distances[n-i].second;
	int cluster_id = empty_clusters[i];
	clusters[point_id] = cluster_id;
	cluster_sizes[cluster_id] = 1;
      }
    }
      
    /* compute the new centroids */
    for (int i=0; i<n; i++) 
      for (int j=0; j<dim; j++) 
	centroids[clusters[i]][j] += data[i][j];
    
    for (int i=0; i<k; i++)
	for (int j=0; j<dim; j++)
	  centroids[i][j] /= cluster_sizes[i];
    
  } while (centroid_diff(centroids, old_centroids) > tol);
  
}
	    

#endif //KMEANS_HPP