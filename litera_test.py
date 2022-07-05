import unittest
from litera import isOverlap
from litera import double_booked

class TestLitera(unittest.TestCase):
    #test for negative values
    def test_isOverlap_negative(self):
        self.assertRaises(ValueError, isOverlap,[-1,0], [1,2])
    #tests for start time being greater than end time
    def test_isOverlap_start_greater_than_end(self):
        self.assertRaises(ValueError, isOverlap,[3,1], [1,2])
        self.assertRaises(ValueError, isOverlap,[1,2], [6,4])
    #tests for overlapping of two events
    def test_isOverlap(self):
        self.assertEqual(True, isOverlap([0, 3], [1,4]))
        self.assertEqual(False, isOverlap([0, 3], [4,7]))

    #tests if empty list is given with no intervals
    def test_double_booked_empty(self):
        self.assertEqual([], double_booked([]))
    #tests if no overlap is found, or only one interval as input
    def test_dobule_booked_noOverLap(self):
        self.assertEqual([], double_booked([[1,2], [2,3]]))
        self.assertEqual([], double_booked([[1,2]]))
    #tests a small set of intervals
    def test_dobule_booked_small(self):
        self.assertEqual([[[2, 10], [3, 4]], [[2, 10], [6, 9]]], double_booked([[2, 10], [3, 4], [6, 9]]))
    #tests a large set of intervals
    def test_double_booked_large(self):
        self.assertEqual([[[1, 3], [2, 4]], [[1, 3], [2, 5]], [[2, 4], [2, 5]], [[2, 4], [3, 4]], [[2, 4], [3, 6]], [[2, 5], [3, 4]], [[2, 5], [3, 6]], [[2, 5], [4, 5]], [[3, 4], [3, 6]], [[3, 6], [4, 5]], [[3, 6], [5, 6]]], 
        double_booked([[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]]))

if __name__ == '__main__':
    unittest.main()