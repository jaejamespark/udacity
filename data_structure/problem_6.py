class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here

    result = LinkedList()
    current_1 = llist_1.head

    # insert linkedlist 1 into result linkedlist
    while current_1 is not None:
        exists_in_result = False
        current_result = result.head
        while current_result is not None:
            if current_result.value == current_1.value:
                exists_in_result = True
                break
            current_result = current_result.next
        if not exists_in_result:
            result.append(current_1.value)
        current_1 = current_1.next

    # only insert the ones that only exists in linkedlist 2
    current_2 = llist_2.head
    while current_2 is not None:
        exists_in_result = False
        current_result = result.head
        while current_result is not None:
            if current_result.value == current_2.value:
                exists_in_result = True
                break
            current_result = current_result.next
        if not exists_in_result:
            result.append(current_2.value)
        current_2 = current_2.next
    return result


def intersection(llist_1, llist_2):
    # Your Solution Here

    result = LinkedList()
    current_1 = llist_1.head

    # Goes through linkedlist 1
    while current_1 is not None:
        value_1 = current_1.value
        current_2 = llist_2.head

        # Goes through linked list 2
        while current_2 is not None:
            value_2 = current_2.value

            exists_in_result = False
            if value_1 == value_2:
                current_result = result.head

                # Goes through result linkedlist
                # to avoid any duplicated entry
                while current_result:
                    if value_1 == current_result.value:
                        exists_in_result = True
                    current_result = current_result.next

                if not exists_in_result:
                    result.append(value_1)

            current_2 = current_2.next
        current_1 = current_1.next
    return result

def provided_example():
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))


def test_case_1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3]
    element_2 = [0, 2]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

def test_case_2():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3]
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


def test_case_3():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = ['rabbit', 'pig']
    element_2 = ['cat', 'dog', 'rabbit']

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))



if __name__ == "__main__":
    test_case_1()
    # Test scenario: Two linkedlists having few elements in them
    # Expected results:
    # union: {0,1,2,3}
    # intersection: {2}

    test_case_2()
    # Test scenario: One of the linkedlists having no elements in it
    # Expected results:
    # union: {1,2,3}
    # intersection: {}

    test_case_3()
    # Test scenario: Two linkedlists having string elements instead of integer elements
    # Expected results:
    # union: {rabbit, pig, cat, dog}
    # intersection: {rabbit}

    #provided_example()
