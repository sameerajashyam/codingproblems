
def ternary_search(arr,i,j,key):
    mid1=i+(j-i)//3
    mid2=j-(j-i)//3
    while i<=j:
        if arr[mid1]==key:
            return mid1
        elif arr[mid2]==key:
            return mid2
        #first part of ternary search
        elif key<arr[mid1]:
            return ternary_search(arr,i,mid1-1,key)
        #third part of ternary search
        elif key>arr[mid2]:
            return ternary_search(arr,mid2+1,j,key)
        else:
            #second part of ternary search
    
            return ternary_search(arr,mid1+1,mid2-1,key)
        #if search element is not found return -1
    return -1



arr=[20,25,47,56,59,63,65,79,82]
i=0#left
j=len(arr)-1#right
key=int(input("Enter number to be found:  "))
position=ternary_search(arr,i,j,key)
print(position)
