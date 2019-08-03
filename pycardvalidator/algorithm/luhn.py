import abc, six

@six.add_metaclass(abc.ABCMeta)
class AlgorithmInterface():
    """
    Algorithm classes should declare a public validate() method
    This abstract base class provides methods to be implemented by all validating algorithms
    """

    @abc.abstractmethod
    def validate(value):
        pass


class Luhn(AlgorithmInterface):
    """
    The Luhn algorthm is the industry standard for validating credit card numbers
    """

    def validate(self, value):
        value_sum = 0
        for index, val in enumerate(reversed(str(value))):
            even_pos = int(val) * (2 if index % 2 else 1)
            value_sum += sum(divmod(even_pos, 10))
        return value_sum % 10 == 0