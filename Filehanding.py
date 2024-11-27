file = open('Data.txt','r')  # reading file
print(file.read())
#file1=open('data1','w') #creating file name data1
#file1.write('writing ddd') # writing data to file

#for data in file:
    #file1.write(data)

#f = open("ABC.txt",'w')
#f.write("line1 added")
#f.write("\nline2")

def word_line():
    word = "hi"
    line = 1
    with open("Data.txt",'r') as f1:
        data = f1.read()
        #print(data)
        if word in data:
            print("data found:" +word)
        else:
            print("not found")

word_line()