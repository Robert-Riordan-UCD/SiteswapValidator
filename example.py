#! /usr/bin/env python3

from siteswap import Validator

validator = Validator()

to_validate = ['3', '441', '531', 'a0', 'TEST', '!£*&', '45', '321']

print("Siteswap | Valid")
print("---------|------")
for siteswap in to_validate:
	print(f"{siteswap:<8} | {validator.validate(siteswap)}")

validator.print_details('3')
validator.print_details('441')
validator.print_details('a0')
validator.print_details('45')
