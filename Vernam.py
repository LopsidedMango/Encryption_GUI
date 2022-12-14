def encrypt(key, input_):
    ckey = ''.join([(key[i % len(key)]) for i in range(len(list(input_)))])
    
    letters = []
    for i in range(0,26):
        letters.append(chr(65+i))
    
    final = ""
    
    increment = 0 
    for char in input_:
        found = False
     
        for i in range(0,26):
            if char.upper() ==  letters[i]:
                
                #capital letter
                if char == char.upper():
                    shift = int((ord(char)-65)%26)
                    found = True        
                #lower case
                else:
                    found = True
                    shift = int((ord(char)-97)%26)
                if ckey[increment] == ((ckey[increment]).upper()):
                    key_shift = int((ord(ckey[increment])-65)%26)
                else:
                    key_shift = int((ord(ckey[increment])-97)%26)
                
        if found == True:
           
            result = ((key_shift ^ shift) % 26)
           
            result = chr(result+97)
            if char == char.upper():
                result = result.upper()
        else:
            result = char
        final = final + result
        increment += 1
    
    return final