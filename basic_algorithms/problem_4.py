def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        return []

    current_index = 0
    offset = 0
    while current_index + offset < len(input_list):
        if input_list[current_index] == 0:
            input_list.pop(current_index)
            input_list.insert(0, 0)
        elif input_list[current_index] == 2:
            input_list.pop(current_index)
            input_list.append(2)
            current_index -= 1  # Move to previous index because 2 is moved to the end
            offset += 1  # increase the offset since the current index moved 1 back

        current_index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Provided case:
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# Test case 1: Tests when input is an single element list. Expects the single element list
test_function([2])
test_function([0])
test_function([1])

# Test case 2: Tests when input is empty. Expects an empty list as an output
test_function([])

# Test case 3: Tests when input is None. Expects an empty list as an output
test_function([None])