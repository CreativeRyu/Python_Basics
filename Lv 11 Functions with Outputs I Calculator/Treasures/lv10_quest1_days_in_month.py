def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  if month == 2 and is_leap(year):
    return 29
  else: 
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

####################################################################################

"""
+================================+
|                                |
|   Lv 10 Training Date of Day   |
|                                |
+================================+
"""

day = int(input("Enter a Day: "))
def day_of_year(year, month, day):

  max_days = days_in_month(year, month)

  if day <= max_days:
    return f"{day}.{month}.{year}"
  else:
    print("This Day does not exists in the month.")

print(day_of_year(year, month, day))