class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None




class DoctorTree:
    def __init__(self):
        self.root = None

    
    def insert(self, parent_name: str, employee_name: str, side: str) -> bool:
        parent = self.find_doctor(self.root, parent_name)

        if parent is None:
            return False

        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(employee_name)
                return True

        elif side == "right":
            if parent.right is None:
                parent.right = DoctorNode(employee_name)
                return True

        return False

    def find_doctor(self, node, name):
        if node is None:
            return None

        if node.name == name:
            return node

        left_result = self.find_doctor(node.left, name)

        if left_result is not None:
            return left_result

        return self.find_doctor(node.right, name)
    
    # Preorder: Root -> Left -> Right
    def preorder(self, node):
        if node is None:
            return []

        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)

        return result

    # Inorder: Left -> Root -> Right
    def inorder(self, node):
        if node is None:
            return []

        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)

        return result

    # Postorder: Left -> Right -> Root
    def postorder(self, node):
        if node is None:
            return []

        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)

        return result

    




# Test your DoctorTree and DoctorNode classes here


tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print("Root Doctor:", tree.root.name)
print("Left Doctor:", tree.root.left.name)
print("Right Doctor:", tree.root.right.name)
print("Dr. Phan's Left:", tree.root.left.left.name)
print("Dr. Phan's Right:", tree.root.left.right.name)

print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))


# Test edge cases for insert()

# Parent doctor does not exist
print(tree.insert("Dr. Unknown", "Dr. Taylor", "left"))

# Invalid side
print(tree.insert("Dr. Croft", "Dr. Taylor", "middle"))

# Position is already occupied
print(tree.insert("Dr. Croft", "Dr. Taylor", "left"))

print(tree.preorder(tree.root))