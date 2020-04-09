
# we will be printing binary string (all the possible) of n bits(n will be passed as argument)

'''
Pranshul Rastogi (9th April, Day 2)
'''

def printBinary(n=0):
    if n==0:
        for ele in x:
            print(ele,end='')
        print()
    else:
        x[n-1]='0'
        printBinary(n-1)
        x[n-1]='1'
        printBinary(n-1)
    
if __name__ == '__main__':
    n = int(input('Enter value of n: '))
    assert n >= 0, 'oops you entered negative value of n, try again!!'
    x=['0']*n
    print("Printing all the possible binary combination of {} length\n".format(n))
    printBinary(n)

