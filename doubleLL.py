'''
implement double linked list
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class doubleLL:
    def __init__(self):
        self.head = None
    

    # insertion in double linked list
    def insert(self,data,pos=-1):
        assert pos >=-1, "make sure to give valid pos argument"
        
        # get the new node
        new_node = Node(data)

        # insertion when list is empty
        if not self.head:
            if pos > 0:
                print("list is empty, can't insert node at defined location")
            else:
                self.head = new_node
        else:
            # insertion when list is not empty
            # 1. insertion at beginning
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            # 2. insertion at middle
            elif pos > 0:
                i=0
                n=self.head
                while(i<pos and n.next ):
                    i+=1
                    n=n.next
                new_node.next = n
                new_node.prev = n.prev
                n.prev.next = new_node
                n.prev = new_node
            else:
                #3. insertion at last (default)
                n=self.head
                while(n.next):
                    n=n.next
                new_node.prev = n
                n.next = new_node
        
        
    # deletion in double linked list
    def delete(self,pos=-1):
        # by default deletes the last node
        n = self.head

        # check empty
        if not n:
            print("Can't perform delete on empty list!!")
            return False
        
        # deletion of head node
        if pos==0:
            n.next.prev = None
            self.head = n.next
            n.next = None
        
        # deletion at certain position
        elif pos > 0:
            i=0
            while ( i<=pos and n.next ):
                i+=1
                n=n.next
            if i<pos:
                print("not valid positon to delete")
                return False
            n.prev.next = n.next
            n.next.prev = n.prev
            n.next = None

        else:
            while(n.next):
                n = n.next
            n.prev.next = None
            n.prev = None

    # display 
    def printLL(self):
        n = self.head
        while(n.next):
            print(n.data,end=' <-> ')
            n = n.next
        print(n.data)


# driver 
if __name__ == '__main__':
    #insert in dll
    dll = doubleLL()
    for i in range(2,33,2):
        dll.insert(i)
    dll.printLL()

    print("inserting at 0")
    dll.insert(1,0)
    dll.printLL()

    print("inserting at 2")
    dll.insert(3,2)
    dll.printLL()

    print("inserting at last")
    dll.insert(34)
    dll.printLL()




     
        