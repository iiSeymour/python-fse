"""
Builds the C Python wrapper for https://github.com/Cyan4973/FiniteStateEntropy
"""

import os.path
from cffi import FFI
from glob import glob

src_path = os.path.abspath("src")
lib_path = os.path.join(src_path, "lib")
sources = os.path.join(lib_path, "*.c")

ffibuilder = FFI()

ffibuilder.set_source(
    "_fse",
    """
    #include <fse.h>
    #include <huf.h>
    """,
    include_dirs=[lib_path],
    libraries=["c"],
    sources=list(glob(sources)),
)

ffibuilder.cdef("""
unsigned FSE_isError(size_t code);
const char* FSE_getErrorName(size_t code);
size_t FSE_compressBound(size_t size);
size_t FSE_compress(void* dst, size_t dstCapacity, const void* src, size_t srcSize);
size_t FSE_decompress(void* dst,  size_t dstCapacity, const void* cSrc, size_t cSrcSize);

unsigned HUF_isError(size_t code);
const char* HUF_getErrorName(size_t code);
size_t HUF_compressBound(size_t size);
size_t HUF_compress(void* dst, size_t dstCapacity, const void* src, size_t srcSize);
size_t HUF_decompress(void* dst,  size_t originalSize, const void* cSrc, size_t cSrcSize);
""")


if __name__ == "__main__":
    ffibuilder.compile()
