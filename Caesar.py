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
            
                    
            
       
            
                
                
        
        

def brute_force(input_, letters):
    found_letters = ["a"]
    amount = [0]
    located = False
    found  = False
    print(len(amount))
    # first try most common for e
    for char in input_:
        for i in range(0,len(found_letters)):
            if char == found_letters[i]:
                amount[i] = amount[i] + 1
                found = True
        if found == False:
            found_letters.append(char)              
            amount.append(1)
        found = False
    if amount[0] == 0:
        del found_letters[0]
        del amount[0]

    brute_shift = found_letters[amount.index(max(amount))]
    if brute_shift == brute_shift.upper():
        E = ord("E")
        if ord(brute_shift) > E:
            brute_key = ord(brute_shift) - E
        else:
            brute_key = 26 - (E- ord(brute_shift))
    print(brute_key, input_, letters)
    encrypt(brute_key, input_, letters)
    
                    
     
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
            
        


