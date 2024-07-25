

class Animal:
    def __init__(self):
        self.numEyes=2
    
    def breath(self):
         print("Inhale Exhale")   
         

class Fish:
    def __init__(self,name):
        self.fins=True
        self.name="Nemo"
    
    def swim(self):
        print("Moving in water")
        

fish=Fish();     
fish.swim()   
