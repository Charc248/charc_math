from nose.tools import *
from cmath.primes import *

def test_primes():
	assert_equal(primes(100),[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
	assert_equal(primes(2),[2])
	assert_equal(primes(-10),[])
	assert_equal(primes(1),[])

