import optparse

# Takes in a plaintext message
# and an integer key and encrypts
# using the Caesar cipher approach
def encrypt(msg, key):
    #New empty message
    newMsg = ""
    
    """
    The purpose of the sign is to be able to handle
    positive and negative signs in one process.

    If the key is positive then we can += 1 each time
    If it is negatice we need to += -1 each time.
    """

    if key > 0:
        sign = 1

    if key < 0:
        sign = -1
    
    #Loops through every character in the message
    for character in msg:

        #Creates a copy of key for safe manipulation
        #Resets for every character
        workingKey = key

        #Translates to ASCII for + and -
        asciiValue = ord(character)
        
        #Needed to keep track of steps left
        while workingKey != 0:

            #If the character is a space skip it
            if asciiValue == 32:
                pass

            #Otherwise, move to the next character
            else:
                asciiValue += sign

                #If we pass 'A' we need to wrap to 'Z'
                if asciiValue == 64:
                    asciiValue = 90

                #If we pass 'Z' we need to wrap to 'A'
                if asciiValue == 91:
                    asciiValue = 65

                #If we pass 'a' we need to wrap to 'z'
                if asciiValue == 96:
                    asciiValue = 122

                #If we pass 'z' we need to wrap to 'a'
                if asciiValue == 123:
                    asciiValue = 97

            #change number of needed steps left
            workingKey -= sign
    
        #Add the new translated character to the final message
        newMsg += chr(asciiValue)

    #Prints final message
    print(newMsg)


# Takes in an encrypted message
# and an integer key and decrypts
# using the Caesar cipher approach
def decrypt(msg, key):
    """
    Changes the key to the opposite of what is inputted, 
    therefore decrypting
    """
    decryptKey = key * -1

    #Encrypts with the opposite key, therefore decrypting
    encrypt(msg, decryptKey)


def main():
    parser = optparse.OptionParser("usage%prog "+ "-f <decrypt | encrypt> -m <message> -k <key>")
    parser.add_option('-f', dest='function', type='string', help='[ decrypt | encrypt ]')
    parser.add_option('-m', dest='msg', type='string',  help='message to encrypt (plaintext) or decrypt (encrypted)')
    parser.add_option('-k', dest='key', type='int', help='cipher key as an integer')
    (options, args) = parser.parse_args()
    function = options.function
    if ((function != "encrypt" and function != "decrypt") or function == None):
        print('[-] You must specify a valid function: "encrypt" or "decrypt"')
        exit(0)
    msg = str(options.msg)
    key = int(options.key)
    if (msg == None) | (key == None):
        print('[-] You must specify a message and key.')
        exit(0)
    if function == "encrypt":
        encrypt(msg, key)
    elif function == "decrypt":
        decrypt(msg, key)

if __name__ == '__main__':
    main()