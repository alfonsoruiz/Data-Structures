class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
        else:
            self.tail.set_next(new_node)

        self.tail = new_node
        self.length += 1

    def remove_tail(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return node.get_value()
        else:
            current_node = self.head

            while current_node:
                if current_node.get_next() is self.tail:
                    self.tail = current_node
                    self.length -= 1
                    return current_node.next_node.value

                current_node = current_node.get_next()

    def contains(self, value):
        if self.length == 0:
            return False
        else:
            current_node = self.head

            while current_node:
                if current_node.value == value:
                    return True

                current_node = current_node.next_node

            return False

    def remove_head(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            head_node_value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return head_node_value
        else:
            head_node_value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return head_node_value

    def get_max(self):
        if self.length == 0:
            return None

        current_node = self.head
        max_value = self.head.value

        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value

            current_node = current_node.next_node

        return max_value


"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        self.size -= 1
        return self.storage.remove_head()
