"""All the many many tests"""

from nose.tools import *
import charc_math as c

def test_charc_math():
    "To make sure I can import safely!"
    print "I imported", c.__name__

def test_gcd():
    "gcd function"
    assert_equal(c.gcd(), 1)
    assert_equal(c.gcd(2), 2)
    assert_equal(c.gcd(2, 4, 6), 2)
    assert_equal(c.gcd(2, 3, 5), 1)
    assert_equal(c.gcd(5, 2, 3), 1)
    assert_equal(c.gcd(-2, 2), 2)

def test_primes():
	assert_equal(c.primes(100), 
	    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
	     37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
	assert_equal(c.primes(2), [2])
	assert_equal(c.primes(-10), [])
	assert_equal(c.primes(1), [])

def test_lcm():
    assert_equal(c.lcm(), 1)
    assert_equal(c.lcm(2), 2)
    assert_equal(c.lcm(2, 4, 6), 12)
    assert_equal(c.lcm(2, 3, 5), 30)
    assert_equal(c.lcm(5, 2, 3), 30)
    assert_equal(c.lcm(-2, 2), 2)
    assert_equal(c.lcm(9, 3, 1), 9)
    assert_equal(c.lcm(9, 2, 2), 18)
    assert_equal(c.lcm(2, 2, 2, 2, 2, 2), 2)

def test_is_prime():
	assert_equal(c.is_prime(2), True)
	assert_equal(c.is_prime(3), True)
	assert_equal(c.is_prime(1301081), True)
	assert_equal(c.is_prime(-1), False)
	assert_equal(c.is_prime(0), False)
	assert_equal(c.is_prime(1), False)
	assert_equal(c.is_prime(1301081 ** 2), False)

def test_is_palindrome():
	assert_equal(c.is_palindrome(0), True)
	assert_equal(c.is_palindrome(1221), True)
	assert_equal(c.is_palindrome(13331), True)
	assert_equal(c.is_palindrome(787), True)
	assert_equal(c.is_palindrome(246), False)
	assert_equal(c.is_palindrome(10), False)
	assert_equal(c.is_palindrome(11), True)
	assert_equal(c.is_palindrome(121), True)
	assert_equal(c.is_palindrome(1234567890987654321), True)
	assert_equal(c.is_palindrome('332'), False)
	assert_equal(c.is_palindrome('121'), False)

def test_is_gp():
    assert_equal(c.is_gp([]), True)
    assert_equal(c.is_gp([2]), True)
    assert_equal(c.is_gp([2, 4, 8, 16]), True)
    assert_equal(c.is_gp([1, 2, 3, 4]), False)
    assert_equal(c.is_gp([3, 1, 4, 2]), False)
    assert_equal(c.is_gp([1, 3, 9, 28]), False)
    assert_equal(c.is_gp([1, 3, 9, 27.000000001]), False)
    assert_equal(c.is_gp([1.2 ** i for i in xrange(3)]), True) 
    # ^^ 4 breaks this.
    assert_equal(c.is_gp([1.0 / 3, 1.0 / 9, 1.0 / 27]), True)
    assert_equal(c.is_gp([1, 0, 0]), True)
    assert_equal(c.is_gp([1, 1, 0]), False)
    assert_equal(c.is_gp([0, 0, 0]), True)
    assert_equal(c.is_gp([0, 0, 1]), False)
    assert_equal(c.is_gp([2 ** i for i in xrange(1000)]), True)
    assert_equal(c.is_gp([2.3 ** i for i in xrange(3)]), True) 
    # ^^ 4 breaks this too.

def test_is_ap():
	assert_equal(c.is_ap([]), True)
	assert_equal(c.is_ap([2]), True)
	assert_equal(c.is_ap([2, 4, 6, 8]), True)
	assert_equal(c.is_ap([1, 2, 3, 4]), True)
	assert_equal(c.is_ap([3, 1, 4, 2]), False)
	assert_equal(c.is_ap([1, 3, 5, 6]), False)
	assert_equal(c.is_ap([1, 3, 5, 7.000000001]), False)
	assert_equal(c.is_ap([1.2, 2.4, 3.6, 4.8 + 1e-17], 1e-18), False)
	assert_equal(c.is_ap([1.0 / 3, 2.0 / 3, 1, 4.0 / 3]), True)

def test_to_base():
    for b in xrange(2, 100):
        assert_equal(c.to_base(b, b), [1, 0])
    assert_equal(c.to_base(10, 2), [1, 0, 1, 0])
    assert_equal(c.to_base(10, 3), [1, 0, 1])
    assert_equal(c.to_base(24, 5), [4, 4])
    assert_equal(c.to_base(24, 7), [3, 3])
    
def test_to_base10():
    for n in xrange(1000):
        for b in xrange(2, 100):
            assert_equal(c.to_base10(c.to_base(n, b), b), n)
