class array:
    def __init__(self):
            self.length = 0
            self.data ={}
    def get(self,index):
        return None if len(self.data)<=index else self.data[index]

    def push(self,value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    def print_data(self):
        # print(str(self.__dict__))
        print(self.data)




if __name__ == "__main__":
    a = array()
    a.push('hi')
    a.push('there')
    print(a.get(0))
    print(a.get(1))
    print(a.pop())
    a.print_data()

