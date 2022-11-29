import unittest
import numpy as np
import scipy

# Importing medianFilter function
from medianFilter import medianFilter


class TestMyCode(unittest.TestCase):
    def test_medianFilter(self):
        data_for_test = [1, 2, 3, 6, 10, 7, 2, 1]
        result1 = medianFilter(data_for_test, 3)
        result2 = scipy.ndimage.median_filter(data_for_test, 3)
        compare = result1 == result2
        res = compare.all()
        if res == True:
            print("The function passed the check")
        else:
            print("The function did not pass the check")


if __name__ == "__main__":
    unittest.main()
