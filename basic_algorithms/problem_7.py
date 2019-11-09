# A RouteTrieNode
class RouteTrieNode:
    # Initialize the node with children and a handler
    def __init__(self, handler):
        self.children = {}
        self.handler = handler

    # Insert the node
    def insert(self, path, handler):
        self.children[path] = RouteTrieNode(handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    def __init__(self, root_handler, not_found_handler):
        self.not_found_handler = not_found_handler
        self.root_handler = root_handler
        self.root = RouteTrieNode(not_found_handler)

        # assign the handler to only the leaf (deepest) node of this path

    def insert(self, paths, handler):
        node = self.root
        total_path = len(paths)
        for i in range(total_path):
            path = paths[i]

            # Check the path
            # if path starts with '/', give the root_handler
            # if not start with '/', print an error
            if i == 0:
                if path == '/':
                    set_handler = self.root_handler
                else:
                    print("ERROR: Path should start with '/'")
                    return
            # if this is the last path, pass the user handler
            elif i == (total_path - 1):
                set_handler = handler
            # otherwise, pass the handler as default
            else:
                set_handler = self.not_found_handler

            if not path in node.children:
                node.insert(path, set_handler)

            node = node.children[path]

    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or "not found handler" for no match
    def find(self, paths):

        node = self.root
        total_path = len(paths)
        for i in range(total_path):
            path = paths[i]

            if not path in node.children:
                return self.not_found_handler

            node = node.children[path]

        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    # Create a new RouteTrie and set the root hander
    # And set default handler as 404 page not found responses
    def __init__(self, root_handler, not_found_handler):
        self.router = RouteTrie(root_handler, not_found_handler)

    # Add a handler for a path
    def add_handler(self, path, handler):
        # Passed the path after split and handler for inserting
        paths = self.split_path(path)
        self.router.insert(paths, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(path)
        return self.router.find(paths)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions.
        if len(path) <= 0:
            return path
        if len(path) == 1:
            if path[0] == "/":
                return path
            else:
                return ''

        paths = []
        # add a root
        if path[0] == "/":
            paths.append(path[0])
            path = path[1:]
        # trailing last slash
        if path[-1] == "/":
            path = path[:-1]
        # split by slash and add with the root
        paths += path.split('/')
        return paths

# create the router and add a route
router = Router("root handler",
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one


# create the router and add a route
router = Router("root handler",
                "not found handler")

# testcase 1
print("Test case 1")
print(router.lookup(""))  # should print 'not found handler'

# testcase 2
print("Test case 2")
print(router.lookup("/"))  # should print 'not found handler' or None if you did not implement one

# testcase 3
print("Test case 3")
router.add_handler("/home/about", "about handler")  # add a route
print(router.lookup("\home/about"))  # should print 'not found handler' or None if you did not implement one

# testcase 4
print("Test case 4")
router.add_handler("\root\bin", "about handler")  # add a route wiht back slash, should print ""ERROR: Path should start with '/'"
print(router.lookup("/root/"))  # should print 'not found handler' or None if you did not implement one