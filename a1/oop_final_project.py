#####################################################################
# Object Oriented Programming (python)
# Liam Kearns           100 871 567
# Spencer Strickland    100 875 589
# Ryan Hamilton         100 879 095
# Final Project
#####################################################################

import random
import string
import math
import time
import sympy
from sympy import randprime  # to install sympy, use CMD "pip install sympy" or "pip3 install sympy for python3"
from re import sub


#####################################################################
#####################################################################

class Message:

    #####################################################################

    def userinp():

        listofmessage = []

        while True:

            print("Enter Message # ")
            userin = str(input())
            userin2 = userin.lower()
            if userin2 == "stop":
                break
            if type(userin) is str:
                print("...Encrypting Message...")
                listofmessage.append(userin)
            if not type(userin) is str:
                raise TypeError("A String must be entered")

        plaintextMsg.Encrypt(listofmessage)

    #####################################################################


#####################################################################

class plaintextMsg(Message):

    def __init__(self, listofmessage):
        super().__init__(listofmessage)

        self.listofmessage = listofmessage

    #####################################################################

    def Encrypt(listofmessage):  # encryppts all entered messages and prints desiered info

        for x in listofmessage:

            choice = random.randint(0, 5)  # randomizing encryption choice
            # choice =  # FOR TESTING

            if choice == 0:
                obj = Substitution()
                print("Original Message         ", x)
                print("Encrypted Message        ", obj.encrypt(x))
                print("Encryption Method        ", ciphertextMsg.getmethod(choice))
                print("\n\n")

            if choice == 1:
                obj = Playfair()
                print("Original Message         ", x)
                print("Encrypted Message        ", obj.encrypt(x))
                print("Encryption Method        ", ciphertextMsg.getmethod(choice))
                print("\n\n")
            if choice == 2:
                obj = Caesar()
                print("Original Message         ", x)
                print("Encrypted Message        ", obj.encrypt(x))
                print("Encryption Method        ", ciphertextMsg.getmethod(choice))
                print("\n\n")
            if choice == 3:
                obj = Transposition()
                print("Original Message         ", x)
                print("Encrypted Message        ", obj.encrypt(x))
                print("Encryption Method        ", ciphertextMsg.getmethod(choice))
                print("\n\n")
            if choice == 4:
                obj = Product()
                print("Original Message         ", x)
                print("Encrypted Message        ", obj.encrypt(x))
                print("Encryption Method        ", ciphertextMsg.getmethod(choice))
                print("\n\n")
            if choice == 5:
                obj = RSA()
                print("Original Message         ", x)
                print("Encrypted Message        ", obj.encrypt(x))
                print("Encryption Method        ", ciphertextMsg.getmethod(choice))
                print("\n\n")


#####################################################################
#####################################################################

class ciphertextMsg(Message):

    def __init__(self, choice):
        self.choice = choice

    #####################################################################

    def getmethod(choice):  # returns method used for encryption

        if choice == 0:
            return "Substitution"
        if choice == 1:
            return "PlayFair"
        if choice == 2:
            return "Caesar"
        if choice == 3:
            return "Transposition"
        if choice == 4:
            return "Product"
        if choice == 5:
            return "RSA"

    def getsecretkey(choice):  # returns encryption key

        if choice == 0:
            return Substitution.getSecretKey()
        if choice == 1:
            return Playfair.getSecretKey()
        if choice == 2:
            return Caesar.getSecretKey()
        if choice == 3:
            return Transposition.getSecretKey()
        if choice == 4:
            return Product.getSecretKey()
        if choice == 5:
            return RSA.getSecretKey()


#####################################################################
#####################################################################

class Substitution:

    def __init__(self):

        self.alphabet = list(string.ascii_letters)  # Creates the key for encryption/decription
        self.key = self.alphabet.copy()
        random.shuffle(self.key)

        self.encryptedMessage = None

    #####################################################################

    def encrypt(self, message):

        tempEncryption = []

        for letter in message:
            if letter not in self.alphabet:
                tempEncryption.append(letter)

            else:
                tempEncryption.append(self.key[self.alphabet.index(letter)])

        self.encryptedMessage = "".join(tempEncryption)

        return self.encryptedMessage

    #####################################################################

    def decryption(self):

        tempDecrypt = []

        for letter in self.encryptedMessage:
            if letter not in self.alphabet:
                tempDecrypt.append(letter)

            else:
                tempDecrypt.append(self.alphabet[self.key.index(letter)])

        decryptidedMessage = "".join(tempDecrypt)

        return decryptidedMessage

    #####################################################################

    def getSecretKey(self):
        return self.key


#####################################################################
#####################################################################

class Playfair:

    #####################################################################

    def createkey(self):  # Creates the key for encryption/decription

        length = int(25)
        letters = string.ascii_lowercase
        secret = (''.join(random.choice(letters) for i in range(length)))

        return secret

    #####################################################################

    def create_matrix(self):

        obj = Playfair()
        global key
        key = obj.createkey()
        key = key.upper()
        matrix = []
        matrix = [[0 for i in range(5)] for j in range(5)]
        letters_added = []
        row = int()
        col = int()

        for letter in key:  # add the key to the matrix
            if letter not in letters_added:
                matrix[row][col] = letter
                letters_added.append(letter)
            else:
                continue
            if (col == 4):
                col = 0
                row += 1
            else:
                col += 1

        # A=65 Z=90
        for letter in range(65, 91):  # Add the rest of the alphabet to the matrix
            if letter == 74:
                continue
            if chr(letter) not in letters_added:  # Do not add repeated letters
                letters_added.append(chr(letter))

        index = 0
        for i in range(5):
            for j in range(5):
                matrix[i][j] = letters_added[index]
                index += 1
        return matrix

    #####################################################################

    def separate_same_letters(self, message):  # Add fillers if the same letter is in a pair

        index = 0
        while (index < len(message)):
            l1 = message[index]
            if index == len(message) - 1:
                message = message + 'X'
                index += 2
                continue
            l2 = message[index + 1]
            if l1 == l2:
                message = message[:index + 1] + "X" + message[index + 1:]
            index += 2
        return message

    #####################################################################

    def indexOf(self, letter, matrix):  # Return the index of a letter in the matrix
        for i in range(5):
            try:
                index = matrix[i].index(letter)
                return (i, index)
            except ValueError:
                continue
        return None  # return None if letter is not found in matrix

    #####################################################################

    def encrypt(self, message, encrypt=True):

        message = (sub(r'[^a-zA-Z]', '', message))
        time.sleep(.5)

        inc = 1
        if encrypt == False:
            inc = -1
        obj = Playfair()
        matrix = obj.create_matrix()
        message = str(message)
        message = message.upper()
        message = message.replace(' ', '')
        message = obj.separate_same_letters(message)
        message = str(message)
        cipher_text = ''
        row1 = int()
        row2 = int()
        col1 = int()
        col2 = int()
        l1 = int()
        l2 = int()
        for (l1, l2) in zip(str(message)[0::2], str(message)[1::2]):

            index = self.indexOf(l1, matrix)
            if index is None:
                l1 = 'L'
                index = self.indexOf(l1, matrix)
            row1, col1 = index
            index = self.indexOf(l2, matrix)
            if index is None:
                l2 = 'K'
                index = self.indexOf(l2, matrix)
            row2, col2 = index

            if row1 == row2:
                cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
            elif col1 == col2:
                cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
            else:
                cipher_text += matrix[row1][col2] + matrix[row2][col1]

        return cipher_text

    #####################################################################

    def getSecretKey():
        return key


#####################################################################
#####################################################################

class Caesar:

    def createkey(self):  # Creates the key for encryption/decription
        secret = int(0)
        secret = random.randint(0, 25)

        return secret

    def encrypt(self, plainText):
        obj = Caesar()
        self.shift = obj.createkey()
        cipherText = ""
        for ch in plainText:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + self.shift
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                cipherText += finalLetter
            else:
                cipherText += ch
        return cipherText

    def decrypt_caesar(self, cipherText):
        plainText = ""
        for ch in cipherText:
            if ch.isalpha():
                stayInAlphabet = ord(ch) - self.shift
                if stayInAlphabet < ord('a'):
                    stayInAlphabet += 26
                finalLetter = chr(stayInAlphabet)
                plainText += finalLetter
            else:
                plainText += ch
        return plainText

    def getSecretKey(self):
        return self.shift


#####################################################################
#####################################################################

class Transposition:

    #####################################################################

    def createkey(self):  # Creates the key for encryption/decription
        secret = int(0)
        secret = random.randint(1, 1000)

        return secret

    #####################################################################

    def encrypt(self, message):
        obj = Transposition()
        key2 = obj.createkey()
        key2 = int(key2) % (len(message) - 1)
        cipherText = [""] * key2
        for col in range(key2):
            pointer = col
            while pointer < len(message):
                cipherText[col] += message[pointer]
                pointer += key2
        return "".join(cipherText)

    #####################################################################

    def getSecretKey(self):
        return key


#####################################################################
#####################################################################

class Product:

    #####################################################################

    def createkey(self):  # Creates the key for encryption/decription
        secret = int(0)
        secret = random.randint(0, 25)

        return secret

    #####################################################################

    def encrypt(self, plain_text):

        obj = Product()
        self.key = obj.createkey()
        key2 = self.key
        # transposition key1
        transposition_cipher = ""
        for i in range(len(plain_text)):
            if i % 2 == 0:
                transposition_cipher += plain_text[i]
        for i in range(len(plain_text)):
            if i % 2 != 0:
                transposition_cipher += plain_text[i]

        # substitution key2
        substitution_cipher = ""
        for ch in transposition_cipher:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + int(key2)
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                substitution_cipher += finalLetter
            else:
                substitution_cipher += ch

        return substitution_cipher

    #####################################################################

    def decrypt_product_cipher(self, cipher_text):

        key2 = self.key

        reversed_substitution_cipher = ""
        for ch in cipher_text:
            if ch.isalpha():
                stayInAlphabet = ord(ch) - int(key2)
                if stayInAlphabet < ord('a'):
                    stayInAlphabet += 26
                finalLetter = chr(stayInAlphabet)
                reversed_substitution_cipher += finalLetter
            else:
                reversed_substitution_cipher += ch

        reversed_transposition_cipher = ""
        mid_point = len(reversed_substitution_cipher) // 2
        for i in range(mid_point):
            reversed_transposition_cipher += reversed_substitution_cipher[i] + reversed_substitution_cipher[
                i + mid_point]

        return reversed_transposition_cipher

    #####################################################################

    def getSecretKey(self):
        return self.key


#####################################################################
#####################################################################

class RSA:

    def __init__(self):

        # Creates the key(s) for encryption/decription
        self.p = randprime(4000, 6000)
        self.q = randprime(2000, 4000)

        self.n = self.q * self.p

        self.phi = math.lcm((self.p - 1) * (self.q - 1))

        # sets e to a commonly used public encryption number, but makes sure
        # that it IS relitivelyprime with phi before moving on
        self.e = 65537

        while math.gcd(self.e, self.phi) != 1:
            self.e = randprime(40000, 100000)

        self.d = pow(self.e, -1, self.phi)

        self.key = {"p": self.p, "q": self.q, "n": self.n, "φ(n)": self.phi, "Public key/e": self.e,
                    "Encryption key/d": self.d, }
        self.encryptedMessage = None

    #####################################################################

    def encrypt(self, message):

        encrytionTemp = []

        # converts the sentence to numbers their value in ASCII and encrypts
        # using m(c) = c^d mod n with c being the translated ASCII values
        for letter in message:
            encrytionTemp.append(pow(ord(letter), self.e, self.n))

        # Combines into one string
        self.encryptedMessage = " ".join(map(str, encrytionTemp))

        return self.encryptedMessage

    #####################################################################

    def decryption(self):

        tempList = self.encryptedMessage.split()
        decryptionTemp = []
        decryptedMessage = None

        # applies the same formula as before, but changes key to private for
        # decryption of encoded letters
        for letter in tempList:
            decryptionTemp.append(chr((pow(int(letter), self.d, self.n))))

        decryptedMessage = "".join(decryptionTemp)

        return decryptedMessage

    #####################################################################

    def getSecretKey(self):
        return self.key


#####################################################################
#####################################################################

def main():
    run = Message
    run.userinp()


#####################################################################
#####################################################################

if __name__ == "__main__":
    main()

#####################################################################
#####################################################################