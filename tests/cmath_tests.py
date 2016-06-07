"""Standard test to make sure nosetesting works - even though i don't use nose here"""

#from nose.tools import *
import cmath

def test_cmath():
    "To make sure I can import safely!"
    print "I imported", cmath.__name__
