def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    n1 = 0
    n2 = 0

    d = [0 for _ in range(10)]
    for n in input_list:
        d[n] += 1

    i = 9
    even = 0
    cdt = True
    while cdt:
        if d[i] > 0:
            if even == 0:
                n1 = (n1 * 10) + i
                even = 1
            else:
                n2 = (n2 * 10) + i
                even = 0
            d[i] -= 1

        if d[i] == 0:
            i -= 1

        if i == 0 & d[i] == 0:
            cdt = False

    return n1, n2


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Provided example
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# Test case 1: Test for empty input
# Expected output: empty input
test_case = [[], []]
test_function(test_case)

# Test case 2: Test for 1 input
# Expected output: [1]
test_case = [[1], [1]]
test_function(test_case)

# Test case 3: Test for odd number of same digits as input
# Expected output: [11, 11]
test_case = [[1,1,1], [11, 1]]
test_function(test_case)