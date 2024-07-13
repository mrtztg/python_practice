# import unittest
from challenges.ch001_find_missing_number import ch001_find_missing_number


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
#

def test_find_missing_number():
    assert ch001_find_missing_number([4,0,3,1]) == 2
    assert ch001_find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]) == 7