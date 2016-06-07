from nose.tools import *
from cmath.is_gp import *

def test_is_gp():
    assert_equal(is_gp([]),True)
    assert_equal(is_gp([2]),True)
    assert_equal(is_gp([2,4,8,16]),True)
    assert_equal(is_gp([1,2,3,4]),False)
    assert_equal(is_gp([3,1,4,2]),False)
    assert_equal(is_gp([1,3,9,28]),False)
    assert_equal(is_gp([1,3,9,27.000000001]),False)
    assert_equal(is_gp([1.2**i for i in range(3)]),True) # 4 breaks this.
    assert_equal(is_gp([1.0/3,1.0/9,1.0/27]),True)
    assert_equal(is_gp([1,0,0]),True)
    assert_equal(is_gp([1,1,0]),False)
    assert_equal(is_gp([0,0,0]),True)
    assert_equal(is_gp([0,0,1]),False)
    assert_equal(is_gp([2**i for i in range(1000)]),True)
    assert_equal(is_gp([2.3**i for i in range(3)]),True) # 4 breaks this too.
