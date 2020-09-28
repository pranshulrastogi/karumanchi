# implement stack using linked list
# basically implement push and pop operation

# push is inserting at end, pop is deletion from the end

class Node:
    def __init__(self):
        self.data = None
        self.next = None

class stackll:
    def __init__(self):
        
        self.head = None

    def isEmpty(self):
        return True if self.head == None else False

    def push(self, data):
        # insertion at end
        node = Node()
        node.data = data
    
        if self.isEmpty():
            # 1st element
            self.head = node

        else:
            # insertion at last
            last = self.head
            while last.next:
                last = last.next
            last.next = node

    def pop(self):
        # pop the last element
        if self.isEmpty():
            print("Stack empty")
            return False
        last = self.head
        slast = self.head

        if last.next == None:
            print(last.data)
            result = last.data
            print("Woo")
            last.data = None
            self.head = None
            return result
        else:
            while last.next:
                slast = last
                last = last.next

        # delete last after printing/returning data
        result = last.data
        slast.next = None
        print(result)
        return result
    
    

if __name__ == "__main__":
    print("pushing in stack")
    stack = stackll()
    for i in range(5):
        stack.push(i+1)
        print("pushed {}".format(i+1))
    
    print("popping")
    for i in range(7):
        stack.pop()
