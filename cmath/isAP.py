# Code:
def isAP(l):
    """
    Calculates the common differences and checks if they are the same
        to find if the list is an arithmetic progression.
    @arg l    The list to check
    @ret      Boolean
    """
    l2 = []
    for i in range(0, len(l) - 1):
        l2.append(l[i + 1] - l[i])
    if len(set(l2)) == 1:
       # print "This is an AP!"
       # print "u_n = %d + %d * n\n" % (l[0], l2[0])
        return True
    else:
        return False


# Bugs:
# isAP([1.0/3,2.0/3,1,4.0/3])=False
# Numerical precision :(
