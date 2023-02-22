#! /usr/bin/env python3

from siteswap import Validator

validator = Validator()

# Valid
validator.validate('3')
validator.validate('441')
validator.validate('531')
validator.validate('a0')

# Invalid
validator.validate('TEST')
validator.validate('!£*&')

# Invalid number of balls
validator.validate('45')

# Invalid collisions
validator.validate('321')