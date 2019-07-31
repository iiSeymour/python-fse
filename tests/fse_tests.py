import numpy as np
from unittest import TestCase, main
from numpy.testing import assert_array_equal

from fse import fse_encode, fse_decode, huf_encode, huf_decode


class Tests:
    """ Base test functions for all encoding/decoding functions """
    def test_decode(self):
        """ S1: simple decode """
        res = self.encode(self.data)
        rec = self.decode(res, len(self.data), self.data.dtype)
        assert_array_equal(self.data, rec)


class BasicTest(Tests):
    """ Base test for encoding and decoding with small simple test case """
    def setUp(self):
        self.data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.uint32)


class RandTest(Tests):
    """ Base test encoding and decoding with large random array """
    def setUp(self):
        self.data = np.random.randint(0, 1024, 20000, np.uint32)


class FSE:
    def encode(self, *args): 
        return fse_encode(*args)

    def decode(self, *args):
        return fse_decode(*args)


class HUF:
    def encode(self, *args): 
        return huf_encode(*args)

    def decode(self, *args):
        return huf_decode(*args)


class FSEBasicTest(FSE, BasicTest, TestCase):
    pass


class HUFBasicTest(HUF, BasicTest, TestCase):
    pass


class FSERandTest(FSE, RandTest, TestCase):
    pass


class HUFRandTest(HUF, RandTest, TestCase):
    pass


if __name__ == '__main__':
    main()
