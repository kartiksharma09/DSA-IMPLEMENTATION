 class Bst:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Bst(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Bst(data)

    def search(self,value):
        if value == self.data:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def inorder_traversal(self):
        iolist = []
        if self.left:
            iolist+=self.left.inorder_traversal()

        iolist.append(self.data)

        if self.right:
            iolist+=self.right.inorder_traversal()

        return iolist


    def calculate_sum(self):
        sum = 0
        sum+=self.data

        if self.left:
            sum+=self.left.calculate_sum()
        
        if self.right:
            sum+=self.right.calculate_sum()

        return sum

    def find_min(self):
        if self.left:
            return self.left.find_min()

        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()

        return self.data

    def delete(self,value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


if __name__=="__main__":
    a = Bst(10)
    a.add_child(12)
    a.add_child(8)
    a.add_child(65)
    print(a.search(8))
    print(a.calculate_sum())
    print(a.inorder_traversal())
    print(a.find_min())
    print(a.find_max())
    a.delete(12)
    print(a.inorder_traversal())