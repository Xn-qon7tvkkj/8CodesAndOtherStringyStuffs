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

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def caesarEncrypt(plainText, shift):
    stringtoencrypt = input("Enter your message to encrypt: ")
    stringtoencrypt = stringtoencrypt.lower()
    ciphershift = input("Enter number for ciphershift: ")
    ciphershift = int(ciphershift)
    msgencrypted = ""
    for ch in stringtoencrypt:
        idx = ALPHABET.find(ch)
        newidx = idx + ciphershift
        if ch in letters:
            msgencrypted += ALPHABET[newidx]
        else:
            msgencrypted = msgencrypted + ch
    ciphershift = str(ciphershift)
    print("The encrypted message is: ", msgencrypted)
    print("You shifted over:", ciphershift)

def caesarDecrypt(cipherText, shift):
    stringtodecrypt = input("Enter your cipher message to decrypt: ")
    stringtodecrypt = stringtodecrypt.lower()
    ciphershift = input("Enter number for ciphershift: ")
    ciphershift = int(ciphershift)
    msg2decrypt = ""
    for ch in stringtodecrypt:
        idx = ALPHABET.find(ch)
        nextidx = idx + ciphershift
        if ch in letters:
            stringtodecrypt += ALPHABET[nextidx]
        else:
            stringtodecrypt += stringtodecrypt + ch
    ciphershift = str(ciphershift)
    print("The decrypted message is: ", msg2decrypt)
    print("You shifted over:", ciphershift)