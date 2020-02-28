def computePay(hours, rate):
 hours = float(hours)
 if(hours>40):
    extra_hours = hours - 40
    payment = 40*rate + extra_hours*rate*1.50
    return payment
 else:
     payment = hours*rate
     return payment

test = input("enter the number of hours worked")
test = float(test)
test_rate = input("enter the rate per hour")
test_rate = float(test_rate)

print(computePay(test, test_rate))
