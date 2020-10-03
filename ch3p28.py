# Problem: Display linked list from the last

import singleLL

def reversep(sll):
    if sll.head.next == None:
        # last node
        print(sll.head.data)
    else:
        p = sll.head
        sll.head = sll.head.next
        reversep(sll)
        print(p.data)

if __name__ == "__main__":
    
    # create a single linked list
    sll = singleLL.singleLL()
    for i in range(10):
        sll.insert(i+1)

    sll.printLL()

    print("reverse print")
    reversep(sll)