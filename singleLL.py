'''
defines singly linked list
'''
class Node :
    '''
    defines a single linked list's node
    '''
    def __init__(self,data=0):
        self.data=data #assign data
        self.next=None
    
    


class singleLL:

    # initialize the single linked list with 0 node
    def __init__( self, head=None ):
        self.head = head
        
    
    def insert( self, data, pos=-1 ):
        # create a new node
        new_node = Node(data)

        if not self.head:
            # first node creation
            self.head = new_node
            return self.head
        elif pos == 0:
            # insertion at beginning
            new_node.next = self.head
            self.head = new_node
        
        # if position is not defined, by default insert at last
        elif pos == -1:
            # last node insertion
            n = self.head
            while (n.next):
                n = n.next
            n.next = new_node
            new_node.next = None
        else:
            assert pos >= 0, "Enter position to insert element more than or equal to 0"
            # traverse to pos
            i=0
            n = self.head
            while ( i < pos-1 ):
                i+=1
                n = n.next    
            # now insert the node 
            new_node.next = n.next
            n.next = new_node
            return self.head

    def printLL (self):
        
        n = self.head
        while (n.next):
            print("{}".format(n.data), end=' -> ')
            n = n.next

        print("{}\n".format(n.data))
    
    def delete(self,pos=-1):
        '''
        by default deletes the last element in the list
        '''
        if not self.head:
            print("Empty list!!")
            return False
        # if delete the head node
        if pos==0:
            self.head = self.head.next
            return self.head
        elif pos == -1 :
            # delete last element
            n = self.head
            while(n.next.next):
                n=n.next
            n.next = None
            return True
        
        else:
            n = self.head
            i = 0
            while (i < pos-1):
                n=n.next
                i+=1
            tmp = n.next
            n.next = n.next.next
            tmp.next = None
            return True


        
    
if __name__ == "__main__":
    # create empty single linked list
    sll = singleLL()
    
    # insert elements
    for i in range(2,33,2):
        sll.insert(i)
    
    # display all 
    sll.printLL()
    
    # insertion check
    print( "inserting 1 in the starting")
    sll.insert(1,0)
    sll.printLL()

    print( "inserting 3 at postion 2nd( 0 based indexing )")
    sll.insert(3,2)
    sll.printLL()

    print( "deleting head node")
    sll.delete(0)
    sll.printLL()

    print( "deleting last node")
    sll.delete()
    sll.printLL()

    print( "deleting 1st node")
    sll.delete(1)
    sll.printLL()
