import unittest
from rotate_2d_matrix import rotate_2d_matrix

class TestRotate2DMatrix(unittest.TestCase):
    def test_rotate_2d_matrix(self):
        # Test rotation of a 3x3 matrix
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_rotated_matrix = [[7, 4, 1],
                                   [8, 5, 2],
                                   [9, 6, 3]]
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, expected_rotated_matrix)

    def test_empty_matrix(self):
        # Test rotation of an empty matrix
        matrix = []
        with self.assertRaises(ValueError):
            rotate_2d_matrix(matrix)

    def test_non_square_matrix(self):
        # Test rotation of a non-square matrix
        matrix = [[1, 2],
                  [3, 4],
                  [5, 6]]
        with self.assertRaises(ValueError):
            rotate_2d_matrix(matrix)

if __name__ == "__main__":
    unittest.main()
