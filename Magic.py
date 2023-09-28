print("Limit of year is 2099")
print("This program is coded by Arunangshu Mitra")
date = int(input("Enter the date: "))
year_user = int(input("Enter the year: "))
print("You have selected ",year_user)
cal_century = year_user
month = input("Enter the month: ")
date_cal = (year_user%100)
cal_quotient = (date_cal//4)
month_code = 0
cal_month = 0
january = 0
february = 3
march = 3
april = 6
may = 1
june = 4
july = 6
august = 2
september = 5
october = 0
november = 3
december = 5
if month=="January":
     month_code = (month_code+january)
elif month=="February":
    month_code = (month_code+february)
elif month=="March":
    month_code = (month_code+march)
elif month=="April":
    month_code = (month_code+april)
elif month=="May":
    month_code = (month_code+may)
elif month=="June":
    month_code = (month_code+june)
elif month=="July":
    month_code = (month_code+july)
elif month=="August":
    month_code = (month_code+august)
elif month=="September":
    month_code = (month_code+september)
elif month=="October":
    month_code = (month_code+october)
elif month=="November":
    month_code = (month_code+november)
elif month=="December":
    month_code = (month_code+december)
else:
    print("Enter a valid number")
if year_user>=1400 and year_user<=1499: 
    cal_century = 0+2
elif year_user>=1500 and year_user<=1599:
    cal_century = 0+0
elif year_user>=1600 and year_user<=1699:
    cal_century = 0+6
elif year_user>=1700 and year_user<=1799:
    cal_century = 0+4
elif year_user>=1800 and year_user<=1899:
    cal_century = 0+2
elif year_user>=1900 and year_user<=1999:
    cal_century = 0+0
elif year_user>=2000 and year_user<=2099: 
    cal_century = 0+6
else:
    print("Sorry we just encountered a problem while finding the day.../nplease enter another number")
cal_day = (date+month_code+cal_century+date_cal+cal_quotient)%7
if cal_day == 0:
    DAY = "SUNDAY"
elif cal_day == 1:
    DAY = "MONDAY"
elif cal_day == 2:
    DAY = "TUESDAY"
elif cal_day == 3:
    DAY = "WEDNESDAY"
elif cal_day == 4:
    DAY = "THURSDAY"
elif cal_day == 5:
    DAY = "FRIDAY"
elif cal_day == 6:
    DAY = "SATURDAY"
print("The day of ",date," ",month," ",year_user," is ",DAY)




    
    
    
    
