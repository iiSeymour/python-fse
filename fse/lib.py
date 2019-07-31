"""
Python bindings for https://github.com/Cyan4973/FiniteStateEntropy
"""

import numpy as np

from _fse import lib, ffi


def fse_encode(data):

    dst_size = lib.FSE_compressBound(data.nbytes)
    dst = np.empty(dst_size, dtype=np.uint8)
    
    size = lib.FSE_compress(
        ffi.cast("void *", ffi.from_buffer(dst)),
        dst_size,
        ffi.cast("void *", ffi.from_buffer(data)),
        data.nbytes
    )

    if size == 0:
        raise Exception("Data is not compressible")
    elif size == 1:
        raise Exception("Use RLE compression instead")
    elif lib.FSE_isError(size):
        err_msg = ffi.string(lib.FSE_getErrorName(size))
        raise Exception(err_msg.decode('utf-8'))

    return dst[:size]


def fse_decode(data, n, dtype):

    dst = np.empty(n, dtype=dtype)
    try:
        dst_size = n * dtype.itemsize
    except TypeError:
        dst_size = n * dtype().itemsize

    size = lib.FSE_decompress(
        ffi.cast("void *", ffi.from_buffer(dst)),
        dst_size,
        ffi.cast("void *", ffi.from_buffer(data)),
        data.nbytes
    )
    
    if lib.FSE_isError(size):
        err_msg = ffi.string(lib.FSE_getErrorName(size))
        raise Exception(err_msg.decode('utf-8'))
    
    return dst[:size]


def huf_encode(data):
    
    # HUF_BLOCKSIZE_MAX 128 * 1024
    if data.nbytes > 131072:
        raise Exception("Data size must be less than 128KB")

    dst_size = lib.HUF_compressBound(data.nbytes)
    dst = np.empty(dst_size, dtype=np.uint8)
    
    size = lib.HUF_compress(
        ffi.cast("void *", ffi.from_buffer(dst)),
        dst_size,
        ffi.cast("void *", ffi.from_buffer(data)),
        data.nbytes
    )

    if size == 0:
        raise Exception("Data is not compressible")
    elif lib.HUF_isError(size):
        err_msg = ffi.string(lib.HUF_getErrorName(size))
        raise Exception(err_msg.decode('utf-8'))

    return dst[:size]


def huf_decode(data, n, dtype):

    dst = np.empty(n, dtype=dtype)
    try:
        dst_size = n * dtype.itemsize
    except TypeError:
        dst_size = n * dtype().itemsize
    
    size = lib.HUF_decompress(
        ffi.cast("void *", ffi.from_buffer(dst)),
        dst_size,
        ffi.cast("void *", ffi.from_buffer(data)),
        data.nbytes
    )
    
    if lib.HUF_isError(size):
        err_msg = ffi.string(lib.HUF_getErrorName(size))
        raise Exception(err_msg.decode('utf-8'))
    
    return dst[:size]
    

