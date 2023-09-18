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
    
    
    
def dayOfYear(year, month, day):
    if type(month) == int and month>0 and month<13 and type(year) == int and year>0 and type(day) == int:
        num_days=[31,0,31,30,31,30,31,31,30,31,30,31]
        if isYearLeap(year):
            num_days[1]=29
        else:
            num_days[1]=28
        if day>0 and day<=num_days[month-1]:
            days=0
            for i in range(month-1):
                days+=num_days[i]
            days+=day
            return days                      
        else:
            return None
    else:
        return None
    
# =============================================================================
# PRUEBA DE LA FUNCION
# =============================================================================

testYears = [2020,2019,2016,2023,2022,2018,2015,'Año "2017"',2018]
testMonths = [12,5,3,12,1,2,3.3,12,13]
testDays = [31,17,23,31,12,30,5,6,3]
testResults = [366,137,83,365,12, None, None, None, None]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    dy = testDays[i]
    result = dayOfYear(yr, mo, dy)
    print(yr, mo, dy, "->", result, 'days', "-> ", end="")
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")















