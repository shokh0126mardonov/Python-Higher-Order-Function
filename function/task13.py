sentence = "Functional programming in Python is very powerful and elegant"

result = list(sorted(sentence.split() , key = lambda x : len(x) , reverse=True))

print(result[:3])
