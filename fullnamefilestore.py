first_name = "Hina"
last_name = "Amin"
full_name = first_name + "" + last_name

def storeInFile(full_name):
    #file = open("newFile2.txt", 'x')
    file = open("newFile2.txt", 'a')
    file.write(str(full_name))
    #file = open("newFile.txt", 'r')
   # file.close()

storeInFile(full_name)   