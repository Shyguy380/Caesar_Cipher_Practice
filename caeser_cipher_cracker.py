import optparse

def decrypt(msg):
    #Number of possible shifts
    numPossible = 26
    
    shift = 1
    
    #Changes key each time to iterate through all possible changes
    for shift in range(numPossible):
        newMsg = ""

        #Loops through every character in the message
        for character in msg:

            #Creates a copy of key for safe manipulation
            #Resets for every character
            workingKey = shift

            #Translates to ASCII for + and -
            asciiValue = ord(character)
            
            #Needed to keep track of steps left
            while workingKey != 0:

                #If the character is a space skip it
                if asciiValue == 32:
                    pass

                #Otherwise, move to the next character
                else:
                    asciiValue += 1

                    #If we pass 'Z' we need to wrap to 'A'
                    if asciiValue == 91:
                        asciiValue = 65

                    #If we pass 'z' we need to wrap to 'a'
                    if asciiValue == 123:
                        asciiValue = 97

                #change number of needed steps left
                workingKey -= 1

            #Add changed character to message
            newMsg += chr(asciiValue)

        print(newMsg)

def main():
    parser = optparse.OptionParser("usage%prog "+ "-m <message>")
    parser.add_option('-m', dest='msg', type='string',  help='message to decrypt')
    (options, args) = parser.parse_args()
    msg = str(options.msg)
    if (msg == None):
        print('[-] You must specify a message and key.')
        exit(0)

    decrypt(msg)

if __name__ == '__main__':
    main()