class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, item):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while self.s2:
            self.s1.append(self.s2.pop())
        print(self.s1)

    def dequeue(self):
        if not self.is_empty():
            return self.s1.pop()
        return None

    def peek(self):
        return self.s1[-1]

    def is_empty(self):
        return self.s1 == []

    def print_queue(self):
        print(self.s1)


class Queue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if self.peek():
            return self.s2.pop()
        return None

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2[-1]
        return None

    def is_empty(self):
        return not self.s2 and  not self.s1

    def print_stacks(self):
        print(self.s1)
        print(self.s2)


if __name__ == '__main__':
    # q=Queue()
    # q.enqueue(5)
    # q.enqueue(6)
    # q.enqueue(7)
    # q.dequeue()
    # print(q.peek())
    # q.print_queue()

    #q2 is the better solution
    q2 = Queue2()
    q2.enqueue(5)
    q2.enqueue(6)
    q2.dequeue()
    q2.dequeue()
    q2.dequeue()
    # q2.dequeue()
    q2.enqueue(100)
    q2.enqueue(5000)
    print(q2.dequeue())
    q2.print_stacks()
