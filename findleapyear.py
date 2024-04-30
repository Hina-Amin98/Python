year = 1995
yearstatus = year % 400
if(yearstatus == 0):
    print("year is leap")
else: 
    checkbyfour = year % 4
    checkbyhundred = year % 100
    if(checkbyfour == 0 and checkbyhundred !=0):
        print("year is leap")
    else:
        print("year is not leap")