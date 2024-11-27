a=" Ramya,Tippannavar  "
print(a.split()[::-1])
l = []
for i in a:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print("".join(l))
print(a[::-1])
print(type(a))
print(a.upper())
print(a.lower())
print(a.strip()) #remove space at the begging or end of string
print(len(a))
print(a.replace("R","S"))
print(a.split(",")) #split the string in to substring
b="hari"
c="sh"
print(b+c)
#formatting nymber with string using formart() method
age = 36
name="cena"
txt = "My name is John{}, and I am {}"
print(txt.format(name,age))

#quantity = int(input(""))
#itemno = int(input(""))
#price = int(input(""))
#myorder = "I want {} pieces of item {} for {} dollars."
#print(myorder.format(quantity, itemno, price))

conc1 = ["a","b","c"]
conc2 = [1,2,3]
print(list(zip(conc1,conc2)))

name1 = "hello tieto evry india"
print(name1.capitalize())
name2 = "LOWER"
print(name2.lower())
name3 = "touppercase"
print(name3.upper())
name4 = "hello tieto evry india"
print(name4.title())
name5 = "Hello Tieto Evry India"
print(name5.swapcase())
name6 = "Hello Tieto"
print(name6.startswith("H"))
name7 = ('Hello_Tieto_Evry_India hello'
         'hello')
print(name7.splitlines())
print(name7.split("_"))
print(name7.casefold())
print(name5.count('o'))
print(name5.encode())
print(name7.format('hi'))
print(name7.isalpha())
print(name7.isspace())