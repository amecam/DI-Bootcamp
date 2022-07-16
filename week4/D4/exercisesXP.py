# def display_message():
#     print('i love python')
# display_message()


# def favorite_book(title):
#     print('My favorite book is the ' +title)

# favorite_book('Torah')

# def describe_city(city, country):
#     print(city +'is in ' +country)

# describe_city('Toronto ', 'Canada')


# def make_shirt(size='large', text='ilovepython'):
#     print('The size of the shirt is ' +size , 'and the text is ' +text )

# make_shirt('large')
# make_shirt('medium')
# make_shirt('XXL', 'iloveisrael')


# def show_magicians(users):
#     for user in users:
#         print('the Great '+ user.title())
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# show_magicians(magician_names)


import random
def get_random_temp(season):
    if season == "winter":
        return(random.randint(-10, 16))
    elif season == "summer":
        return(random.randint(32, 40))
    elif season == "spring":
        return(random.randint(24, 32))
    elif season == "fall":
        return(random.randint(16, 24))
get_random_temp("fall")
def main():
    temp = get_random_temp("fall")
    if temp < 0:
        print( "Brrr, thats freezing! Wear some extra layers today")
    elif 0<= temp <= 16:
        print( "Quite chilly! Dont forget your coat")
    elif 16< temp <= 23:
        print( "Its cool outside")
    elif 24< temp <= 32:
        print("Its hot outside")
    elif 32< temp <= 40:
        print("Its very hot dont forget your water")
main()


