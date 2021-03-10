class Textfile:
    def __init__(self,file):
        self.name=file
                
    def occurrences(self):
        txt=open(self.name,'r')
        txt=txt.read()
        trans=str.maketrans(',.!?;:"\'`~-_$&@#%','                 ')
        txt.translate(trans)
        txt=txt.split()
        occu=dict()
        for i in txt:
            if i not in occu:
                occu.update({i:txt.count(i)})
        return occu
