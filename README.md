# pyfse

Python binding to [https://github.com/Cyan4973/FiniteStateEntropy](FiniteStateEntropy).

## Installing

$ pip install --user pyfse

## Example

```
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
$ git clone --recurse-submodules https://github.com/iiSeymour/pyfse.git
$ python3 -m venv .venv
$ source .venv/bin/activate
$ make test
```