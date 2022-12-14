letters = []
for i in range(0,26):
    letters.append(chr(65+i))


def encrypt(key,input_):
    key = int(key)
    letters = []
    for i in range(0,26):
        letters.append(chr(65+i))
    actual = ""
    for char in input_:
        found = False
        for i in range(0,26):
            if char.upper() ==  letters[i]:
                #capital letter
                if char == char.upper():
                    shift = (((ord(char)-65+key)%26)+65)
                    found = True
                #lower case
                else:
                    shift = (((ord(char)-97+key)%26)+97)
                    found = True
        if found == True:
            actual = actual + (chr(shift))
        else:
            actual = actual + char
   
    return actual
            
                    
     
def decrypt(key, input_):
    key = int(key)
    new = ""
    alpha = []
    for i in range(0,26):
        alpha.append(chr(65+i))
    for char in input_:
        found =  False
        up_char = char.upper()
        for i in range(0, (len(alpha))):
           
            if up_char == alpha[i]:
                found = True
                if up_char == char:
                    #caps
                    shift = chr((((((ord(char)-65)-key)+26)%26)+65))
                    new = new + shift
             
                else:
                    #low
                    shift = chr((((((ord(char)-97)-key)+26)%26)+97))
                    new = new + shift
                   
        if found == False:
           
            new = new + char

            
           
        
    return new
            
        


