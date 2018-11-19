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
            if constraints_type == "must":
                self.assertTrue(cluster_number_t_a == cluster_number_t_b)
            elif constraints_type == "cannot":
                self.assertTrue(cluster_number_t_a != cluster_number_t_b)
            else:
                raise Exception()

    def test_cop_kmeans(self):
        # initialize numpy array which random data.
        input_matrix = numpy.random.rand(100, 500)
        must_link = [(0, 10), (0, 20), (0, 30)]
        cannot_link = [(1, 10), (2, 10), (3, 10)]
        k = 5
        result = cop_kmeans.cop_kmeans(dataset=input_matrix,
                                       k=5,
                                       ml=must_link,
                                       cl=cannot_link)
        seq_cluster_number, seq_center_list = result
        self.assertTrue(isinstance(seq_center_list, list))
        self.is_constraints_okay(clustering_result=seq_cluster_number,
                                 seq_constraints=must_link,
                                 constraints_type="must")
        self.is_constraints_okay(clustering_result=seq_cluster_number,
                                 seq_constraints=cannot_link,
                                 constraints_type="cannot")

if __name__ == '__main__':
    unittest.main()