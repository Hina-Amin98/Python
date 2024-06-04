def isEven(num):
    #file = open("newFile5.txt", 'x')
    returnData = ""

    if(num % 2 == 0):
        returnData = "Number is even"
    else:
        returnData = "Number is odd"

    return returnData    


result = isEven(3)

file = open("newFile5.txt", 'w')
file.write(str(result))
file.close()