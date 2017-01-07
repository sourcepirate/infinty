##INFINITE

[![Build Status](https://travis-ci.org/plasmashadow/infinty.svg?branch=master)](https://travis-ci.org/plasmashadow/infinty)

Bunch of infinite series and tools to generate infinite series.

##Usage

```python

from infinity import series

## Let me generate a series for 2n + 1.
## Since the series doesn't have any initial value.
@series()
def formulae(n):
  return 2*n + 1

##Let me genrate a series for 2kn + 24
## since the series takes k as inital value

@series(2)
def formulae_2(k, n):
  return 2*k*n + 24


sofn = formulae_2()

print(next(sofn))
print(next(sofn))

```


## License

MIT
