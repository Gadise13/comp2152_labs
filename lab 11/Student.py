from person import Person  #import

class Student(Person):  # Capitalized class name
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)  # Pass arguments properly
        self.major = major
        print("This time it's a student object")

    def __del__(self):  # Moved outside __init__
        print("Deleting the student object")


# Creating an instance of Student
s1 = Student("Maria", 22, 6, "Computer Science")

# Accessing attributes
print(s1.name)
print(s1.major)
