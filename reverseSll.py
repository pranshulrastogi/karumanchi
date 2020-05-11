'''
reverses single linked list
input: single linked list
output: reversed single linked list
'''
import singleLL

def reverseSll(ll_head):
    if not ll_head:
        return False
    if not ll_head.next:
        return ll_head
    else:
        second = ll_head.next
        ll_head.next = None
        reversedLL = reverseSll(second)
        second.next = ll_head
        return reversedLL

if __name__ == "__main__":
    sll = singleLL.singleLL()
    for i in range(4):
        sll.insert(i)
    sll.printLL()
    print(sll.head.data)
    print("Reversing single LL")
    n=sll.head
    rsll = reverseSll(sll.head)
    sll.head = rsll
    sll.printLL()
    
