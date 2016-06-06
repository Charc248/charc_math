import math as m
from .isAP import *

# Code:
def isGP(l):
    """
    Calculates the log of the sequence and checks if this is an AP
    @arg l  The list to check
    @ret    Boolean
    """
    if set(l) == {0}:
         return True
    elif 0 in l:
	return False

    l2 = []
    for i in range(0, len(l)):
        l2.append(m.log10(l[i]))
    if isAP(l2):
       # print "This is a GP!"
       # print "u_n = %f * %f ^n" % (l[0],
       #     (1.0 * l[i+1]) / (l[i] * 1.0))
        return True
    else:
        return False


# Bugs:
# Relies on isAP so precision!
# isGP([2,4,8,16])=False 
# This one is perhaps not that good.
