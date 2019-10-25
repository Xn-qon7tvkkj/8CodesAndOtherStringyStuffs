# Strings

# Concatenation
#   2 or more strings and put them together


firstName = "Tulip"
lastName = "Swing"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition
#   repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])

print(name[-3])

for i in range(0, len(name)):
    print(name[i])

# Slicing and Dicing

print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

# Searching

print("biv" in name)

if "y" not in name:
    print("y is not in name")
else:
    print("y is in name")


# String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)      This will add a symbol to the beginning and end of the string.
str = "Hello World"
if str == "Hello World":
    str2 = str.center(20,'#')
else:
    str2 == str.center(20,'!')
print("Old value:", str)
print("New value:", str2)


    # ljust         aStr.ljust(w)       This method add the symbols at the end of the string. It alsoreturns the string left justified in a string of length width. The original string is returned if width is less than len(s).
str3 = "Hello World"
if str3 == "Hello World":
    str4 = str.ljust(20, '#')
else:
    str4 == str.ljust(20, '!')
print("Old value:", str3)
print("New value:", str4)


    # rjust         aStr.rjust(w)       This will add symbols at the beginning of the string.
str5 = "Hello World 3"
if str5 == "Hello World 3":
    str6 = str.rjust(20, '#')
else:
    str6 = str.rjust(20, '!')
print("Old value:", str5)
print("New value:", str6)


    # upper         aStr.upper()        This will uppercase the letters.
str7 = 'hello world 4'
print(str.upper())


    # lower         aStr.lower()        This will lowercase the letters.
str8 = 'HELLO WORLD $'
print(str.lower())


    # index         aStr.index(item)    This will have an exception unless the substring is found (lowest index/ValueError)
str9 = 'Working on these string methods are interesting.'
print(str9.index('ing', 10, -18))

    # rindex        aStr.rindex(item)   This will return the last index or an exception.
str10 = 'What is this?'
str11 = 'is'
print(str10.rindex(str11))
print(str10.index(str11))


    # find          aStr.find(item)     This will find a specific word in the index sentence or an exception.
str12 = 'Twinkle Twinkle Little Star'
str13 = 'Little'
print(str12.find(str13))


    # rfind         aStr.rfind(item)    This returns an integer value. If the substring exists inside the string, it returns the highest index where the string is found. If the substring is not found, it returns -1.
str14 = 'let it be'
result1 = str14.rfind('let it')
print("Substring 'let it':", result1)
result2 = str14.rfind('it be')
print("Substring 'it be':", result2)
result3 = str14.rfind('be')
print("Substring 'be':", result3)


    # replace       aStr.replace(old, new)  This replace a word with another.
str15 = "this is this"
print(str15.replace("this", "This"))
print(str15.replace("this", "This was"))

    # Be sure to include multiple examples of all of them in use