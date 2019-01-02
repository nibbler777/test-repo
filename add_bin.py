import sys

def add_bin(one, two):
    one = [int(x) for x in one]
    two = [int(x) for x in two]
    one_rev = one[::-1]
    two_rev = two[::-1]
    carry = False
    summed = list()
    for x,y in zip(one_rev, two_rev):
        if carry and (x and y):
            carry = True
            summed.insert(0, 1)
        elif carry and (x or y):
            carry = True
            summed.insert(0, 0)
        elif carry and not (x or y):
            carry = False
            summed.insert(0, 1)
        elif (x and y):
            carry = True
            summed.insert(0, 0)
        elif (x or y):
            carry = False
            summed.insert(0, 1)
        elif not (x or y):
            carry = False
            summed.insert(0, 0)
    #if len(summed) > 8:
    #    summed = summed[len(summed)-8:]
    return summed 

print add_bin(sys.argv[1], sys.argv[2])



