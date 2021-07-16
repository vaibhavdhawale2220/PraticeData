# lower = 1
# upper = 25

lower = int(input('lower:'))
upper = int(input('upper:'))

print("Print the ", lower, "&", upper)
for num in range (lower,upper + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)