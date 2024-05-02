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

    def delete(self,index):
        delete_item = self.get(index)
        self.shiftitems(index)
        self.length -= 1
        return delete_item


    def shiftitems(self,index):
        for i in range(index,self.length-1):
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]




if __name__ == "__main__":
    a = array()
    a.push('hi')
    a.push('there')
    a.push('metal')
    a.push('cat')
    a.push('dog')
    print(a.get(0))
    print(a.get(1))
    print(a.pop())
    a.delete(1)
    a.push('monster')
    a.delete(2)
    a.print_data()


