class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        item = self.stack[len(self.stack)-1]
        del self.stack[len(self.stack)-1]
        return item

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[len(self.stack)-1]

    def printStack(self):
        print(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push('google')
    stack.push('udemy')
    stack.push('ZTM')
    stack.push('stack')
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
    stack.push('ZTM')
    stack.printStack()