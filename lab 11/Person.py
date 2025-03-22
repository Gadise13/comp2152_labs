class Person:
    def __init__(self, name, age, height):
        self.__name = name  # Private variable
        self.__age = age    # Private variable
        self.__height = height  # Private variable
        self.public_prop = "I'm public"
        print("Constructing the Person object")

    def __del__(self):
        print("The garbage collector is automatically destroying the person object")


    # Magic getter/setter for 'name'
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Magic getter/setter for 'age'
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    # Magic getter/setter for 'height'
    @property
    def height(self):
        return self.__height  

    @height.setter
    def height(self, height):
        self.__height = height

   
# # Creating an instance of Person
# p1 = Person(name="Mark", age=20, height=6)

# # Accessing attributes
# print(p1.public_prop)

# # Using property-based getters and setters
# print(p1.name)  # Calls the @property method
#print(p1.__name)
# p1.name = "Anna"  # Calls the setter
# print(p1.name)

# p1.age = 25  # Calls the setter
# print(p1.age)
# #pl.name ="jake"
# #print(p1.name)
# #print(p1.get_name())


# print(p1.height)
# p1.height = 5.9  # Calls the setter
# print(p1.height)

# print("Script is ending")
