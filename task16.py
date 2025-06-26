data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = list(filter(lambda x: type(x) == str and len(x) > 5,data))

print(result)

