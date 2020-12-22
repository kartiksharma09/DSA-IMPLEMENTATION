class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,value):
        if self.head is None:
            element = Node(value,None)
            self.head = element
        else:
            element=Node(value,self.head)
            self.head = element

    def print_ll(self):
        if self.head is None:
            print("linked list is Empty")
            return 
        itr = self.head
        ll_str = ""
        while itr:
            if itr.next is None:
                ll_str+=str(itr.data)
            else:
                ll_str+=str(itr.data)+"-->"
            itr=itr.next
        print(ll_str)

    def get_length(self):
        count=0
        itr = self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    
    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value,None)
            return
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(value,None)
                break
            itr = itr.next

    def insert_at(self,value,index):
        if index<0 or index>=self.get_length():
            raise Exception("abey saale ! index invalid hai")
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(value,itr.next)
                break
            itr = itr.next
            count+=1

    def remove_from(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("abey saale ! index invalid hai")
        itr = self.head
        
        if index == 0:
            self.head =itr.next
        count = 0
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr = itr.next
            count+=1

    def insert_data_after(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                return
        
            itr = itr.next 
        raise Exception("bhai data hi nhi h")  

    def remove_by_value(self,data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next
            return
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
                      




    



if __name__ =="__main__":
    ll = Linkedlist()
    ll.insert_at_beginning(34)
    ll.insert_at_beginning(1)
    print(ll.get_length())
    ll.insert_at_end(10)
    ll.insert_at_beginning(12)
    ll.insert_at(100,2)
    ll.remove_from(0)
    # ll.insert_data_after(2,2)
    ll.remove_by_value(10)
    ll.print_ll()

########################################