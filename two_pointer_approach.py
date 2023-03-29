
#two pointer approach
#two sum
def two_sum(arr,target_sum):
    l=0
    r=len(n)-1
    while l<r:
        if n[l]+n[r]==target_sum:
            return l,r
        elif n[l]+n[r]<target_sum:
            l+=1
        else:
            r-=1
    return -1,-1

n=[20,40,60,80,90,120,240]

target_sum=10

print(two_sum(n,target_sum))
    
