# Python program to swap two variables
# developed by : adi

a= 5
b = 10

# To take inputs from the user
#a = input('Enter value of a: ')
#b = input('Enter value of a: ')

# create a temporary variable and swap the values
t = a
a = b
b = t

print('The value of x after swapping: {}'.format(a))
print('The value of y after swapping: {}'.format(b))
