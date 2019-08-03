import unittest
from pycardvalidator.algorithm.luhn import Luhn

class TestLuhn(unittest.TestCase):

    def test_filter(self):
    	luhn_validator = Luhn()
        test_data = self.validation_provider()

        for input_case, output_case in test_data:
        	assert output_case == luhn_validator.validate(input_case)

    def validation_provider(self):
        return [
        	(5555555555554444, True),
            (5105105105105100, True),
            (4111111111111111, True),
            (4012888888881881, True),
            (79927398710, False),
            (79927398711, False),
            (79927398712, False),
            (79927398713, True),
            (79927398714, False),
            (79927398715, False),
            (79927398716, False),
            (79927398717, False),
            (79927398718, False),
            (79927398719, False),
        ]
