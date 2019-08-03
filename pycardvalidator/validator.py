from algorithm.luhn import Luhn
from filter.filter_default import FilterDefault

class Validator(object):
	"""
	The validator class handles filtering and validating credit card numbers

	Attributes:
		validate
	"""
	
	def validate(value):
		"""
		Main Validate Function to check credit cards

		Args:
			value (String)

		Returns:
			Boolean true or false, depending upon validation
		"""
		if not value:
			return False

		#Validate a credit card number. It will be filtered then validated and the result returned as a boolean.
		self.filter_object = self.get_filter()
		filtered_input_value = self.filter_object.filter(value)

		#Holds the algorithm model for processing validation
		self.algorithm = self.get_algorithm()

		return self.algorithm.validate(filtered_input_value)

	def get_filter(self):
		"""
		Gets the filter class to use for sanitising input data

		Args:
			None

		Returns:
			self with filter object set

		"""
		if not self.filter_object:
			self.filter_object = FilterDefault()
		return self

	def get_algorithm(self):
		"""
		Gets the algorithm class to use for validation

		Args:
			None

		Returns:
			self with algorithm object set

		"""
		if not self.algorithm:
			self.algorithm = Luhn()
		return self.algorithm

	def set_algorithm(self, algorithm):
		"""
		Sets the algorithm class to use for validation

		Args:
			None

		Returns:
			self with algorithm object set

		"""
		self.algorithm = algorithm
		return self

	def set_filter(self, filter_object):
		"""
		Sets the filter class to use for sanitising input data

		Args:
			None

		Returns:
			self with filter object set

		"""
		self.filter_object = filter_object
		return self




pycvalid = Validator()
		