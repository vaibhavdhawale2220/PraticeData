num1 = float(input('1st Number:'))
num2 = float(input('2nd Number:'))
num3 = float(input('3rd Number:'))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3
print("Largest Number in The Data is", largest)
