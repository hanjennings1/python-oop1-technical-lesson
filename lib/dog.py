# Create Class...
class Dog:
    def __init__(self, name, breed, age, last_checkup=None):
        self.name = name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup

    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date

    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}!")

    #fido.age
    def get_age(self):
        return self._age

    # fido.age = 10
    def set_age(self, value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not valid age.")
    age = property(get_age, set_age)

# Create Dogs in Dog Class...
fido = Dog("fido", "Golden Retriever", 3, "05/12/2023")
clifford = Dog(
    name = "Clifford",
    age = 2,
    breed = "Big Red"
)

fido.age = 7
print(fido.age)

# print(fido.age)      #3
# fido.birthday_celebration()
# print(fido.age)      #4
 
# print(clifford.last_checkup)        #None
# clifford.checkup("03/02/2026")
# print(clifford.last_checkup)        #03/02/2026

# balto = Dog("Balto", "Husky", "Not an age")
# steele = Dog("steele", "Husky", -10)
