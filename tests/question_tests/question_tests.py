#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import sum_even
from src.question_b.question_b import get_miles_per_hour
from src.question_c.question_c import get_day_of_week
from src.question_d.question_d import use_global
global_variable = 10
class Test_Config(unittest.TestCase):
    def test_question_a_config(self):
        self.assertEqual(30, sum_even(11))
        self.assertEqual(30, sum_even(10))
        self.assertEqual(20, sum_even(8))

    def test_question_b_config(self):
        self.assertEqual(19.883872 , get_miles_per_hour(32,60))

    def test_question_c_config(self):
        self.assertEqual("Invalid number", get_day_of_week(0))
        self.assertEqual("Monday", get_day_of_week(1))
        self.assertEqual("Tuesday", get_day_of_week(2))
        self.assertEqual("Wednesday", get_day_of_week(3))
        self.assertEqual("Invalid number", get_day_of_week(8))
    
    def test_question_d_config(self):
        self.assertEqual(20 , use_global())