largest = None
smallest = None

while True:
 number_entered = input('Enter a  number')
 if number_entered == "done" :
  break
 try:
  number_entered = float(number_entered)
  if largest == None and smallest == None:
    largest = number_entered
    smallest = number_entered
 except:
  print('Invalid input')


  continue
 if number_entered > largest:
  # number_entered = float(number_entered)
  largest = number_entered

 if number_entered < smallest:
  # number_entered = float(number_entered)
  smallest = number_entered

print('Maximum is', largest)
print('Minimum is', smallest)
