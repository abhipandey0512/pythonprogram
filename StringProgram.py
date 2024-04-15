#Task 3 You have a string message: "My name is Abhishek Pandey" convert this to "Pandey Abhishek is name My".
s = "My name is Abhishek Pandey"
words = s.split()
result = " ".join(words[-1:] + words[:-1])
print(result)