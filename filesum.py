sum = 1
for counter in range(5):
    sum = (sum * (counter+1))

def storeInFile(sum):
    #file = open("newFile4.txt", 'x')
    file = open("newFile4.txt", 'a')
    file.write(str(sum))
    #file = open("newFile.txt", 'r')
   # file.close()

storeInFile(sum)       