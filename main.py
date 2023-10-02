print("Limit of year is 2099")
print("This program is coded by Arunangshu Mitra")
user_date = input("Enter the date: ")
year = input("Enter the year: ")
print("You have selected ",year)
cal_century = year
user_month = input("Enter the month: ")
check_date = (user_date.isdigit())
check_year = (year.isdigit())
if (check_date and check_year) == True:
     year_user = int(year)
     date = int(user_date)
     date_cal = (year_user%100)
     cal_quotient = (date_cal//4)
     month = 0
     cal_month = 0
     cal_century = 0
     month_code = 0
     if user_month=="January":
          month = month+1
     elif user_month=="February":
         month = month+2
     elif user_month=="March":
         month = month+3
     elif user_month=="April":
         month = month+4
     elif user_month=="May":
         month = month+5
     elif user_month=="June":
         month = month+6
     elif user_month=="July":
         month = month+7
     elif user_month=="August":
         month = month+8
     elif user_month=="September":
         month = month+9
     elif user_month=="October":
         month = month+10
     elif user_month=="November":
         month = month+11
     elif user_month=="December":
         month = month+12
     elif user_month=="1":
          month = month+1
     elif user_month=="2":
         month = month+2
     elif user_month=="3":
         month = month+3
     elif user_month=="4":
         month = month+4
     elif user_month=="5":
         month = month+5
     elif user_month=="6":
         month = month+6
     elif user_month=="7":
         month = month+7
     elif user_month=="8":
         month = month+8
     elif user_month=="9":
         month = month+9
     elif user_month=="10":
         month = month+10
     elif user_month=="11":
         month = month+11
     elif user_month=="12":
         month = month+12
     else:
         print("Enter a valid month")
     if date>0 and month>0 and year_user>0:
          if month==1:
               month_code = (month_code+0)
          elif month==2:
              month_code = (month_code+3)
          elif month==3:
              month_code = (month_code+3)
          elif month==4:
              month_code = (month_code+6)
          elif month==5:
              month_code = (month_code+1)
          elif month==6:
              month_code = (month_code+4)
          elif month==7:
              month_code = (month_code+6)
          elif month==8:
              month_code = (month_code+2)
          elif month==9:
              month_code = (month_code+5)
          elif month==10:
              month_code = (month_code+0)
          elif month==11:
              month_code = (month_code+3)
          elif month==12:
              month_code = (month_code+5)
          else:
              print("Enter a valid month")
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
              print("Sorry we just encountered a problem while finding the day...please enter another number")
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
     else:
              print("Sorry we just encountered a problem while finding the day.../nplease enter another number")
              print("Enter a valid number")
else:
     print("Enter a valid year and date")
