myFile = open('Hina.txt', 'r')
#for reading file 
print(myFile.read())

# for printing some characters
# print(myFile.read(5))

myFile = open('Hina.txt', 'a')
myFile.write("I am appending data")



myFile.close()