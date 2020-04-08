# tower of hanoi problem implementation
# for problem statement search it

def toh(n,frm, to, aux):
    '''
    toh == tower of hanoi, n= number of disks (numbered 1,2,...n),
    'frm' is source disk, 'to' is destination disk and 'aux' is auxillary disk
    '''
    # if only 1 disk, transfer to destination
    if n==1:
        print("Move disk {} from {} to {}\n".format(n,frm,to))
    else:
        # move n-1 disks from source to auxillary using destination
        toh(n-1,frm, aux, to)
        # move last disk from source to destination
        print("Move disk {} from {} to {}\n".format(n,frm, to))
        # move n-1 disks back from auxillary to destination using source
        toh(n-1, aux, to, frm)


if __name__ == '__main__':
    n = int(input("enter number of disks "))
    print("We are using A, B and C tower, where A initially contains all the disks\n and need to be transferred to C\n")
    toh(n, 'A', 'C', 'B')
    print("Completed..")