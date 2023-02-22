# SiteswapValidator
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
