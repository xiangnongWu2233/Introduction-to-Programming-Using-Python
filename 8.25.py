class Textfile:
    def __init__(self,file):
        self.name=file
        
    def nchars(self):
        txt=open(self.name,'r')
        txt=txt.read()
        trans=str.maketrans(',.!?;:"\'`~-_$&@#%','                 ')
        txt.translate(trans)
        return len(txt)
    
    def nwords(self):
        txt=open(self.name,'r')
        txt=txt.read()
        trans=str.maketrans(',.!?;:"\'`~-_$&@#%','                 ')
        txt.translate(trans)
        txt=txt.split()
        return len(txt)
    
    def nlines(self):
        txt=open(self.name,'r')
        txt=txt.readlines()
        return len(txt)
    
    def read(self):
        txt=open(self.name,'r')
        print(txt.read())
    
    def readlines(self):
        txt=open(self.name,'r')
        return txt.readlines()

    def grep(self, target):
        txt=open(self.name,'r')
        txt=txt.readlines()
        for i in range(len(txt)):
            if target in txt[i]:
                print('{:}: {:}'.format(i,txt[i]),end='')
