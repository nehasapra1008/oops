class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print( self.brand)
        print( self.model)
        print( self.year)


# Create an object
car = Car("Toyota", "Camry", 2020)

# Call the display method
car.display()