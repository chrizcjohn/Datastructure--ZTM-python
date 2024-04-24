
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1


    def print_list(self):
        temp = self.head
        if temp == None:
            print("List is empty")
        else:
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next



if __name__ == '__main__':
    my_linkedlist = LinkedList()
    # my_linkedlist.prepend(60)
    my_linkedlist.append(20)
    my_linkedlist.append(30)
    my_linkedlist.prepend(100)
    # # print(my_linkedlist.length)
    my_linkedlist.print_list()

