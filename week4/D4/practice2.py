# def calculation(a,b) -> tuple:
#     addition = a + b
#     substraction = a - b
#     print(global_var)
#     return addition, substraction

# def welcome_statement(name,gender) -> str:
#     if gender == 'M':
#         return f"Hello Mr.{name}"
#     if gender == 'F':
#         return f"Hello Ms.{name}"

# def allowed(account,restricted) -> list:
#     allowed_list = []
#     for account in accounts:
#         if account not in restricted:
#             allowed_list.append(account)

#     return allowed_list


# def print_names(*names: tuple):
#     for name in names:
#         print(name)

# print_names('yossi','david','raz','shlomo','whatever')

# def return_args(*args) -> list:
#     args_list = []
#     for arg in args:
#         if isinstance(arg, str):
#             args_list.append(arg * 2)
#         elif isinstance(arg, int):
#             args_list.append(arg ** 2)
#         else:
#             args_list.append(arg)
#         args_list.append(arg)
#     return args_list

# result = return_args(1,2,3,'ABC','BVC',[123])

# print(result)



# #kwargs = key value argument

# def some_func(a, b):
#     print(a, b)


# some_func(5, b=5)

# #some_func(a=5, 5)



# def create_dict_func(**details):
#     return details

# details_yossi = create_dict_func(name = 'Yossi', address = 'Tel Aviv', country = 'Israel', children = ['bob', 'ross'])
# details_lise = create_dict_func(name = 'lise', address = 'Holon', country = 'Israel', gender = 'F')



# print(details_yossi)
# print(details_lise)



# def make_details(*names: tuple, **details: dict):
#     full_details = {}
#     for name in names:
#         full_details[name] = details
#     return full_details

# f_details = make_details('Yossi','Lise','Reuven', Address = '', Zip = -1, Phone = -1)

# print(f_details)



# def to_power(n: int, power:int) -> int:
#     return n ** power


# print(to_power(2,2))

# to_power = lambda n, power: n ** power

# print(to_power(2,2))


# numbers = [1,2,3,4,5,6]

# to_power = lambda n, power: n ** power

# def set_power(power):
#     return lambda: n ** power

# p2_lambda = set_power(4)

# res_list = list(map(lambda n: n ** 2, numbers))

# res_list = list(map((p2_lambda), numbers))

# print(p2_lambda)





# even = lambda n: True if n % 2 == 0 else False

# numbers = [n for n in range(100) ]

# print(list(filter(even, numbers)))


# restricted = ['Ben','Ron']
# accounts = ['Ben','Ron','Raz','Ran','Bill', 'Sam']

# allowed = lambda name: True if name not in restricted else False

# print(list(filter))

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]


# name = lambda n: True if len(n) <= 4 else False

# people = list(filter(name, people))

# print(people)


# hello = lambda n: "hello " + n

# for name in map(hello, people):
#     print(name)




# from functools import reduce

# [1,2,3,4,5]
# 1,2 - > 3

# [3,3,4,5]
# 3, 3 -> 6

# [6,4,5]
# 6,4 -> 10

# [10,5]
# 10,5 -> 15

nums = [1,2,3,4,5]
        [1,2] -> 2
        [2,3] -> 6
        

add = lambda n1,n2: n1 * n2

print(reduce(add,nums))


