def isYearLeap(year):
    if (year%4 == 0 and year%100 == 0 and year%400 == 0) or (year%4 == 0 and year%100 != 0):
        return True
    else:
        return False        
        

def daysInMonth(year, month):
    if type(month) == int and month>0 and month<13 and type(year) == int and year>0 :
        num_days=[31,0,31,30,31,30,31,31,30,31,30,31]
        if isYearLeap(year):
            num_days[1]=29
        else:
            num_days[1]=28
        return num_days[month-1]
    else:
        return None
     

      
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
