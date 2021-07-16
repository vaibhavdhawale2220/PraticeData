list = str(input('Enter string: '))
a = []
for i in list:
    if i not in a:
        a.append(i)
print('The list is :'+ str(a))