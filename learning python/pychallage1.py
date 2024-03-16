import html_in_python
"""Data persists when it outlives the program that created it. We can use files to persist data by
writing the output of our programs to a file. Write a program that collects data from a user—
and saves it to a file—so the data persists."""

#Answer
"""getAge = input("Enter your age >>")
getFirstName = input("Enter your First name>>")
getLastName = input("Enter your last name..")"""

"""
myFile = open("my_new_py.txt",'w')
myFile.write(getAge)
myFile.write(getFirstName)
myFile.write(getLastName)
myFile.close()"""

#html_in_python.printweb()

class Car:
    
    
    def __init__(self,modelNum,namE,coloR):
        self.modelNumber = modelNum
        self.namE = namE
        self.coloR = coloR
        
        
    
    

    def printV(self):
        print(self.modelNumber)
        
        print(self.namE)
        
        print(self.coloR)
        
bmw1 = Car("x5","BMW japan","black")

print("the details of the first car are >>")
print(bmw1.coloR,"\n",bmw1.modelNumber,"\n",bmw1.namE)

bmw2 = Car("x7","Bmw singapore", "red")

print("\n\nthe details of second car is >>")
print(bmw2.modelNumber,bmw2.namE,bmw2.coloR)

    