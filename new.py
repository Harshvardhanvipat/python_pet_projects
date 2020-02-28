
hrs = input("enter the hours ")
hrs = int(hrs)
pay = 10.5

if hrs>40:
 hours_worked_over_forty = hrs - 40
 total_pay = (40*10.25) + hours_worked_over_forty*(1.5*10.25)
 print(total_pay)
else :
  normal_pay = hrs*10.25
  print(normal_pay)
