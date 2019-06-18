# Sortings

def bubble_sort(array):
    for i in range(0,len(array)):
        for j in range (0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

# Basic operations

def maxarray(array):
    maxx=array[0]
    for i in range(1,len(array)):
        if(array[i]>maxx):
            maxx=array[i]
    return maxx

def minarray(array):
    minn=array[0]
    for i in range(1,len(array)):
        if(array[i]<minn):
            minn=array[i]
    return minn

def remall(array,k):
    s=[]
    for i in array:
        if i!=k:
            s.append(i)
    return s

def max_index(array):
    index=0
    maxx=array[0]
    for i in range(0,len(array)):
        if array[i]>maxx:
            maxx=array[i]
            index=i
    return index

def min_index(array):
    index=0
    minn=array[0]
    for i in range(0,len(array)):
        if array[i]<minn:
            minn=array[i]
            index=i
    return index