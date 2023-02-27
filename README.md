# Vanilla Siteswap Validator
A simple siteswap validator to validate vanilla juggling patterns

Patterns are valid if:
1) Only valid characters are used (0-9 or a-z)
2) The number of balls required to juggle the pattern is an integer
3) No ball lands at the same time as any other ball

## Example usage
```python
from siteswap import Validator

validator = Validator()

to_validate = ['3', '441', '531', 'a0', 'TEST', '!£*&', '45', '321']

print("Siteswap | Valid")
print("---------|------")
for siteswap in to_validate:
	print(f"{siteswap:<8} | {validator.validate(siteswap)}")
```

### Example output
```
Siteswap | Valid
---------|------
3        | True
441      | True
531      | True
a0       | True
TEST     | False
!£*&     | False
45       | False
321      | False
```

# Multiplex Siteswap Validator
A simple siteswap validator to validate multiplex juggling patterns

Patterns are valid if:
1) Only valid characters are used (0-9, a-z, or [ ])
2) Usage of [ ] is syntactically correct
3) The number of balls required to juggle the pattern is an integer
4) The number of balls which land at any given beat matches the number of balls thrown on the same beat

## Example usage
```python
from siteswap import MultiplexValidator

validator = MultiplexValidator()

to_validate = ['3', '441', 'TEST', '321', '[22]0', '[a2]0', '[32][32]', '[32][]', '[75]3', '[32][33]', '[11]2', '[2[22]]2', ']3[']

print("Siteswap | Valid")
print("---------|------")
for siteswap in to_validate:
	print(f"{siteswap:<8} | {validator.validate(siteswap)}")
```

### Example output
```
Siteswap | Valid
---------|------
3        | True
441      | True
TEST     | False
321      | False
[22]0    | True
[a2]0    | True
[32][32] | True
[32][]   | False
[75]3    | False
[32][33] | False
[11]2    | False
[2[22]]2 | False
]3[      | False
```
