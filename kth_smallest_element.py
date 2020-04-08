'''
Source: https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
Given an array arr[] and a number K where K is smaller than size of array, 
the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Expected Time Complexity: O(n)

Input:
The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. 
Each test case consists of three lines. First line of each testcase contains an integer N denoting size of the array. 
Second line contains N space separated integer denoting elements of the array. 
Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the kth smallest element in a new line.
'''

if __name__ == '__main__':
    # get the input
    t = int(input().strip())
    while(t):
        t-=1
        n = int(input().strip())
        arr = [int(x) for x in input().strip().split()]
        k = int(input().strip())
        # sort it
        arr.sort()
        print(arr[k])
