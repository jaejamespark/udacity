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
        return []

    if suffix is None:
        raise ValueError("ValueError: suffix not provided")

    results = []
    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item.endswith(suffix):
            results.append(item_path)
        elif os.path.isdir(item_path):
            results.extend(find_files(suffix, os.path.join(path, item)))
    return results

c = find_files(".c", "./testdir")
print('results')
print(c)

def test_case_1():
    # Test scenario: Tests when path is None
    # Expected output: an empty list
    suffix = ".c"
    path = None
    result = find_files(suffix, path)
    print(result)


def test_case_2():
    # Test scenario: Tests when path is None
    # Expected output: an empty list
    suffix = None
    path = "./"
    try:
        result = find_files(suffix, path)
    except ValueError as e:
        print(str(e))


def test_case_3():
    # Test scenario: Finds .py files in current directory
    # Expected output: an empty list
    suffix = ".py"
    path = "./"
    result = find_files(suffix, path)
    print(result)


if __name__ == "__main__":
    test_case_1()
    # output is an empty list

    test_case_2()
    # output is an ValueError message

    test_case_3()
    # output is a list of .py files if they exists in the path