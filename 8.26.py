class Textfile:
    def __init__(self,file):
        self.name=file
                
    def words(self):
        txt=open(self.name,'r')
        txt=txt.read()
        trans=str.maketrans(',.!?;:"\'`~-_$&@#%','                 ')
        txt.translate(trans)
        txt=list(set(txt.split()))
        return txt
