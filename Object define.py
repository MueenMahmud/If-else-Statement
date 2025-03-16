class eub:
    def __init__ (self, name, id, age):
        
        self.name = name
        self.id = id
        self.age = age
    def myfunction(abc):
        print("My name is : " + abc.name)
        print("Your id is : " + str(abc.id))
        print("Your age is : " + str(abc.age))
        
    
p1 = eub("Md. Mueein Mahmud", 2301057, 25)
p1.myfunction()
