# this function coverts the letter of each message into its Unicode value so we can add the key to 
#the Unicode value to get the proper tranlation. We set it up in a way that the keys cycles either
#the 97-122 or 65-90 Unicode digits to wrap around through lower or upper case letters respectively.

def caesar_encrypt(key, message):
    """Encrypt a message"""
    encrypted_message = ""
    for i in message:
        if ord(i) >= 97 and ord(i) <= 122:
           encrypted_message += chr((ord(i)- 97 + int(key))%26 + 97)
        elif ord(i) >= 65 and ord(i)<=90:
            encrypted_message += chr((ord(i)- 65 + int(key))%26 + 65)
        else:
            encrypted_message += i
    return encrypted_message

def caesar_decrypt(key, message):
    """Decrypt a message"""
    decrypted_message = ""
    for i in message:
        if ord(i) >= 97 and ord(i) <= 122:
            decrypted_message += chr((ord(i)- 97 - int(key))%26 + 97)
        elif ord(i) >= 65 and ord(i)<= 90:
            decrypted_message += chr((ord(i)- 65 - int(key))%26 + 65)
        else:
            decrypted_message += i
    return decrypted_message

z=caesar_encrypt(12, "Experience is the teacher of all things.")
print(z)
print(caesar_decrypt(12, z))
