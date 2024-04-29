from LinkedList_With_Node_Class import  LinkedList, Node


def reverse(linked_list):
    if linked_list.length <=1:
        return linked_list
    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        linked_list.head.next = None
        linked_list.head = first
        return linked_list



if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(22)
    linked_list.append(49)
    linked_list.append(34)
    print(linked_list.print_list())
    reversed_list= reverse(linked_list)
    print(reversed_list.print_list())
