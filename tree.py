class tree:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self,child):
        child.parent=self
        self.child.append(child)

    def get_level(self):
        level = 0
        itr = self.parent
        while itr:
            itr = itr.parent
            level+=1
        return level

    def print_tree(self):
        spaces=' '*self.get_level()*3
        prefix = spaces+'|__' if self.parent else ""
        print(prefix,self.data)
        if self.child:
            for child in self.child:
                child.print_tree()

if __name__ =="__main__":
    root = tree("electornics")

    laptop = tree("laptop")
    laptop.add_child(tree("mac"))
    laptop.add_child(tree("thinkpad"))
    laptop.add_child(tree("dell"))

    tv = tree("tv")
    tv.add_child(tree("mi"))
    tv.add_child(tree("lg"))
    tv.add_child(tree("samsung"))

    phone = tree("phone")
    phone.add_child(tree("vivo"))
    phone.add_child(tree("apple"))
    phone.add_child(tree("oneplus"))

    root.add_child(phone)
    root.add_child(tv)
    root.add_child(laptop)

    root.print_tree()