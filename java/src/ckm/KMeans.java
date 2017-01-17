package ckm;

import java.util.ArrayList;

public class KMeans {
	private double centroid_diff(ArrayList<ArrayList<Double>> first,
			ArrayList<ArrayList<Double>> second) {
		int k = first.size();
		int dim = first.get(0).size();
		double total_diff = 0;
		for (int i = 0; i < k; i++)
			for (int j = 0; j < dim; j++)
				total_diff += Math.abs(first.get(i).get(j)
						- second.get(i).get(j));
		return total_diff;
	}

	private double point_diff(ArrayList<Double> first, ArrayList<Double> second) {
		int dim = first.size();
		double total_diff = 0;
		for (int i = 0; i < dim; i++)
			total_diff += Math.pow(first.get(i) - second.get(i), 2);
		return total_diff;
	}

	private void find_closest(ArrayList<Double> instance,
			ArrayList<ArrayList<Double>> centroids, Integer cluster_id,
			Double distance_to_centroid) {
		int k = centroids.size();
		double diff = point_diff(instance, centroids.get(0));
		double least_diff = diff;
		int closest = 0;

		for (int i = 1; i < k; i++) {
			diff = point_diff(instance, centroids.get(i));
			if (diff < least_diff) {
				least_diff = diff;
				closest = i;
			}
		}
		cluster_id = closest;
		distance_to_centroid = least_diff;
	}

	public void kmeans(ArrayList<ArrayList<Double>> data, int k,
			ArrayList<Integer> init, double tol, ArrayList<Integer> clusters) {
		int n = data.size();
		int dim = data.get(0).size();

		ArrayList<ArrayList<Double>> centroids = new ArrayList<ArrayList<Double>>();
		ArrayList<ArrayList<Double>> old_centroids = new ArrayList<ArrayList<Double>>();
		ArrayList<Integer> cluster_sizes = new ArrayList<Integer>();
		
		for (int i=0; i<k; i++) {
			ArrayList<Double> centroid = new ArrayList<Double>();
			for (int j=0; j<dim; j++)
				centroid.add(0.0);
			old_centroids.add(centroid);
		}
			
		for (int i = 0; i < k; i++) {
			centroids.add(new ArrayList<>(init.get(i)));
			cluster_sizes.add(-1);
		}
		

	}

}
