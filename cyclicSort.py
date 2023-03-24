def CyclicSort(lis):
    pivot = 0
    while(pivot < len(lis)):
        while(lis[pivot] != pivot + 1):
            # temp = 
           
            lis[lis[pivot]-1] ,lis[pivot] = lis[pivot],lis[lis[pivot]-1]
        # else:
        pivot +=1
           
    return lis
l = [3,5,2,1,4]
print(CyclicSort(l))