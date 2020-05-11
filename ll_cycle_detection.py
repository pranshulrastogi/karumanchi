'''
cycle detection in linked list
Usage Floyd cycle detection algorithm
'''
import singleLL

def findStartofLoop(sll, slow, fast):
    '''
    if there is a loop/cycle in linked list,
    find the starting point of that cycle
    '''
    # initialize slow to head
    slow = sll.head
    print(slow.data)
    print(fast.data)
    # now lets move slow and fast pointer at same pace
    # wherever they will meet will be the starting point
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow

def detectCycle(sll):

    slow = sll.head
    fast = sll.head
    print("Detecting cycle")
    while slow and fast:
        fast = fast.next
        if slow == fast:

            # find the start of the loop
            start = findStartofLoop(sll,slow,fast)
            print("Yes, cycle detected, start point {}".format(start.data))
            break
        
        elif fast == None:
            print("No Cycle")
            break
        
        fast = fast.next
        if fast == slow:
            # find the start of the loop
            start = findStartofLoop(sll,slow,fast)
            print("Yes, cycle detected, start point {}".format(start.data))
            break
        elif fast == None:
            print("No Cycle")
            break
        slow = slow.next

if __name__ == "__main__":

    # create linked list with cycle
    cycle_ll = singleLL.singleLL()
    # insert 1,2,3,4,5,6, also 6's next points to 3
    for i in range(1,7):
        cycle_ll.insert(i)
    n = cycle_ll.head

    cycle_ll.printLL()

    detectCycle(cycle_ll)

    while n.next:
        if n.data == 3:
            n3 = n
        n = n.next
    n.next = n3
    #cycle_ll.printLL()
    print("cycle created lets see")

    detectCycle(cycle_ll)