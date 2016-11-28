class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current != None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""

        if self.is_empty():
            return 0

        count = 1
        current_node = self.head
        while current_node.next != None:
            count += 1
            current_node = current_node.next
            # print('loop two')
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail.prev = new_node
            self.tail = new_node



    def prepend(self, item):
        """Insert the given item at the head of this linked list"""

        if self.head == None:
            new_node =  Node(item)
            self.head = new_node
            self.tail = new_node

        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        if self.is_empty():
            raise valueError

        if self.head.data == item and self.length() == 1:
            self.head = None
            self.tail = None

        while current_node is not None:

            if current_node.data == item:
                #its somewhere in the middle
                if previous_node is not None:
                    previous_node.next = current_node.next
                    current_node.next.prev = None
                    current_node.next = None
                    current_node.prev = None
                #its the tail
                elif current_node.next is None:
                    previous_node.next = None
                    current_node.prev = None
                    self.tail = previous_node
                #its the head
                else:
                    self.head = current_node.next
                    current_node.next.prev = None
                    current_node.next = None
                previous_node = current_node
                current_node = current_node.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True

        current_node = self.head
        while current_node.next != None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next
        return None

    def __iter__(self):
        current = self.head
            while current is not None:
                yield current
                current = current.next
