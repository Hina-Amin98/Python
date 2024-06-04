num1 = 10
num2 = 30

result = num1 + num2

def storeInFile(result):
    #file = open("newFile.txt", 'x')
    file = open("newFile.txt", 'a')
    file.write(str(result))
    file = open("newFile.txt", 'r')
   # file.close()

storeInFile(result)   