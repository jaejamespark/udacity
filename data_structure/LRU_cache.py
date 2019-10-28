class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.dic = dict()
        self.max_capacity = capacity
        self.current_capacity = 0
        self.head = Node(None, None)
        self.tail = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        if not self._exist(key):
            return -1

        node = self.dic[key]
        value = node.value

        self._remove(key, value)
        self._add(key, value)

        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.current_capacity < self.max_capacity:
            self._add(key, value)
        else:

            self._remove_head()
            self._add(key, value)

    def _remove_head(self):

        key = self.head.key
        value = self.head.value
        self._remove(key, value)

    def _remove(self, key, value):

        if not self._exist(key):
            raise KeyError("Key does not exist - Removing failed")

        # node is the head
        if self.head.key == key:
            new_head = self.head.next
            self.head = new_head
            self.head.prev = None

        # node is the tail
        elif self.tail.key == key:
            new_tail = self.tail.prev
            self.tail = new_tail
            new_tail.next = None

        # node is not the head nor the tail
        else:
            existing_node = self.dic[key]
            existing_node.prev.next = existing_node.next
            existing_node.next.prev = existing_node.prev

        # Delete node from dictionary
        del self.dic[key]

        # Test if key is removed from the dictionary
        if self._exist(key) is False:
            self.current_capacity -= 1
            return True
        else:
            raise Exception("Failed to remove key")

    def _add(self, key, value):

        if self._exist(key):
            #raise KeyError('Key already exists')
            self._remove(key, value)

        new_tail = Node(key, value)

        # first time adding
        if self.head.key is None:
            self.head = new_tail
            self.tail = new_tail
        # head already exists. append to tail
        else:
            existing_tail = self.tail
            existing_tail.next = new_tail
            new_tail.prev = existing_tail
            self.tail = new_tail

        self.dic[key] = new_tail

        if self._exist(key):
            self.current_capacity += 1
            return True
        raise Exception("Failed to add key")

    def _exist(self, key):
        if key in self.dic:
            return True
        return False

    def __str__(self):

        result = ""
        tail = self.tail

        while tail.prev is not None:
            key = tail.key
            value = tail.value
            result += (str(key) + " : " + str(value) + " -> ")
            tail = tail.prev

        key = tail.key
        value = tail.value
        result += (str(key) + " : " + str(value))

        return result


class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache)

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)       # returns -1 because 9 is not present in the cache

print(our_cache)

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(3)

print(our_cache)
