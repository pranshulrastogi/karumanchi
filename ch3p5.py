# "Find nth node from the end of linked list"
# solution performs only one scan, 
# T.C: O(m), m is the length of the list > n

import singleLL

if __name__ == "__main__":
    # initialize single ll
    sll = singleLL.singleLL()

    # insert 20 items 
    for i in range(20):
        sll.insert(i+1, pos=i)

    sll.printLL()

    query_index = int(input("Which node you want to retrieve from last: "))
    assert query_index <= 20, "Index out of range"

    p = sll.head
    q = sll.head
    # p will move forward 'query_index' times, once it reaches that , q will start moving
    i = 0
    while p and i!= query_index:
        p = p.next
        i+= 1
    while p:
        p = p.next
        q = q.next
    print(q.data)
