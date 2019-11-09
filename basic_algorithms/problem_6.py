def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if ints is None or len(ints) < 1:
        return None

    min_int = None
    max_int = None

    for i in ints:
        if min_int == None:
            min_int = i
            max_int = i

        if min_int > i :
            min_int = i

        if max_int < i:
            max_int = i

    return(min_int, max_int)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# test case 1: Test empty string input
# expected value: None
l = []
print ("Pass" if None == get_min_max(l) else "Fail")

# test case 2: Test input with multiple same values
# expected value: 1, 1
l = [1,1,1,1]
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

# test case 3:
# expected value: None
l = None
print ("Pass" if None == get_min_max(l) else "Fail")

