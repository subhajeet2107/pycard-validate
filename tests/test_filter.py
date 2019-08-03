import unittest
from pycardvalidator.filter.filter_default import FilterDefault

class TestFilterDefault(unittest.TestCase):

    def test_filter(self):
    	filter_default = FilterDefault()
        test_data = self.filter_provider()

        for input_case, output_case in test_data:
        	assert output_case == filter_default.filter(input_case)

    def filter_provider(self):
        return [
        	('        ', ''),
        	('   - - -     - - - ', ''),
        	('A string with spaces', 'Astringwithspaces'),
        	('A-string-with-dashes and spaces', 'Astringwithdashesandspaces'),
        	('  Spaces at start, dashes at end---', 'Spacesatstart,dashesatend')
        ]
