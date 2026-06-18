class Mobile:
    def __init__(self, company, ram, storage):
        self.company = company
        self.ram = ram
        self.storage = storage
 
    def display(self):
        print(self.company)
        print(self.ram)
        print(self.storage)
 
 
m = Mobile("Samsung", "8GB", "128GB")
 
m.display()