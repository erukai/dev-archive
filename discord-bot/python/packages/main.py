#committed: 27/11/2025
#---

import math #using a built-in python module
from my_package import my_module #using a module inside a local python package

import numpy as np #using a 3rd party python package (library)
import matplotlib.pyplot as plt #using a 3rd party python package (library)

#using a variable from a module
number = my_module.num #return 25

#using a function from a module
name = my_module.get_name() #return "Eruka"

#using a class from a module
car = my_module.Car(brand="Volvo", color="red") #create a Car object with properties: {brand="Volvo", color="red"}
car.drive() #return "This red car is made by Volvo."

#------------------------

#math (module) > sqrt() (function)
sqrt_num = math.sqrt(number) #return 5

#numpy (package) > array() (function)
np_array = np.array([1, 2, 3]) #return a NDArray object

#------------------------

#matplotlib (package) > pyplot (module)

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)

plt.title("Simple Line Plot")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")

plt.show()