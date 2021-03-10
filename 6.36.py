def caesar(key,text):
    map=dict()
    for i in range(26):
        map.update({chr(i+65):chr((i+key)%26+65)})
        map.update({chr(i+97):chr((i+key)%26+97)})
    y=open(text,'r')
    y=y.read()
    encryption=open('cipher.txt','w')
    for i in y:
        if i in map:
            encryption.write(map[i])
        else:
            encryption.write(i)
    encryption.close()
    encryption=open('cipher.txt','r')
    return encryption.read()
    
