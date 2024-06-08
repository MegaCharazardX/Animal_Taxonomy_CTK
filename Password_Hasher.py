import random
import string
import Loading

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = ['d', 'H', 'v', "'", '[', '@', 'b', 'r', '7', 'T', 'S', 'M', '=', '\\', 'E', 'W', 'A', 'K', 'e', 'i', 'C', 'G', '^', 'w', ' ', '+', '!', 'P', '>', 'y', 'x', 'R', '*', 'q', '/', 'U', 'B', ']', '"', '}', '{', '<', 'g', 'O', 'k', '%', '.', 'N', '0', 't', '-', 'u', '`', 'X', '(', 'L', '?', '4', '8', 'n', 'Q', '&', 'J', '_', 'h', 'o', 'V', '5', ';', '#', 'I', 'l', 's', '9', 'z', 'f', ':', ')', 'Z', 'F', 'c', '1', '~', 'p', 'j', 'Y', 'D', ',', 'm', '3', '6', '|', '2', '$', 'a']

# random.shuffle(key)
# print(key)
class Encrypter :
    #ENCRYPT
    def __init__(self, _text):
        self.text = _text
        
    def encrypt(self):
        #plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for letter in self.text:
            index = chars.index(letter)
            cipher_text += key[index]
        
        return cipher_text

    #DECRYPT
    def decrypt(self):
        #cipher_text = input("Enter a message to decrypt: ")
        plain_text = ""

        for letter in self.text:
            index = key.index(letter)
            plain_text += chars[index]

        return plain_text

#Loading.loading(text = "Encrypting..")
#e = Encrypter("Hari Dhejus").encrypt()
#print(e)
