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
        if self.length == 0:
            return None
        elif self.length == 1:
            tail = self.tail
            self.head = None
            self.tail = None
            return tail
        else:
            current_node = self.head

            while current_node:
                if current_node.get_next() == self.tail:
                    self.tail = current_node
                    return self.tail

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
