class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Returns True if Stack is empty, False otherwise"""
        if self.head:
            return False
        return True

    def push(self, item):
        """Adds an item to the top of stack"""
        new_node = Node(item)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def pop(self):
        """Removes the item from the top of stack. Returns the removed item"""
        my_node = self.head
        if self.head:
            self.head = self.head.next
        return my_node.data

    def peek(self):
        """Returns the top item in the stack, but doesn't remove it"""
        if self.head:
            return self.head.data
        return False

    def size(self):
        """Returns the (int) size of the stack"""
        current_node = self.head
        index = 0
        if current_node:
            while current_node:
                current_node = current_node.next
                index += 1
        return index

    def __str__(self):
        """Returns a string representation of all items in stack"""
        current_node = self.head
        result = ""
        while current_node:
            if result != "":
                result = result + ", "
            result = result + current_node.data 
            current_node = current_node.next
        return result


my_stack = Stack()

print('Is Stack empty?', my_stack.isEmpty())

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
my_stack.push('D')

print('Popped item:', my_stack.pop())
print('Top item:', my_stack.peek())

print('Here are all the items in the stack:', my_stack)
print('The size of my stack is:', my_stack.size())

# BONUS - Implement the Stack with a Linked List