def encrypt(text,s):
    result = ""
    text=text.replace(" ","")
 
    for i in range(len(text)):
        char = text[i]
 
       
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
    
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 

text =input("Enter the message:")
s = int(input("Enter the shift code:"))
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))

def decrypt(text,s):
    result = ""

    
    for i in range(len(text)):
        char = text[i]
 

        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
 

        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result
 

text =input("Enter the decrypt message:")
s = int(input("Enter the shift code:"))
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + decrypt(text,s))

