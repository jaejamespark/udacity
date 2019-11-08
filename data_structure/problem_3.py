import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def huffman_encoding(data):
    # Input validation
    if (data is None) or (len(data) < 1):
        return None, None

    dic = {}
    for c in data:
        dic[c] = dic.get(c, 0) + 1

    # make tuples with character frequency for sorting
    letters = []
    for k, v in dic.items():
        letters.append((v, Node(k)))

    # Generates the tree
    root = None
    if len(letters) <= 0:
        return
    elif len(letters) == 1:
        root = letters[0][1]
    else:
        while len(letters) > 1:
            letters = sorted(letters, key=lambda x: x[0])
            # joint two node
            l = letters.pop(0)
            r = letters.pop(0)
            v = l[0] + r[0]  # sum char freq
            root = Node(v)
            root.left = l[1]
            root.right = r[1]
            letters.append((v, root))
        root = letters[0][1]

    # Make encoding map for each character
    dec_dict = dict()
    dec_dict['codes'] = ''
    generate_code(root, dec_dict)

    # Encode the data
    encoded_data = ''
    for c in data:
        encoded_data += dec_dict[c]

    return encoded_data, root


def generate_code(root, dec_dict):
    if root:
        if (root.left is None) and (root.right is None):
            dec_dict[root.value] = dec_dict['codes']
            return dec_dict

        if root.left:
            dec_dict['codes'] += '0'
            generate_code(root.left, dec_dict)

        dec_dict['codes'] = dec_dict['codes'][:len(dec_dict['codes']) - 1]

        if root.right:
            dec_dict['codes'] += '1'
            generate_code(root.right, dec_dict)

        dec_dict['codes'] = dec_dict['codes'][:len(dec_dict['codes']) - 1]

    return dec_dict


def huffman_decoding(data, tree):
    # Input validation
    if (data is None) or (tree is None):
        return None

    node = tree
    result = ''
    for d in data:

        if d == '0':
            # if node.left:
            node = node.left

        if d == '1':
            # if node.right:
            node = node.right

        if (not node.left) and (not node.right):
            result += node.value
            node = tree

    #print(result)
    return result


def provided_example():
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


def test_case_1():
    # Test scenario: Test when input is a string.
    # Expected output: the original data which is "Hello world"
    a_great_sentence = "Hello world"
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == a_great_sentence, "ERROR: original data and decoded data are different"
    print("original data: {}".format(a_great_sentence))
    print("decoded data: {}\n".format(decoded_data))


def test_case_2():
    # Test scenario: Test when input is an empty string.
    # Expected output: None
    a_great_sentence = ""
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == None, "ERROR: For empty string as an input, expected to get None output"
    print("original data: {}".format(a_great_sentence))
    print("decoded data: {}\n".format(decoded_data))


def test_case_3():
    # Test scenario: Test when input is None.
    # Expected output: None
    a_great_sentence = None
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == None, "ERROR: For None as an input, expected to get None output"
    print("original data: {}".format(a_great_sentence))
    print("decoded data: {}\n".format(decoded_data))



if __name__ == "__main__":
    test_case_1()
    # Expected output: "Hello world"

    test_case_2()
    # Expected output: None

    test_case_3()
    # Expected output: None

    # provided_example()

