import re


# 1. Check whether a string starts with 'a'
text = "apple"
print("Starts with a:", bool(re.match(r"^a", text)))


# 2. Check whether a string ends with 'a'
text = "banana"
print("Ends with a:", bool(re.search(r"a$", text)))


# 3. Find vowels
text = "Welcome to Python"
print("Vowels:", re.findall(r"[aeiou]", text))


# 4. Find digits
text = "My number is 203 and pin is 500089"
print("Digits:", re.findall(r"[0-9]", text))


# 5. Find all alphabets
text = "Python 3.9 is fun!"
print("Alphabets:", re.findall(r"[a-zA-Z]", text))


# 6. Find special characters
text = "Email: hello@123.com!"
print("Special characters:", re.findall(r"[^a-zA-Z0-9]", text))


# 7. Find all digits using \d
text = "My phone number is 9876543210"
print("Digits:", re.findall(r"\d", text))


# 8. Find non-digits
text = "Pin: 500089"
print("Non-digits:", re.findall(r"\D", text))


# 9. Find whitespace
text = "John Doe"
print("Spaces:", re.findall(r"\s", text))


# 10. Find non-whitespace characters
text = "Hi there!"
print("Non-space characters:", re.findall(r"\S", text))


# 11. Find word characters
text = "user_123@domain.com"
print("Word characters:", re.findall(r"\w", text))


# 12. Find non-word characters
text = "user_123@domain.com"
print("Non-word characters:", re.findall(r"\W", text))


# 13. Find any character except newline
text = "Hello!"
print("All characters:", re.findall(r".", text))


# 14. Dot meta character
text = "acb a9b a_b a b"
print("a.b matches:", re.findall(r"a.b", text))


# 15. Start anchor
print("Start match:", re.match(r"^Hello", "Hello World"))


# 16. End anchor
print("End match:", re.search(r"World$", "Hello World"))


# 17. Zero or more repetitions
text = "ab abb abbb a ac"
print("ab* matches:", re.findall(r"ab*", text))


# 18. One or more repetitions
text = "ab abb abbb a ac"
print("ab+ matches:", re.findall(r"ab+", text))


# 19. Zero or one occurrence
text = "ab abb abbb a ac"
print("ab? matches:", re.findall(r"ab?", text))


# 20. Exact repetition
text = "ab abb abbb abbbb"
print("ab{2} matches:", re.findall(r"ab{2}", text))


# 21. Repetition range
text = "ab abb abbb abbbb"
print("ab{2,3} matches:", re.findall(r"ab{2,3}", text))


# 22. Character class
print("Vowels:", re.findall(r"[aeiou]", "Hello Python"))


# 23. OR operator
text = "I have a cat and a dog."
print("Animals:", re.findall(r"cat|dog", text))


# 24. Grouping
text = "abababab"
print("Repeated group:", re.findall(r"(ab)+", text))


# 25. match()
pattern = r"ab"
text = "abaaab"
result = re.match(pattern, text)
print("match():", result)


# 26. fullmatch()
pattern = r"abaaab"
text = "abaaab"
result = re.fullmatch(pattern, text)
print("fullmatch():", result)


# 27. search()
pattern = r"abab"
text = "xxababyy"
result = re.search(pattern, text)
print("search():", result)


# 28. findall()
pattern = r"\d"
text = "Room 12 has 3 chairs"
print("findall():", re.findall(pattern, text))


# 29. split() using non-word characters
text = "apple,banana;orange-grape"
print("split():", re.split(r"\W+", text))


# 30. sub() - replace digits
text = "Phone: 123-456-7890"
print("sub():", re.sub(r"\d", "#", text))


# 31. subn() - replace and count
text = "Phone: 123-456-7890"
print("subn():", re.subn(r"\d", "#", text))


# 32. Meaning of r'\W+'
text = "apple,banana;orange-grape"
print("Using r'\\W+':", re.split(r"\W+", text))


# 33. Match a simple word
text = "hello world"
print("hello:", re.search(r"hello", text))


# 34. Match complete words
text = "Python is awesome_123"
print("Words:", re.findall(r"\w+", text))


# 35. Split using whitespace
text = "Python is fun"
print("Words:", re.split(r"\s+", text))


# 36. Find non-digits
text = "Price: $100"
print("Non-digits:", re.findall(r"\D", text))


# 37. Optional character
text = "I like color and colour"
print("Color forms:", re.findall(r"colou?r", text))


# 38. Find literal dots
text = "file.txt, file.pdf"
print("Dots:", re.findall(r"\.", text))


# 39. Find 2 to 4 digit groups
text = "123 4567 89"
print("2-4 digit groups:", re.findall(r"\d{2,4}", text))


# 40. Gmail validation
emails = [
    "example@gmail.com",
    "user.name@gmail.com",
    "user+123@gmail.com",
    "invalid-email@yahoo.com",
    "another-invalid@gmail.org"
]

gmail_pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"

for email in emails:
    if re.match(gmail_pattern, email):
        print(email, "is a valid Gmail address")
    else:
        print(email, "is NOT a valid Gmail address")


# 41. General email validation
emails = [
    "user@gmail.com",
    "student@example.org",
    "hello@company.in",
    "wrong-email"
]

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

for email in emails:
    if re.match(email_pattern, email):
        print(email, "is valid")
    else:
        print(email, "is NOT valid")