import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

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
        block = self.tail
        while block.prev is not None:
            print(block.data)
            block = block.prev
        print(block.data)



def test_case_1():
    # Test scenario: Create a block chain
    # containing two blocks which contain "hello" and "world"
    # in blocks then print the output to make sure the
    # blockchain has the correct data
    # Expected output: "world \n hello" will be printed.
    blockchain = Blockchain()
    blockchain.insert('hello')
    blockchain.insert('world')
    blockchain.print()


def test_case_2():
    # Test scenario: Try creating a blockchain with None value.
    # Expected output: ValueError will be thrown.
    blockchain = Blockchain()
    try:
        blockchain.insert(None)
    except ValueError as e:
        print("ValueError: " + str(e))


def test_case_3():
    # Test scenario: Try creating a blockchain with integer value.
    # Expected output: ValueError will be thrown.
    blockchain = Blockchain()
    try:
        blockchain.insert(123)
    except ValueError as e:
        print("ValueError: " + str(e))


if __name__ == "__main__":
    test_case_1()
    # Output is "world \n hello"

    test_case_2()
    # "Data should be string type" error should occur

    test_case_3()
    # "Data should be string type" error should occur