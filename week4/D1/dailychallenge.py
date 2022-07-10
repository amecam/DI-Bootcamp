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