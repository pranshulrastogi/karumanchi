'''
source: https://practice.geeksforgeeks.org/problems/find-transition-point/1
You are given a sorted array containing only numbers 0 and 1. 
Find the transition point efficiently. Transition point is a point where "0" ends and "1" begins.

Input:

You have to complete the method which takes 2 argument: the array arr[] and size of array N. You should not read any input from stdin/console. There are multiple test cases. For each test cases, this method will be called individually.

Output:

Your function should return transition point.

'''

def transition_point(arr,n):
    i=0
    j=n-1
    while(i<j):
        mid = (i+j)//2
        if arr[mid]==0:
            if arr[mid+1]==1:
                return mid+1
            i=mid+1
        elif arr[mid]==1:
            if arr[mid-1]==0:
                return mid-1
            j=mid-1
        