#################### HASH TABLE IMPLEMENTAION(without collision handling)##########
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr =[None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h]==val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h]==None

####################################################################
########## COLLISION HANDLING IN HASH TABLE ########################

class HashTableNew:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.h):
            if kv[0] == key:
                print("del",index)
                del self.arr[h][index]

    def Print_all(self):
        print(self.arr)

a  = HashTableNew()
a.__setitem__('march 6',1)
a.__setitem__('march 17',2)
a.Print_all()

######################################################################