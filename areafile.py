length = 20
width = 10
area = (length * width)

def storeInFile(area):
    #file = open("newFile3.txt", 'x')
    file = open("newFile3.txt", 'w')
    result = "area is " + str(area)
    file.write(str(result))
    #file = open("newFile.txt", 'r')
   # file.close()

storeInFile(area)   