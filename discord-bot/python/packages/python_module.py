#from: commit 01

num = 25

def get_name():
    return "Eruka"

class Car:
    category = "vehicle"

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        return print(f"This {self.color} car is made by {self.brand}.")