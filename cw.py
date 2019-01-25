



#Start with a main function and make each problem a function. Call those functions from your main function.
def main():
    # problem1()
    # problem2()
    #problem3()
    #problem4()

# these classes are created for the problem functions below
class Dog:
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender

    def printAll(self):
        print(self.name,'\n',self.breed,'\n',self.color,'\n',self.gender,)



class Product:
    def __init__(self, name='', price='', quantity=''):
        self.name= name
        self.price= price
        self.quantity= quantity
    def __str__(self):
        return (f'{self.name}, {self.price}, {self.quantity}')

#Create a class Dog. Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.

def problem1():

    dog1= Dog("Max","beagle","white and Brown","Male")
    Dog.printAll(dog1)

#Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.

def problem2():
    uI= ''
    while(uI!='='):
        uI= input("Enter something")

# In your main file create three Person objects. Change the weight and height of each one. Afterwards, print the BMI (body mass index) of each Person.
def problem3():
    peopleList=[{"height": 62, "weight": 140}, {"height": 73, "weight": 119}, {"height": 59, "weight": 180}]

    for x in peopleList:
        print('BMI: ', (x["weight"] / (x["height"] * x["height"])) * 703)

#Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#create an object of Product in your problem4 function and print all of it's attributes.
def problem4():

    product1 = Product()
    product2 = Product('Camera')
    product3 = Product('Magic Booster Pack ', '$8')
    product4 = Product('Silicone Tunnels', '$5', '3')

    print(product1)
    print(product2)
    print(product3)
    print(product4)











if __name__ == '__main__':
    main()