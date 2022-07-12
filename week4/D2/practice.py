# # number_list = [1,2,3,4,5]

# # # for i in number_list:
# # #     print(i)

# # # range(star, end, step)
# # print(number_list[0::2])
# # print(number_list[-1::-1])

# # number_list[2] = 33
# # print ('updated list:', number_list)

# # numbers_b = [6,7,8,9]

# # number_list += numbers_b

# # number_list *= 2


# # print('After addition list:', number_list)

# # print('after multiplication list:', number_list)





# # # #index looping when looping from the middle
# # print('looping through indexes')
# # for i in range(len(numbers))
# #     print[i]

# # # enumerate for looping from start of list
# # # print('looping through enumerate')
# # # for i, val in enumerate(numbers):
# # #     print(i)
# # #     print(val)

# # print('looping through items')
# # for num in numbers[2:]:
# #     print(num)

# numbers = [1,2,3,4,5]

# product = numbers[0]
# for num in numbers[1:]:
#     product *= num
    
# print('product')

# list1 = [1,2,3,4,5]

# multiply = 1 
# for i in list1:
#     multiply *= i 
#     print(multiply)



# a = []
# #adding itmes
# a.append(1)
# print(a)

#to remove first occuracnce of 1
# a.remove(1)
# print(a)

# to remove first index value
# del a[0]
# print(a)


# a += [2,3,4]
# a.pop()
# print(a)


# elegible_users = ['yossi','david', 'reuven']
# #pop for removing by index + returning
# blocked_user = elegible_users.pop(1)
# print(blocked_user)


#sorting items

# char_list = ['z','b','f','a','d']

# sorted_char_list = sorted(char_list)

# print(sorted_char_list)

# char_list.sort()

# print('original list after sort():'char_list)



# list1 = [5,10,15,20,25,50,20]

# x = list1.index(20)
# print(x)

# list1[x] = 200

# print(list1)



# a_tuple = (1,2,3)

# print(a_tuple)

# a_tuple = 1,2,3

# print(a_tuple)

# person_1 = ('yossi', 'yossi@gmail.com',30)
# person_2 = ('yosef', 'yosef@gmail.com',25)


# a, b = b, a
# print(a)
# print(b)




# a_tuple = (10,20,30,40)

# a, b, c, d = a_tuple
# print(a)
# print(b)
# print(c)
# print(d)


# number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# # We are using "for loop" to iterate the multiplication 10 times       
# print ("The Multiplication Table of: ", number)    
# for count in range(1, 11):      
#    print (number, 'x', count, '=', number * count) 



















# num = int(input('enter number '))


# # for i in range(1, 11):
# #    print(num*i)

# # for j in range()


for row in range(1, 11):
    for col in range(1, 11):
        num = row * col
        if num < 10:
            empty = "  "
        else:
            if num < 100:
                empty = " "
        if col == 0:
            if row == 0:
                print("    ", end='')
            else:
                print("  ", row, end='')
        elif row == 0:
            print("  ", col, end='')
        else:
            print(empty, num, end='')
    print()