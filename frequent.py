from collections import Counter

text = "hope day hope day null null null null null null"

words = text.split()

counter = Counter(words)
top_three = counter.most_common(1)
print(top_three)
