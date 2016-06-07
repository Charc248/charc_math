from nose.tools import *
from cmath.gcd import *

def test_gcd():
    assert_equal(gcd(), 1)
    assert_equal(gcd(2), 2)
    assert_equal(gcd(2, 4, 6), 2)
    assert_equal(gcd(2, 3, 5), 1)
    assert_equal(gcd(5, 2, 3), 1)
    assert_equal(gcd(-2, 2), 2)
