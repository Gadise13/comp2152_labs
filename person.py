from mammal import Mammal
class person(Mammal):
    def __init__(self, name, age, height):
        super().__init__(age)
        self.name = name
        self.heart = height
        
    def speak(self):
        print("Hello")  
        
    def __str__(self):
         return f"this  person's name is {self.name}.their heart is beating at{self.heart.bpm}bpm."  