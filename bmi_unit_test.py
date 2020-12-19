import unittest

from bmi_calculator import BMI_Caculator

def unit_test_bmi_calculator(height, weight):
    height_in_sq_metre = height/ 100
    unit_test_bmi_value = round(weight / height_in_sq_metre  ** 2, 2)
    return unit_test_bmi_value

class TestBmi(unittest.TestCase):
    def test_Bmi_Index(self):
        """
        Test that it can sum a list of integers
        """
        height_in_cm = 175
        weight_in_kg = 75
        result = BMI_Caculator(height_in_cm, weight_in_kg)
        unit_test_bmi_value = unit_test_bmi_calculator(height_in_cm, weight_in_kg)
        self.assertEqual(result, unit_test_bmi_value)

if __name__ == '__main__':
    unittest.main()