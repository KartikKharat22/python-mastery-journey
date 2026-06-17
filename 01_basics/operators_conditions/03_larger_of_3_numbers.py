num1 = int(input('Enter a 1st number : '))
num2 = int(input('Enter a 2nd number : '))
num3 = int(input('Enter a 3rd number : '))

if num1 == num2 == num3:
    print('All numbers are equal')
elif num1>=num2 and num1>=num3:
    print(f'{num1} is larger ')
elif num2>=num1 and num2>=num3:
    print(f'{num2} is larger ')
else:
   print(f'{num3} is larger ')

