from node import Node
class BST:
    def __init__(self):
        self.head: Node | None = None

def insert(bst: BST, value: int) -> Node:
    new_node = Node(value)
    if bst.head is None:
        bst.head = new_node
    else:
        current = bst.head
        prev: Node | None = None
        while current != None:
            prev = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        if prev and value < prev.value:
            prev.left = new_node
        elif prev:
            prev.right = new_node
    return new_node

def delete(bst: BST, value: int):
    pass

def update(bst: BST, value: int, replace_value: int):
    pass

def inorder(current: Node | None):
    if current is None:
        return
    inorder(current.left)
    print(current.value)
    inorder(current.right)
    
def preorder(current: Node | None):
    if current is None:
        return
    print(current.value)
    inorder(current.left)
    inorder(current.right)

def postorder(current: Node | None):
    if current is None:
        return
    inorder(current.left)
    inorder(current.right)
    print(current.value)

bst = BST()



