text = input("enter a string")
revText = text[::-1]
otherText = text[0::1]
anotherText = text[::3]
text = revText
print('Reverse of given string is: ')
print(text)
print(otherText)
print(anotherText)
