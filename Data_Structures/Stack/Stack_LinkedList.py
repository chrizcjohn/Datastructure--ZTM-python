class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self,value):
        node = Node(value)
        if self.top is None:
            self.top = node
            self.bottom = node
            self.length += 1
        else:
            node.next = self.top
            self.top = node
            self.length += 1

    def printStack(self):
        temp = self.top
        list_format = []
        for i in range(self.length):
            list_format.append(temp.data)
            temp = temp.next
        print(list_format)




    def pop(self):
        if self.top is None:
            return None
        else:
            prev = self.top.data
            self.top = self.top.next
            self.length -= 1
            return prev

    def peek(self):
        if not self.empty():
            return self.top.data
        else:
            return None


    def empty(self):
        if self.top is None:
            return True
        else:
            return False


if __name__ == '__main__':
    stack = Stack()
    stack.push("google")
    stack.push("udemy")
    stack.push("discord")
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    stack.push("python")
    stack.printStack()


