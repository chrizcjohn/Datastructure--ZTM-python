

from anytree import Node, RenderTree

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = BinaryTreeNode(data)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if current_node.data > new_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right


    def lookup(self,data):
        current_node = self.root
        while current_node is not None:
            if current_node.data is data:
                return current_node.data
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def remove(self, data):
        current_node = self.root
        while current_node is not None:
            if current_node.data is data:
                break
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        else:
            return None
        node_right  = current_node.right
        node_left = current_node.left.right

        print(node_left.data)
        # replacing_node=node_left
        # while node is not None:
        #     replacing_node = node_left.left
        # else:
        #     replacing_node = zero
        # print(replacing_node.data)


#         8
#     4       10
# 2     5    9   11
#          6           89

if __name__ == "__main__":

    def traverse(node):
        if node is None:
            return None

        tree = {"value": node.data}
        tree["left"] = traverse(node.left)
        tree["right"] = traverse(node.right)

        return tree

    tree = BinaryTree()
    tree.insert(8)
    tree.insert(4)
    tree.insert(10)
    tree.insert(5)
    tree.insert(6)
    tree.insert(11)
    tree.insert(89)
    # print(tree.lookup(8))
    # print(tree.lookup(100))
    # print(tree.lookup(89))
    tree.remove(8)


    # print(traverse(tree.root))