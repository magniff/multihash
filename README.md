# Python 3, PEP 247 compliant, multihash implementation.

[![Build Status](https://api.travis-ci.org/magniff/multihash.svg?branch=develop)](https://travis-ci.org/magniff/multihash)
[![codecov](https://codecov.io/gh/magniff/multihash/branch/develop/graph/badge.svg)](https://codecov.io/gh/magniff/multihash)

From the [multihash spec](https://github.com/jbenet/multihash), this
implementation is [PEP247](https://www.python.org/dev/peps/pep-0247/)
(`update(arg)`, `digest()`, `hexdigest()`, and `copy()`) compliant:

```python3
>>> import multihash
>>> m = multihash.sha1()
>>> m.update('foo'.encode())
>>> print(m.hexdigest())
11140beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33
```
