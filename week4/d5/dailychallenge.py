
words = ['without', 'hello', 'bag', 'world']
result = [i for _, i in sorted((word[0], word) for word in words)]
print(result)
