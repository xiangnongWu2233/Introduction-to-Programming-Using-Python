def mirror(str):
    map={'b':'d','d':'b','i':'i','l':'l','m':'m','n':'n','o':'o',
         'p':'q','q':'p','v':'v','w':'w','x':'x',}
    mir=''
    length=len(str)
    for i in range(length):
        if str[length-1-i] in map:
            mir+=map[str[length-1-i]]
        else:
            return 'INVAILD'
    return mir
