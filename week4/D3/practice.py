# # from os import PRIO_USER
# # from typing import ValuesView


# user_a = {
#     'first_name': 'Bob',
#     'last_name': 'Ross',
#     'age': 53,
#     'address': 'Tel Aviv',
#     'family': [('Jessica', 34), ('Tommy, 8')]
#     }

# print('Tel Aviv' in user_a.values())

# print('Tel Aviv' == user_a['address'])

# print('first_name' in user_a)

# # # print(user_a['first_name'].upper())

# # print(user_a.keys())
# # for k in user_a.keys():
# #     print(k)


# # for value in user_a.values():
# #     print("Value:",value)

# # for key, value in user_a.items():
# #     print("K and V:", (key,value))

# # name_removed = user_a.pop('first_name')

# # print(user_a)

# # print("Name removed:",name_removed)

# # del user_a['last_name']

# # print(user_a)



# # user_a['firstname'] = name_removed
# # print(user_a)

# # user_a['firstname'] = 'BOBBY'
# # print(user_a)

# # sample_dict = { 
# #    "class":{ 
# #       "student":{ 
# #          "name":"Mike",
# #          "marks":{ 
# #             "physics":70,
# #             "history":80
# #          }
# #       }
# #    }
# # }

# # print(sample_dict["class"]['student']['marks']['history'])


# # sample_dict = {
# #   "name": "Kelly",
# #   "age":25,
# #   "salary": 8000,
# #   "city": "New york"

# # }

# # del sample_dict['name']
# # del sample_dict['salary']

# # print(sample_dict)



# # lista = ['yossi','lise','avner']
# # listb = [1991,1992,1984]
# # listc = ['Tel Aviv', 'Ramat Gan', 'Givataim']

# # members = list(zip(lista, listb, listc))

# # # print(res)
# # # #bonus: named tuples 

# # # info_data = []
# # # for user in members:
# # #     user_dict = {
# # #         'name': user[0]
# # #         'year': user[1]
# # #         'residence': user[2] 
# # #     }


# # print(res)

# # list comprehension

# squared_num = []
# for n in range(5,10):
#     if n % 2 == 0:
#         squared_num.append(n)
#         continue
#     squared_num.append(n**2)
# print(squared_num)

# squared_num = [n ** 2 for n in range(5,10)]
# print(squared_num)

# #dictionary comprehension
# dictionary_comp = {key: value for key, value in enumerate('ABC')}
# print(dictionary_comp)

















