class Entity:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def toString(self):
        print(f"Name: {self.name}\n ID: {self.ID}")