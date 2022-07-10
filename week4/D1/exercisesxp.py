# run_times = 5
# for i in range(run_times):
#     print("hello world")


# x = pow(99,3)

# print ((x)*8)

# exercise 3 
# False
# true
# false
# false
# false

#exercise 4 

# computer_brand = "mac"
# print(f'I have a {computer_brand} computer')


# exercise 5

# name = 'amecam'
# age = 29
# shoe_size = 12
# info = (f'my name is {name} i am {age} years old and my shoe size is {shoe_size}')
# print(info)

# exercise 6

# a = 32
# b = 23
# if (a > b):
#     print ("hello world")

# exercise 7 

# num = int (input ("Enter any number to test whether it is odd or even: "))

# if (num % 2) == 0:

#               print ("The number is even")

# else:

#               print ("The provided number is odd")

# exercise 8

# my_name = 'amecam'

# b = input('Whats your name ? ')

# if (my_name == b):
#     print("haha we have the same name")


# exercise 9 

# num = int (input ("Whats your height in inches? "))

# if (num < 145) == 0:

#                print ("you are tall enough to ride")

# else:

#                print ("you need to grow some more to ride")


# daily challenge

# a = str(input('type something '))
# if (len(a) < 10):

#     print ("string not long enough")

# else:
#    print ("string too long")
# length = len(a)
# for row in range (length):
#  for col in range(row+1):
#     print(a[col],end= "")
#     print()




# print(a[0]) 
# print(a[-1])

# print(a[0])
# print(a[0:1])
# print(a[0:2])
# print(a[0:3])
# print(a[0:4])
# print(a[0:5])
# print(a[0:6])
# print(a[0:7])
# print(a[0:8])
# print(a[0:9])


string = input('enter the string:')
length = len(string)
for row in range (length):
    for col in range(row+1):
        print(string[col],end= "")
    print()