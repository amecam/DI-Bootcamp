#daily challenge part 1 

# text = 'dodo'


# letters_dict = {}


# for char_i, char in enumerate(text):
   
#     if char in letters_dict:
#         letters_dict[char].append(char_i)
#         continue
#     letters_dict[char] = [char_i]


# print(letters_dict)



#part 2 

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"
# wallet_clean = int(wallet.strip('$'))
# if ',' in wallet_clean:
#     wallet_clean = wallet_clean.split(',')
#     wallet_clean = "".join(price_clean)




# can_buy = []
# for product, pricce in items_purchase.items():
#     price_clean = price.strip('$')

#     if ',' in price_clean:
#         price_clean = price_clean.split(',')
#         price_clean = "".join(price_clean)  
        
#     if price_clean > wallet_clean:
#         continue
#     can_buy.append(product)

# print(can_buy)



# def func_name(print_this):
#     print(f"{print_this}")

# def func(name):
#     return "hello "+ name
# welcome = func('Yossi')

# print(welcome)

# global_var = 100

# def calculation(a,b):
#     #local scope
#     addition = a + b
#     substraction = a - b
#     print(global_var)
#     return addition, substraction

# #global scope
# print(calculation(1,2))



def calculation(a,b) -> tuple:
    addition = a + b
    substraction = a - b
    print(global_var)
    return addition, substraction

def welcome_statement(name,gender) -> str:
    if gender == 'M':
        return f"Hello Mr.{name}"
    if gender == 'F':
        return f"Hello Ms.{name}"

def allowed(account,restricted) -> list:
    allowed_list = []
    for account in accounts:
        if account not in restricted:
            allowed_list.append(account)

    return allowed_list


