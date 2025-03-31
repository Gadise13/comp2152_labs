from heart import heart
# import heart

class Mammal:
    def __init__(self, age, heart):
        self.age = age
        self.heart = heart()
        
        
    def speak(self):
        print("Grr...")
        
    def __str__(self):
        return f"Mammal is {self.age} years old"
    
           