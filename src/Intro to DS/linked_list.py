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