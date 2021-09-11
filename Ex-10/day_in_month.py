def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 != 0) :
            if (year % 400 == 0):
                return True
            else:
                return True
        else:
            return False
    else:
        return False

def days_in_month(year, month):
    if 0 < month < 12: 
        # months_days = [31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
        months_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
        # leap = is_leap(year)
        # if month % 2 == 0 and month != 2:
        #     return months_days[0]
        # elif month % 2 != 0 and month != 2:
        #     return months_days[1]
        # elif month == 2:
        #     if leap:
        #         return months_days[2]
        #     else:
        #         return months_days[3]
        if is_leap(year) and month == 2:
            return 29
        return months_days[month - 1]
    else:
        return "Invalid month"    
        


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)