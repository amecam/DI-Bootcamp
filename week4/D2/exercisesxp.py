#exercise 1 

# my_fav_numbers = {23,34,8,15,1}

# my_fav_numbers.add (22)
# my_fav_numbers.add (45)
# my_fav_numbers.pop ()
# print(my_fav_numbers)

# friend_fav_numbers = {7,10,47}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# #exercise 2

# false 



#exercise 3 

# basket = ['Banana', 'Apples', 'Oranges', 'Blueberries']

# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0,'Apples')
# basket.count('Apples')
# print(basket.count('Apples'))
# basket.clear()
# print(basket)


# #exercise 4

# A float is a number with a decimal and an integer is a whole number



#exercise 5 

# numbers = range(21)
# for number in numbers:
#     if number % 2 == 0 :
#         print(number)


#exercise 6

# while True:
#     name = input("what is your name")
#     if name == "amecam":
#         break


#exercise 7

basket = str(input("what is your varotite fruit")).split()
print(basket)
fruit = input("enter a fruit ")

if fruit in basket:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")





