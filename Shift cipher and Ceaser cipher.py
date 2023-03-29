def encryption(plain_text, key):
    cipher_test = ""

    for i in range(len(plain_text)):

        char = plain_text[i]
        if (char.isupper()):
            cipher_test = cipher_test + chr((ord(char) + key - 65) % 26 + 65)
        elif (char.islower()):
            cipher_test = cipher_test + chr((ord(char) + key -97) % 26 + 97)
        else:
            continue

    return cipher_test




def decryption(cipher_text, key):
    main_text = ""

    for i in range(len(cipher_text)):

        text = cipher_text[i]

        if (text.isupper()):
            main_text = main_text + chr((ord(text) - key -65) % 26 +65)
        elif (text.islower()):
            main_text = main_text + chr((ord(text) - key -97) % 26 + 97)
        else:
            continue

    return main_text

plain_text = input('Write your massage: ')
key = int(input('Enter you encryption + decryption key: '))
cipher_text = encryption(plain_text,key)
main_text = decryption(cipher_text,key)
print("Your Text is: " , plain_text)
print("Your Encryption key is: " , key)
print("Your Cipher Text is: " , cipher_text)
print("")
print("")
print("Your endrypted massage is: " , cipher_text)
print("Your decrypted key is: " , key)
print("Your Decripted masssage is: " , main_text)
