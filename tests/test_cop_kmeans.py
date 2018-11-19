import unittest
from copkmeans import cop_kmeans
from typing import List, Tuple
import numpy


class TestCore(unittest.TestCase):

    def is_constraints_okay(self,
                            clustering_result: List[int],
                            seq_constraints: List[Tuple[int, int]],
                            constraints_type: str):
        # check if the given constraints are met or not.
        for t_constraint in seq_constraints:
            cluster_number_t_a = clustering_result[t_constraint[0]]
            cluster_number_t_b = clustering_result[t_constraint[1]]
            if constraints_type == "join":
                self.assertTrue(cluster_number_t_a == cluster_number_t_b)
            elif constraints_type == "non-join":
                self.assertTrue(cluster_number_t_a != cluster_number_t_b)
            else:
                raise Exception()

    def test_cop_kmeans(self):
        # initialize numpy array which random data.
        input_matrix = numpy.random.rand(100, 500)
        join_constraints = [(0, 10), (0, 20), (0, 30)]
        non_join_constrains = [(1, 10), (2, 10), (3, 10)]
        k = 5
        result = cop_kmeans.cop_kmeans(dataset=input_matrix,
                                       k=5,
                                       ml=join_constraints,
                                       cl=non_join_constrains)
        seq_cluster_number, seq_center_list = result
        self.assertTrue(isinstance(seq_center_list, list))
        self.is_constraints_okay(clustering_result=seq_cluster_number,
                                 seq_constraints=join_constraints,
                                 constraints_type="join")
        self.is_constraints_okay(clustering_result=seq_cluster_number,
                                 seq_constraints=non_join_constrains,
                                 constraints_type="non-join")

if __name__ == '__main__':
    unittest.main()