#class is the blueprint of the object.
class Student:
    #Properties/Attributes
    #inbuilt function
    def __init__(self,name,age,grade,hobby):
        self.name=name
        self.age=age
        self.grade=grade
        self.hobby=hobby
        self.intro= " "
        
    #Functions
    def displayDetails(self):
        print("The details of the student")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grade:",self.grade)
        print("Hobby:",self.hobby)

    def introduction(self):
        self.intro=input("Tell me about yourself:")
        print(self.intro)

#Creating Object
s1=Student("John",27,"78th grade","Riding a mole")
s1.displayDetails()
s1.introduction()

s2=Student("Pizza",9,"18th grade","Shooting pebbles")
s2.displayDetails()
s2.introduction()

s3=Student("Slide",89,"8723th grade","Looking at earth")
s3.displayDetails()
s3.introduction()