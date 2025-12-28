
str = input("Enter a Something")

words = [word.capitalize() for word in str.split()]

words.sort()
for string in words:
    print(f"Sorted string: {string}")