class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        item = self.stack[self.size-1]
        del self.stack[self.size-1]
        self.size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.size-1]

    def printStack(self):
        print(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    stack.printStack()
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    # print(stack.pop()) While through stack is empty error as stack is empty
    stack.printStack()