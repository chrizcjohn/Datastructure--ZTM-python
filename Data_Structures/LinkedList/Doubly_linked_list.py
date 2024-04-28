class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.append(data)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def insert(self, data, index):
        node = self.head
        if index == 0:
            self.prepend(data)
        else:
            new_node = Node(data)
            for i in range(index-1):
                if node is None:
                    print("Index out of range")
                node = node.next

            after_nodes = node.next
            node.next = new_node
            new_node.prev = node
            new_node.next = after_nodes
            if after_nodes:
                after_nodes.prev = new_node
            self.length += 1

    def remove(self, index):
        if index == 0:
            if self.head is None:
                print("List is empty")
                return
            self.head = self.head.next
            if self.head is None:
                self.tail = None  # Update tail when removing the last node
            else:
                self.head.prev = None
            self.length -= 1
        else:
            node = self.head
            for i in range(index - 1):
                if node is None or node.next is None:
                    print("Index out of range")
                    return
                node = node.next

            if node.next is None:
                print("Index out of range")
                return

            node.next = node.next.next
            if node.next is None:
                self.tail = node  # Update tail when removing the last node
            else:
                node.next.prev = node  # Update prev pointer of the next node
            self.length -= 1

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

    def print_list_reverse(self):
        temp_array= []
        temp = self.tail
        if temp == None:
            print("List is empty")
        else:
            while temp != None:
                temp_array.append(temp.data)
                # print(vars(temp),end=" ")
                temp = temp.prev
        return temp_array


if __name__ == "__main__":
    my_list = DoublyLinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.prepend(3)
    my_list.insert(4, 1)
    my_list.remove(2)
    my_list.remove(3)

    my_list.remove(2)
    print(my_list.print_list())
    print(my_list.print_list_reverse())

