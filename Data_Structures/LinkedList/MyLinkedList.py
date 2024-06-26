#
# linkedList_example = {
#     'head': 10,
#     'next': {
#         'head': 2,
#         'next' :{
#             'head': 50,
#             'next': None
#         }
#     }
# }



class LinkedList:
    def __init__(self,value):
        self.head = {
            'value':value,
            'next':None
        }
        self.tail = self.head
        self.length = 1

    def append(self,data):
        new_node = {
            'value':data,
            'next':None
        }
        self.tail['next']= new_node
        self.tail = new_node
        self.length += 1

    def prepend(self,data):
        new_node = {
            'value':data,
            'next':None
        }
        new_node['next'] = self.head
        self.head= new_node
        self.length += 1



if __name__ == '__main__':
    my_linkedlist = LinkedList(10)
    my_linkedlist.prepend(60)
    my_linkedlist.append(20)
    my_linkedlist.prepend(100)
    # print(my_linkedlist.length)
    print(my_linkedlist.head)

