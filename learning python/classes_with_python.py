


#function to demostrate Dictionery Data structure. 
def DictioneryFun(name, age):
    
    my_dict = {"my_name":name,
            "my_age":age}
    
    my_name1 = my_dict["my_name"]
    myAge = my_dict["my_age"]
    print(">> My name is",my_name1,"\b.","\n","\b>> I'm ", myAge, "years old." )


inputName = input("Enter your name >>")
inputAge = input("Enter your age >>")
DictioneryFun(inputName, inputAge)

