class Textfile:
    def __init__(self,file):
        self.name=file
                
    def average(self):
        txt=open(self.name,'r')
        txt=txt.readlines()
        numbers=[]
        trans=str.maketrans(',.!?;:"\'`~-_$&@#%','                 ')
        for i in txt:
            line=i.translate(trans)
            numbers.append(len(line.split()))
        numbers.sort()
        return sum(numbers)/len(numbers), numbers[len(numbers)-1], numbers[0]
