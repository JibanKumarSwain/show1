import calendar
yy = int(input("enter the year: "))
mm = int(input("enter the month: "))
if mm > 12:
    print("error plz enter the 1-12")
else:
    print(calendar.month(yy, mm))
