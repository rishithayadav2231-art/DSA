year=int(input("Enter a year:"))
if(year%400==0)or(year%4==0 and year%100!=0):
  print("this  this the leap year")
else:
 print("this is not the leap year")