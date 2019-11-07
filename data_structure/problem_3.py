import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        #self.code = None

def huffman_encoding(data):
    # count the # of character
    dic = {}
    for c in data:
        dic[c] = dic.get(c, 0) + 1

    # for sorting a tuple which has # of character and Node which has key as value
    letters = []
    for k, v in dic.items():
        letters.append((v, Node(k)))

    root = None
    if len(letters) <= 0:
        return
    elif len(letters) == 1:
        # Tohandle,whenremainis1orless
        root = letters[0][1]
    else:
        while len(letters) > 1:
            letters = sorted(letters, key=lambda items:items[0])
            # joint two node
            l = letters.pop(0)
            r = letters.pop(0)
            v = l[0] + r[0]
            root = Node(v)
            root.left = l[1]
            root.right = r[1]
            letters.append((v, root))

        root = letters[0][1]
        dec_dict = {}
        dec_dict['tmp'] = ''

    generateCode(root, dec_dict)

    decoded_data = ''
    for c in data:
        decoded_data += dec_dict[c]

    return decoded_data, root

def generateCode(root, dec_dict):
    if root:
        # if this is leaf add the code in the dictionary
        if root.left == None:
            if root.right == None:
                dec_dict[root.value] = dec_dict['tmp']
                return dec_dict

        if root.left:
            dec_dict['tmp'] += '0'
            generateCode(root.left, dec_dict)

        dec_dict['tmp'] = dec_dict['tmp'][:len(dec_dict['tmp']) - 1]

        if root.right:
            dec_dict['tmp'] += '1'
            generateCode(root.right, dec_dict)

        dec_dict['tmp'] = dec_dict['tmp'][:len(dec_dict['tmp']) - 1]

    # print(dec_dict)
    return dec_dict


def huffman_decoding(data,tree):
    node = tree
    result = ''
    for b in data:

        if b == '0':
            # if node.left:
            node = node.left

        if b == '1':
            # if node.right:
            node = node.right

        if not node.left:
            if not node.right:
                result += node.value
                node = tree

    print(result)
    return result


if __name__ == "__main__":
    codes = {}

    # a_great_sentence = "The bird is the word"
    a_great_sentence = "hello"


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))