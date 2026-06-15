#Swap two numbers without using third variable
a= int(input('Enter a number: '))
b= int(input('Enter b number: '))

a, b = b, a
print(f'Values after swapping \n a:{a} \n b:{b}')
