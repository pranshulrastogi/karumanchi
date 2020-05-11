from singleLL import singleLL

class StackLL:
    '''
    stack implemented from Linked list
    Major operation: push, pop
    '''
    def __init__(self):
        self.my_stack = singleLL()
    
    def push(self,element):
        self.my_stack.insert(element)

    def pop(self):
        n = self.my_stack.head
        while n.next:
            n=n.next
        print(n.data)
        self.my_stack.delete()    
    def display(self):
        self.my_stack.printLL()

if __name__ == '__main__':

    my_stack = StackLL()
    # insert in stack
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.display()
    my_stack.pop()
    my_stack.display()
