def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if (number is None) or (not isinstance(number, int)) or (number < 0):
        print("The input should be an integer greater than 0")
        return

    start = 1
    end = number

    if (number == 0) or (number == 1):
        return number

    while start <= end:
        mid = (start + end) // 2

        # Found a match, return it
        if (mid * mid == number):
            return mid

        # update range to lower partition
        if (mid * mid > number):
            end = mid - 1
        # Update range to upper partition
        else:
            start = mid + 1
            result = mid
    return result

# Provided example
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# Test cases
print("Test case 1")
print ("Pass" if  (None == sqrt(-100)) else "Fail")  # Expects None when input is a negative number

print("Test case 2")
print ("Pass" if  (None == sqrt(None)) else "Fail")  # Expects None when input is None

print("Test case 3")
print ("Pass" if  (None == sqrt("abcdefg")) else "Fail")  # Expects None when input is a string type

print("Test case 4")
print ("Pass" if  (0 == sqrt(0)) else "Fail")  # Expects 0 when input is 0

print("Test case 5")
print ("Pass" if  (1 == sqrt(1)) else "Fail")  # Expects 1 when input is 1

print("Test case 6")
print ("Pass" if  (None == sqrt(16.5)) else "Fail")  # Expects None when input a decimal number