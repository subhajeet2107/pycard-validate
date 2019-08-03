from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name = 'pycard-validate',
    version = version,
    license = license,
    author = 'Subhajeet Dey',
    author_email = 'subhajeet2107@gmail.com',
    url = 'https://github.com/subhajeet2107/pycard-validate',
    description = 'Blazing Fast Credit Card number validator using Luhn Algorithm',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        'pytest',
        'six',
    ],
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'pycardvalidator = pycardvalidator.__main__:main',
        ]
    }
)
