
mystring = str(input('Enter Name:'))

mystring = mystring.casefold()

reverse = reversed(mystring)

if list(mystring) == list(reverse):
    print('Is Palindrome ')
else:
    print('Not')
