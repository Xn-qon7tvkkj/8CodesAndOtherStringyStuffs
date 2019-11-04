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
# write a caesarEncrypt(cipherText, shift)

shift = 4,
    plainText: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    cipherText: XYZABCDEFGHIJKLMNOPQRSTUV

def caesarEncrypt(plainText, shift):
    msg = input("Enter your message to encrypt: ")
    cipherText = ""
    print("The encrypted message is: ", cipherText)
    return cipherText

def caesarDecrypt(cipherText, shift):
    msg2 = input("Enter your cipher message to decrypt: ")
    plainText = ""
    print("The decrypted message is: ", plainText)
    return plainText