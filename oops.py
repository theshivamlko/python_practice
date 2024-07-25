

class Animal:
    def __init__(self):
        self.numEyes=2
        print("Animal init")
    
    def breath(self):
         print("Animal Inhale Exhale")   
         

class Fish(Animal):
    def __init__(self,name):
        super().__init__()
        self.fins=True
        self.name="Nemo"
        print("Fish init")
        

    def swim(self):
        print(f"Fish {self.name} Moving in water {self.fins}")
     
    def breath(self):
        super().breath()
        print("Fish Breath")   
   

fish=Fish("Nemo");     
fish.swim()   
fish.breath()   
