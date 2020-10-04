# Problem: JosephusCircle, get the leader among person arranged in circular way, by removing every Mth person

import singleLL

def getLeader(sll, m):
    p = sll.head
    q = sll.head
    i=0
    count = 1
    p = p.next
    while p!=q:
        count+=1
        p = p.next
    p = sll.head
    print(count)
    while count > 0:
        if i==m:
            # delete p
            temp = p.next
            p.next = None
            q.next = temp
            p = temp
        else:
            q = p
            p = p.next
        count -= 1
        i+=1
    return p.data



if __name__ == "__main__":
    
    sll = singleLL.singleLL()

    # initialize it and make it circular
    for i in range(10):
        sll.insert(i+1)
    
    # make sll as circular
    p = sll.head
    q = sll.head
    while(q.next):
        q = q.next
    q.next = p

    i=0
    q = sll.head
    while i<11:
        print(q.data, end="->")
        q=q.next
        i+=1
    m = int(input("Enter value of M: "))
    leader = getLeader(sll, m) 
    print("leader is {}".format(leader))       