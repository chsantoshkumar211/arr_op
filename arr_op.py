# Sortings

def bubble_sort(array):
    for i in range(0,len(array)):
        for j in range (0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index=j
        temp=array[min_index]
        array[min_index]=array[i]
        array[i]=temp
    return array

def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array

def quick_sort(arr):
    def quick(arr,l,r):
        if(l<r):
            pivot=median(arr,l,r)
            i=l
            j=r-2
            while(True):
                while(arr[i]<pivot):
                    i+=1
                while(arr[j]>pivot):
                    j-=1
                if(i<j):
                    t=arr[i]
                    arr[i]=arr[j]
                    arr[j]=t
                else:
                    break
            t=arr[i]
            arr[i]=arr[r-1]
            arr[r-1]=t
            quick(arr,l,i-1)
            quick(arr,i+1,r)

    def median(arr,l,r):
        mid=(l+r)//2
        if(arr[l]>arr[mid]):
            t=arr[l]
            arr[l]=arr[mid]
            arr[mid]=t
        if(arr[l]>arr[r]):
            t=arr[l]
            arr[l]=arr[r]
            arr[r]=t
        if(arr[mid]>arr[r]):
            t=arr[mid]
            arr[mid]=arr[r]
            arr[r]=t
        t=arr[mid]
        arr[mid]=arr[r-1]
        arr[r-1]=t
        return arr[r-1]

    l=0
    r=len(arr)-1
    quick(arr,l,r)
    return arr

def sorted_merge(array1,array2):
    i=0
    j=0
    array3=[]
    while(i<len(array1) and j<len(array2)):
        if array1[i]<array2[j]:
            array3.append(array1[i])
            i+=1
        else:
            array3.append(array2[j])
            j+=1
    while(i<len(array1)):
        array3.append(array1[i])
        i+=1
    while(j<len(array2)):
        array3.append(array2[j])
        j+=1
    
    return array3

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

def rev(array):
    s=array[::-1]
    return s
