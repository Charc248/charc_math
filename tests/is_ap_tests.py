from nose.tools import *
from cmath.is_ap import *

def test_is_ap():
	assert_equal(is_ap([]),True)
	assert_equal(is_ap([2]),True)
	assert_equal(is_ap([2,4,6,8]),True)
	assert_equal(is_ap([1,2,3,4]),True)
	assert_equal(is_ap([3,1,4,2]),False)
	assert_equal(is_ap([1,3,5,6]),False)
	assert_equal(is_ap([1,3,5,7.000000001]),False)
	assert_equal(is_ap([1.2,2.4,3.6,4.8 + 1e-17],1e-18),False)
	assert_equal(is_ap([1.0/3,2.0/3,1,4.0/3]),True)
