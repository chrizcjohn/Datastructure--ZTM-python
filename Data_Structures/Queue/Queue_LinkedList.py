class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last =self.first
            self.size = 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.size += 1
        return new_node.data

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            value = self.first.data
            self.first = self.first.next
            self.size -= 1
            if self.size == 0:
                self.last = None
            return value

    def peek(self):
        if self.is_empty():
            return None
        return self.first.data

    def print_queue(self):
        if self.is_empty():
            print('Queue is empty')
        printer_node = self.first
        for i in range(self.size):
            print(printer_node.data,end=" ")
            printer_node = printer_node.next
        print()
    def is_empty(self):
        return self.size == 0




if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('google')
    queue.print_queue()
    queue.enqueue('udemy')
    queue.enqueue('ZTM')
    queue.print_queue()
    print(queue.peek())
    print(queue.dequeue())
    queue.print_queue()
    print(queue.dequeue())
    queue.print_queue()
    print(queue.dequeue())
    queue.print_queue()





