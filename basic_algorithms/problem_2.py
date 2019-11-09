def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # input validations
    if input_list is None or len(input_list) < 1:
        return -1

    if None in input_list:
        return -1

    # find pivot index
    # pivot_index is -1 if pivot does not exist
    pivot_index = find_pivot(input_list, 0, len(input_list) - 1)

    # The input list has a pivot
    # Check if the pivot index has the number
    if pivot_index != -1:
        if input_list[pivot_index] == number:
            return pivot_index

        # set start and end
        if input_list[0] > number:
            start = pivot_index + 1
            end = len(input_list) - 1
        else:
            start = 0
            end = pivot_index -1
    else:
        # The input list has no pivot
        start = 0
        end = len(input_list) - 1

    mid = (start + end) // 2

    # do binary search
    while start <= end:
        # Found a match, return it
        if input_list[mid] == number:
            return mid

        # update range to lower partition
        if input_list[mid] > number:
            end = mid - 1
        # Update range to upper partition
        else:
            start = mid + 1

        mid = (start + end) // 2

    return -1


def find_pivot(input_list, start, end):
    # input list has no pivot. Returns -1
    if input_list[start] < input_list[end]:
        return -1

    mid = (start + end) // 2

    if mid < end and input_list[mid] > input_list[mid + 1]:
        return mid
    elif mid > start and input_list[mid - 1] > input_list[mid]:
        return mid - 1
    elif input_list[start] >= input_list[mid]:
        return find_pivot(input_list, start, mid - 1)
    return find_pivot(input_list, mid + 1, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


print("Test case 1")
test_function([[], 10]) # Tests for empty list as an input. Expects -1

print("Test case 2")
test_function([[None, 1, 2], 10]) # Tests when input list has None value. Expects -1

print("Test case 3") # Tests when the input list has no pivot. Expects 3.
test_function([[1, 2, 3, 4, 5], 4])

print("Test case 4") # Tests when the input list has a pivot. Expects 4.
test_function([[3, 4, 5, 6, 1, 2], 1])