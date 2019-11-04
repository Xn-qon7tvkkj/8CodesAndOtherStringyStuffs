# Transposition Cipher

# encryption function
def scramble2Encrypt(plainText):
    # stripSpaces(plainText)
    evenChars = ""
    oddChars = ""
    charCount = 0;
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]     # halflength to the end
    oddChars = cipherText[:halfLength]      # 0 to halflength - 1
    plainText = ""

    for i in range(halfLength):             # split cipherText
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):      # if oddChars is less than evenChars
        plainText = plainText + evenChars[-1]

    return plainText

# write a stripSpaces(text) function here
def stripSpaces(plainText):
    plainText = plainText.replace(" ", "")
    return plainText


# write a caesarEncrypt(plainText, shift)
# write a caesarDecrypt(cipherText, shift)

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

msg_input = input("Enter your message: ")
cipher = int(input("Enter your key: "))

n = len(msg_input)

msg_output = ""

def caesarEncrypt(plainText, shift):
    for i in range(n):
        plainText = msg_input[i]
        idx = ALPHABET.find(msg_input)
        newidx = (idx + cipher) % 26
        msg_output += ALPHABET[newidx]
print(msg_output)



msg2_input = input("Enter your encrypted message: ")
cipher2 = int(input("Enter your key: "))

n2 = len(msg2_input)

msg2_output = ""

def caesarDecrypt(cipherText, shift):
    for i in range(n):
        ch = msg2_input[i]
        idx = ALPHABET.find(ch)
        newidx = (idx + cipher) % 26
        msg2_output += ALPHABET[newidx]
print(msg2_output)