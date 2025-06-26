prices = ["$120", "$340", "$50", "$90"]

result = list(map(lambda x: x[1:len(x)] , prices))

print(result)