class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length+=1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        temp_array= []
        temp = self.head
        if temp == None:
            print("List is empty")
        else:
            while temp != None:
                temp_array.append(temp.data)
                temp = temp.next
        return temp_array


    def insert(self, data, index):
        new_node = Node(data)
        pre_node = self.head

        if pre_node is None:
            self.append(data)
        elif index == 0:
            self.prepend(data)
        else:
            for i in range(index - 1):
                if pre_node is None:
                    raise IndexError("Index out of range")
                pre_node = pre_node.next

            after_nodes = pre_node.next
            pre_node.next = new_node
            new_node.next = after_nodes
            self.length += 1


    def remove(self, index):

        if self.head == None:
            print("List is empty")
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            node = self.head
            for i in range(index-1):
                if node.next is None:
                    print("Index out of range")
                    break
                node = node.next
            if node.next is None:
                print("Index out of range")
            else:
                node.next = node.next.next
                self.length -=1



if __name__ == '__main__':
    my_linkedlist = LinkedList()
    # my_linkedlist.prepend(60)
    my_linkedlist.append(20)
    my_linkedlist.append(30)
    my_linkedlist.prepend(100)
    my_linkedlist.append(41)
    my_linkedlist.append(74)
    print(my_linkedlist.print_list())

    my_linkedlist.insert(99, 0)
    my_linkedlist.insert(85,2)
    print(my_linkedlist.print_list())
    my_linkedlist.remove(3)

    print(my_linkedlist.print_list())
    my_linkedlist.remove(0)
    print(my_linkedlist.print_list())
    my_linkedlist.remove(4)
    print(my_linkedlist.print_list())
    my_linkedlist.remove(5)
    print(my_linkedlist.print_list())
    my_linkedlist.remove(1)
    print(my_linkedlist.print_list())