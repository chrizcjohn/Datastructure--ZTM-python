

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

    def remove(self, value):
        if not self.root:
            return False

        current_node = self.root
        parent_node = None

        while current_node:
            if value < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.data == value:
                # We have a match, get to work!

                # Option 1: No right child:
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    else:
                        # if parent > current value, make current left child a child of parent
                        if current_node.data < parent_node.data:
                            parent_node.left = current_node.left
                        # if parent < current value, make left child a right child of parent
                        elif current_node.data > parent_node.data:
                            parent_node.right = current_node.left

                # Option 2: Right child which doesn't have a left child
                elif current_node.right.left is None:
                    current_node.right.left = current_node.left
                    if parent_node is None:
                        self.root = current_node.right
                    else:
                        # if parent > current, make right child of the left the parent
                        if current_node.data < parent_node.data:
                            parent_node.left = current_node.right
                        # if parent < current, make right child a right child of the parent
                        elif current_node.data > parent_node.data:
                            parent_node.right = current_node.right

                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left is not None:
                        left_most_parent = left_most
                        left_most = left_most.left

                    # Parent's left subtree is now leftmost's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node is None:
                        self.root = left_most
                    else:
                        if current_node.data < parent_node.data:
                            parent_node.left = left_most
                        elif current_node.data > parent_node.data:
                            parent_node.right = left_most

                return True
        return False


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
    tree.remove(10)


    print(traverse(tree.root))