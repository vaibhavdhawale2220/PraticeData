num = int(input("Enter Number:"))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "Yes")
else:
    print(num, "No")


# 153 = 1*3 + 5*3 + 3*3