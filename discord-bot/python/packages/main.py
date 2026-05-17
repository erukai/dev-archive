#from: commit 01
#---

import math #using a built-in python module
import module #using a simple python file as a module
import numpy as np #using a 3rd party python package
import matplotlib.pyplot as plt #using a 3rd party python library

#using a variable from a module
number = module.num #return 25

#using a function from a module
name = module.get_name() #return "Eruka"

#using a class from a module
car = module.Car(brand="Volvo", color="red") #create a Car object with properties: {brand="Volvo", color="red"}
car.drive() #return "This red car is made by Volvo."

#------------------------

#math (module)
sqrt_num = math.sqrt(number) #return 5

#numpy (package)
np_array = np.array([1, 2, 3]) #return a NDArray object

#------------------------

#matplotlib (library) -> pyplot (module)

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)

plt.title("Simple Line Plot")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")

plt.show()