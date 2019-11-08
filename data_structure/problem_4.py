class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        raise ValueError("ValueError: invalid input")

    users = group.get_users()
    if user in users:
        return True

    sub_groups = group.get_groups()
    for sub_group in sub_groups:
        if is_user_in_group(user, sub_group):
            return True
    return False


def test_case_1():
    # Test scenario: Test for a user that exists in the group
    # Expected result: True
    print(is_user_in_group("sub_child_user", parent))


def test_case_2():
    # Test scenario: Test for a user that does not exist in the group
    # Expected result: True
    print(is_user_in_group("no_one", parent))

def test_case_3():
    # Test scenario: Test for a case when the group is None
    # Expected result: ValueError
    try:
        is_user_in_group("sub_child_user", None)
    except ValueError as e:
        print(str(e))


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


if __name__ == "__main__":
    test_case_1()
    # Expected output: True

    test_case_2()
    # Expected output: False

    test_case_3()
    # Expected output: "ValueError: invalid input"