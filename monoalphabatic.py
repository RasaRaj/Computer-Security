import  random

alpha = "abcdefghijklmnopqrstuvwxyz"

# Encryption Massage

def encrypt(plain_text, key=None):
    if key is None:
        l = list(alpha)
        random.shuffle(l)
        key = "".join(l)
        print("Alpha: ",alpha)
        print("Key: ",key)
    new=[]
    for i in plain_text:

        new.append(key[alpha.index(i)])
    return "".join(new),key

# Decryption Massage
def decrypt(cipher_text, key=None):
    if key is not None:
        new =[]

    for letter in cipher_text:
        new.append(alpha[key.index(letter)])
    return "".join(new)

plain_text = input("Enter the text: ")
cipher_text,key = encrypt(plain_text, None)
main_text = decrypt(cipher_text, key)
print("The Cipher text is: ",cipher_text)
print("")
print("The main Text is: ",main_text)
print("")

