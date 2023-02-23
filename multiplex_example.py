#! /usr/bin/env python3

from siteswap import MultiplexValidator

validator = MultiplexValidator()

to_validate = ['3', '441', '531', 'a0', 'TEST', '!£*&', '45', '321', '[22]0', '[a2]0', '[32][32]', '[32][]', '45', '[75]3', '[32][33]']

print("Siteswap | Valid")
print("---------|------")
for siteswap in to_validate:
	print(f"{siteswap:<8} | {validator.validate(siteswap)}")

print()

validator.print_details('3')
validator.print_details('441')
validator.print_details('a0')
validator.print_details('[22]0')
validator.print_details('[a2]0')
validator.print_details('4[a2]')
validator.print_details('[32][32]')
validator.print_details('[234]021')
validator.print_details('[32][]') # Invalid syntax
validator.print_details('45') # Invalid number of balls
validator.print_details('[75]3') # Invalid number of balls
validator.print_details('[32][33]') # Invalid [xx][xx] -> [xxx][x]
validator.print_details('[11]2') # Invalid disappearing balls
