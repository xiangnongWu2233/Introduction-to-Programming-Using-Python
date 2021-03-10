class Worker:
    def __init__(self, name, wage):
        self.name=name
        self.wage=wage
    def changeRate(self, wage):
        self.wage=wage
    def pay(self, time):
        print('Not Implemented')

class HourlyWorker(Worker):
    def pay(self, time):
        if time<=40:
            return time*self.wage
        else:
            return self.wage*40+(time-40)*self.wage*2
        
class SalariedWorker(Worker):
    def pay(self, time=None):
        return 40*self.wage
