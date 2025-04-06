class Dog:
    def speak(self):
        return "Woof"
        
class Cat:
    def speak(self):
        return "Meow"
        
def animal_sound(animal):
    return animal.speak()
    
    
dog = Dog()
cat = Cat()

print(animal_sound(dog)) #Woof
print(animal_sound(cat)) #Meow
