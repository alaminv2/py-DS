from collections import deque


class TreeNode:
    def __init__(self, name=None, designation=None, parent=None):
        self.name = name
        self.designation = designation
        self.parent = parent
        self.children = []

    def add_child(self, name=None, designation=None, parent=None):
        child = TreeNode(name, designation, self)
        self.children.append(child)
        return child

    def print_tree(self, level=0):
        lvl = self.get_level()
        if lvl <= level:
            prefix = ' ' * lvl * 2
            prefix += '|__' if self.parent else ''
            print(f'{prefix}{self.name} ({self.designation})')
            if self.children:
                for child in self.children:
                    child.print_tree(level)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def __str__(self):
        return f'{self.name}, {self.designation}'


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        pass

    def level_order_print(self):
        # Method using queue
        queue = deque()
        result = list()
        queue.append(self)
        print(queue)
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            result.append(cur.data)
        return result

# Level order tree traversal
    def get_tree_height(self):
        l_height = 0 if not self.left else self.left.get_tree_height()
        r_height = 0 if not self.right else self.right.get_tree_height()

        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1

    def get_current_level(self, level):
        pass

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    parent = BinaryTree(20)
    parent.left = BinaryTree(15)
    parent.right = BinaryTree(22)
    parent.left.left = BinaryTree(10)
    parent.right.left = BinaryTree(16)
    parent.right.right = BinaryTree(19)
    # parent.add_child(30)
    # parent.add_child(12)
    # parent.add_child(13)
    # parent.add_child(5)
    # parent.add_child(21)
    # parent.add_child(25)
    # parent.add_child(23)
    # parent.add_child(24)

    print('height = ', parent.get_tree_height())
    res = parent.level_order_print()
    print(res)