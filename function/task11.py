nums = list(range(1, 21))

result = list(map(lambda x : x ** 2,list(filter(lambda x: x % 2 == 0,nums))))

print(result)