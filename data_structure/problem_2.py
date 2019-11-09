import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None:
        raise ValueError("ValueError: path not provided")

    if suffix is None:
        raise ValueError("ValueError: suffix not provided")

    if not os.path.exists(path):
        raise FileNotFoundError("FileNotFoundError: The path does not exist")

    results = []
    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item.endswith(suffix):
            results.append(item_path)
        elif os.path.isdir(item_path):
            results.extend(find_files(suffix, os.path.join(path, item)))
    return results

#c = find_files(".c", "./testdir")
#print('results')
#print(c)

def test_case_1():
    # Test scenario: Tests when path is None
    # Expected output: ValueError
    suffix = ".c"
    path = None
    try:
        result = find_files(suffix, path)
    except ValueError as e:
        print("PASS: expected result received. " + str(e))
    else:
        print("FAIL: expected result not received. Expected ValueError")


def test_case_2():
    # Test scenario: Tests when suffix is None
    # Expected output: an empty list
    suffix = None
    path = "./"
    try:
        result = find_files(suffix, path)
    except ValueError as e:
        print("PASS: expected result received. " + str(e))
    else:
        print("FAIL: expected result not received. Expected ValueError")


def test_case_3():
    # Test scenario: Finds .py files in current directory
    # Expected output: a list of .py files (if exists)
    suffix = ".py"
    path = "./"
    result = find_files(suffix, path)

    print("PASS: expected result received.")
    print(result)

def test_case_4():
        # Test scenario: Finds .py files in not-existing path
        # Expected output: FileNotFound Exception
        suffix = ".py"
        path = "NOT_EXITING_PATH___"
        try:
            result = find_files(suffix, path)
        except FileNotFoundError as e:
            print("PASS: Expected FileNotFoundError exception received. " + str(e))
        else:
            print("FAIL: Expecting FileNotFoundError exception but not received")



if __name__ == "__main__":
    test_case_1()
    # Test scenario: Tests when path is None
    # Expected output: an empty list

    test_case_2()
    # Test scenario: Tests when suffix is None
    # Expected output: an empty list

    test_case_3()
    # Test scenario: Finds .py files in current directory
    # Expected output: a list of .py files (if exists)

    test_case_4()
    # Test scenario: Finds .py files in not-existing path
    # Expected output: FileNotFound Exception