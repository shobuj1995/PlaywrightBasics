actualString="Hello Python"

# Reverse String
reversed_text=''
for char in actualString:
    reversed_text=char+reversed_text
print(reversed_text)

# Using Recurssion
def reverseString(s):
    if len(s) == 0:
        return s
    return reverseString(s[1:]) + s[0]
print(reverseString(actualString))

