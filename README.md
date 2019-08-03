pycard-validator
==========================

A simple python module to implement credit card number validation using Luhn Algorithm.
[![Build Status](https://travis-ci.org/subhajeet2107/pycard-validate.svg?branch=master)](https://travis-ci.org/subhajeet2107/pycard-validate) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)


## Installation

Install in your project with pip:

```bash
pip install pycard-validate
```

## Usage

An example use:

```python
import pycardvalidator
result = pycardvalidator.validate('4111 1111 1111 1111') # returns True
```

## License

MIT license. See `LICENSE.md` for more information.