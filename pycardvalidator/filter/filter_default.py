import abc, six


@six.add_metaclass(abc.ABCMeta)
class FilterInterface():
	"""
	Filter classes should filter incoming data against a variety of conditions
	This abstract base class provides methods to be implemented by Filters
	"""

	@abc.abstractmethod
	def filter(value):
		pass


class FilterDefault(FilterInterface):
	"""
	The default filter will strip whitespaces and dashes from the incoming data
	"""

	def filter(self, value):
		cleaned_value = value.replace(' ','-')
		cleaned_value = cleaned_value.replace('-','')
		return cleaned_value
		