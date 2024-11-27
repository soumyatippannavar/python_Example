from array import *

val = array('i',[1,2,3,4])
print(val)
val.reverse()
print(val)
print(val[1])
tup=(1,2,3)
dic={"hi":12}

arr=array('i',[])
n=int(input("entre size of array"))
for i in range(n):
    x=int(input("entre values"))
    arr.append(x)

print(arr)

k=int(input("enter search value"))
index=0
for i in arr:
    if i==k:
        print(index)
        break

    index=index+1


print(arr)
arr = arr + 1
print(arr)






