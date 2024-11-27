List1 = ["banana","apple",3,"banana"] #ordered , changable ,duplicated allowed
D = [1,2,3,1,1,3]
D.sort()
print()
print(D[::-1])
print(D.count(2))
print(List1)
print(D[1::])
print(List1[1:2])
List1[:1]=["orange"]
print(List1)

List1.insert(0,"banana")
print(List1)
List1.append(5)
print(List1)
List2 = ["first","second","third"]
List2.remove("first")
print(List2)
List2.pop(0)
print(List2)
List1.clear()
print(List1)

#-----Tuple--------#ordered, immtable, allow duplicate
tupe1=("apple",1,2,"mango","apple")
print(tupe1[0])
tupe2=list(tupe1)
print(tupe2,"tuple as list")
tupe2.append("new2")
tupe1=tuple(tupe2)
print(tupe1)

#------Dictionary------
Dict={"name":10,"number":20,"address":5,"name":1}
a =Dict.get("name")
print(a)
print(Dict.keys())
print(Dict.values())
print(sorted(Dict.values(),reverse=True))
print(Dict["name"])
print("-------dictorny")

List3 = ["a","b","c"]
print(List3)
List4=List3
List4[0]="A"
print(List3)
print(List3[1:-2])
print(List3[:])

A = ["A","B"]
B = A.copy()
B.append("C")
print("B:--", B)
print("A:--", A)

 ### display duplicate char in list
exa = ["india","in","input","apple"]
print(exa.count("in"))
strr = ''.join(exa)
print(strr.count("i"))
print(strr)
dic = []
for i in strr:
    if strr.count(i)>1 and i not in dic:
        dic.append(i)
print(dic)

List=["A","B","C","A","C","B"]
DICT={}
print(DICT)
for i in List:
    DICT[i]=List.count(i)
print(DICT)
DICT['C']=3

list=[10,1,2]
print(sorted(list)[-2])

numbers=[10,7,8,90]
numbers.sort()
print(numbers)
largest = max(numbers)
print(largest)
numbers.remove(largest)
print(max(numbers))

set1=set()
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)

emp=["A","","b",""]
emp.sort()
print(emp)
emp.remove("")
print(emp)

num=[2,3,4,5,6,10,15]
for i in num:
    if i%2==0 and i%5==0:
        print("$")
    elif i%2==0:
        print(i)
    elif i%5==0:
        print("$")
list2=[1,10,11,3,4,0]
m=max(list2)
print(m)



