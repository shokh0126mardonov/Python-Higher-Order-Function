words = ["sun", "mountain", "a", "apple"]

result = list(sorted(words, key = lambda i: len(i)))

print(result)