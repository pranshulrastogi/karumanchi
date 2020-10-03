# reverse a single linked list 

import singleLL 

def reverse(sl):
    if sl.head.next == None:
        return sl
    p = sl.head
    q = p.next
    p.next = None
    sl.head = q
    nl = reverse(sl)
    q.next = p
    return nl
    

if __name__ == "__main__":
    
    # make single linked list
    sl = singleLL.singleLL()
    for i in range(10):
        sl.insert(i+1)

    sl.printLL()
    print("reversing the list")
    rsl = reverse(sl)
    rsl.printLL()