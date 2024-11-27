List = [1,3,5,8,4,80,10]
List1 = [1,3,5,8,4,80,10]

result = list(filter(lambda n:n%2==0,List))
result1 = list(map(lambda n:n*2,List))
result2 = list(filter(lambda n:n*3,List1))

print(result)
print(result2)