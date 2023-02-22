#! /usr/bin/env python3

from siteswap import Validator

validator = Validator()

to_validate = ['3', '441', '531', 'a0', 'TEST', '!£*&', '45', '321']

for siteswap in to_validate:
	print(f"{siteswap:<8} {validator.validate(siteswap)}")
