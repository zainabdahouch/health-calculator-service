import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)

    def test_calculate_bmr(self):
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'male'), 1695.67, places=2)
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'female'), 1507.13, places=2)

if __name__ == '__main__':
    unittest.main()
