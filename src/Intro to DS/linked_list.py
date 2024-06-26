class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    # data = None
    # next_node = None

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "Node data: %s" % self.data

class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time.
        :return:
        """
        current = self.head
        count = 0

        while current != None: # Can also do while current
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new Node data at the head of the list.
        Takes O(1) time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Return the node or 'None' if not found

        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node

        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position.
        Insertion takes O(1) time but finding the node at the
        insertion point takes O(n).

        Takes overall O(n).
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Return the node or None if key doesn't exist
        Takes O(n) time.
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def remove_by_index(self, index):
        """
        Removes node by index. Takes O(n) time.
        Returns none if it doesn't exist.
        """
        prev_node = None
        current_node = self.head
        if index == 0:
            self.head = current_node.next_node
        else:
            for i in range(index):
                prev_node = current_node
                current_node = current_node.next_node
            try:
                prev_node.next_node = current_node.next_node
            except:
                # current_node = None
                return "Invalid index"

        return current_node

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """
        # return "There are %d Nodes" % self.size() # My implementation.
        nodes = []
        current = self.head

        while current: # or again current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)