import pickle
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."


s = Student('Sinchan',10)

with open('students.txt', 'wb') as f:
    pickle.dump(s, f)
with open('students.txt', 'rb') as f:
    loaded_data = pickle.load(f)
print(loaded_data.name)
print(loaded_data.hi())