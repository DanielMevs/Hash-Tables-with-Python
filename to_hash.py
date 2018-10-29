d=[102, 301, 21, 34, 42, 109, 2, 29, 57, 82, 401, 43, 73]
print("data set:", d)
def to_hash(d, func, table_len):
    '''takes a table of values, a hash function and a table length
    returns a hash table'''
    keys= [func(k) for k in d]
    pairs= dict(zip(d,keys))
    mapping = [[x if pairs[x]==k else None for x in pairs]for k in range(table_len)]
    return [list(filter(lambda x: x!=None,k)) for k in mapping]
f= lambda x: x%5
ls = to_hash(d, f,5)
print("hashed keys:", ls)


def lookup (ls,element,x=0,y=0):
    '''takes  hash table and an element
    returns the element's index'''
    if not ls[x]:
        return lookup(ls,element,x+1,0)
    if ls[x][y]==element:
        return (x,y)
    elif y==len(ls[x])-1:
        return lookup(ls,element,x+1,0)
    return lookup(ls,element,x,y+1)

sorted_ls = []
new_dict = {}
for i in d:
    sub_tup = lookup(ls, i)
    new_dict.update({sub_tup: i})
    sorted_ls.append(lookup(ls, i))



    
def ascendingSort(arr, N):
    #print("Original array: ", arr)
    n = N-1
    count = 0
    j = 0
    while(n):
        #print ("n: ",n)
        temp = 0
        for i in range(1,n+1):
            
            if(arr[i-1] > arr[i]) :
                swap(arr, i-1, i)
                temp = i
                j = j +1
            #print(i, " ", arr)
        n=temp
    return arr

def swap(arr,x,y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

#print(ascendingSort(sorted_ls, len(sorted_ls)))
print('\n')
new_ls = ascendingSort(sorted_ls, len(sorted_ls))
print("{:<15s}{:<15s}{:>10s}".format("Hash value","key","Table index"))
print('_'*45)
for x,y in enumerate(new_ls):
    print("{:<15s}{:<15d}{:<15d}".format(str(y), new_dict[y], x))
    
    


