def panagram(s):
    a = str.lower(s)  #Remove case sensitivity
    b = list(a)       # Convert into list
    c = set(b)          #remove duplicates
    c = list(c)         #Convert back to list
    
    getascii = []
    for i in range(len(c)):
        getascii.append(ord(c[i]))
    
    getascii.sort()
    sumascii = 0
    
    #get sum of numbers
    for i in range(len(getascii)):
        if 97 <= getascii[i] <= 122:
            sumascii += getascii[i]
    
    sumoriginal = sum(range(97,97+26))
    
    if sumascii != sumoriginal :
        print('not pangram')
    else:
        print('pangram')

string = input().strip()
panagram(string)