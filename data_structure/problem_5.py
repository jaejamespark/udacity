import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None
        print("New block created at {}".format(self.timestamp))

    def calc_hash(self):
        sha = hashlib.sha256()
        #hash_str = "We are going to encode this string of data!".encode('utf-8')
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.previous_hash = 0

    def insert(self, data):

        if data is None:
            raise ValueError("ERROR: Cannot add block without any data")


        if not isinstance(data, str):
            raise ValueError("Data should be string type")

        block = Block(datetime.utcnow(), data, self.previous_hash)
        if self.head is None:
            self.head = block
            self.tail = self.head
            self.previous_hash = block.hash
            block.prev = None
        else:
            self.previous_hash = block.hash
            block.prev = self.tail
            self.tail = block

    def print(self):
        if self.tail is None:
            raise ValueError("ERROR: Block is empty. Nothing to print")

        block = self.tail
        output = ""
        output += "---------------------tail-------------------------\n"
        while block is not None:
            output += "--------------------------------------------------\n"
            output += "timestamp: " + str(block.timestamp) + "\n"
            output += "data: " + block.data + "\n"
            output += "previous_hash: " + str(block.previous_hash) + "\n"
            output += "hash: " + block.hash + "\n"
            output += "--------------------------------------------------\n"
            block = block.prev
        output += "---------------------head-------------------------\n\n"
        print(output)


def test_case_1():
    print("TEST CASE 1")
    # Test scenario: Create a block chain containing two blocks which
    # contain "hello" and "world" as data in the blocks then
    # print the output to make sure the blockchain has the correct data
    # Expected output: "world" -> hello" blocks will be printed.
    blockchain = Blockchain()
    blockchain.insert('hello')
    blockchain.insert('world')
    blockchain.print()


def test_case_2():
    print("TEST CASE 2")
    # Test scenario: Try creating a blockchain with None value.
    # Expected output: ValueError will be thrown.
    blockchain = Blockchain()
    try:
        blockchain.insert(None)
    except ValueError as e:
        print("PASS: expected ValueError received: " + str(e))
    else:
        print("FAIL")


def test_case_3():
    print("TEST CASE 3")
    # Test scenario: Try creating a blockchain with integer value.
    # Expected output: ValueError will be thrown.
    blockchain = Blockchain()
    try:
        blockchain.insert(123)
    except ValueError as e:
        print("PASS: expected ValueError received: " + str(e))
    else:
        print("FAIL")

def test_case_4():
    print("TEST CASE 4")
    # Test scenario: Print empty blockchain
    # Expected output: "ERROR: Error message, Block is empty. Nothing to print"
    blockchain = Blockchain()
    try:
        blockchain.print()
    except ValueError as e:
        print("PASS: expected ValueError received: " + str(e))
    else:
        print("FAIL")


if __name__ == "__main__":
    test_case_1()
    # Test scenario: Create a block chain containing two blocks which
    # contain "hello" and "world" as data in the blocks then
    # print the output to make sure the blockchain has the correct data
    # Expected output: "world" -> hello" blocks will be printed.

    test_case_2()
    # Test scenario: Try creating a blockchain with None value.
    # Expected output: ValueError will be thrown.

    test_case_3()
    # Test scenario: Try creating a blockchain with integer value.
    # Expected output: ValueError will be thrown.

    test_case_4()
    # Test scenario: Print empty blockchain
    # Expected output: "ERROR: Error message, Block is empty. Nothing to print"