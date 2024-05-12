

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
        if current_node.data is None:
            return None
        if current_node.data == data:
            return True


#         8
#     4       10
# 2     5    9   11







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
    tree.insert(6)
    tree.insert(11)
    # print(tree.lookup(8))
    tree_dict = traverse(tree.root)

    print(traverse(tree.root))