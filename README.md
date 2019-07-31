# python-fse

[![Build Status](https://travis-ci.org/iiSeymour/pyfse.svg?branch=master)](https://travis-ci.org/iiSeymour/pyfse)

Python binding to [FiniteStateEntropy](https://github.com/Cyan4973/FiniteStateEntropy).

## Installing

```
$ pip install --user python-fse
```

## Example

```python
>>> import numpy as np
>>> from fse import fse_encode, fse_decode, huf_encode, huf_decode
>>>
>>> size = int(40e6)
>>> data = np.random.randint(0, 512, size=size)
>>> data.nbytes
320000000
>>> compressed = encode(data)
>>> compressed.nbytes
74042566
>>> recovered = decode(compressed, data.nbytes, data.dtype)
>>> compressed.nbytes / data.nbytes * 100
23.1350796875
```

## Development Quick Start

```
$ git clone --recurse-submodules https://github.com/iiSeymour/python-fse.git
$ python3 -m venv .venv
$ source .venv/bin/activate
$ make test
```
