class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Returns True if Queue is empty, False otherwise"""
        if self.head:
            return False
        return True

    def enqueue(self, item):
        """Adds an item to the back of queue"""
        if self.head:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            new_node = Node(item)
            current_node.next = new_node
        else:
            new_node = Node(item)
            self.head = new_node


    def dequeue(self):
        """Removes the item from the front of queue. Returns the removed item"""
        if self.head:
            popped = self.head
            self.head = self.head.next
            return popped.data
        return False

    def peek(self):
        """Returns the first item in the queue, but doesn't remove it"""
        if self.head:
            return self.head.data
        return None

    def size(self):
        """Returns the (int) size of the queue"""
        current_node = self.head
        index = 0
        while current_node:
            current_node = current_node.next
            index += 1
        return index

    def __str__(self):
        """Returns a string representation of all items in queue"""
        current_node = self.head
        result = ""
        while current_node:
            if result != "":
                result = result + ", "
            result = result + current_node.data 
            current_node = current_node.next
        return result


my_queue = Queue()

print('Is Queue empty?', my_queue.isEmpty())
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
my_queue.enqueue('D')
print("queue state:", my_queue)

print('Dequeued item:', my_queue.dequeue())
print('First item:', my_queue.peek())

print('Here are all the items in the queue:', my_queue)
print('The size of my stack is:', my_queue.size())

# BONUS - Implement the Queue with a Linked List
