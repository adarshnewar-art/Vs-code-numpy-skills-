# You are given an array of temperature in Fahrenheit. Convert them all to Celsius and Kelvin using element-wise arithmetic , without using any loop
import numpy as np
n=np.array([32, 68, 100, 212])  # Example array of temperatures in Fahrenheit
# Convert to Celsius
Celsius = (n - 32) * 5/9 
# Convert to Kelvin
Kelvin = Celsius + 273.15 
print("Temperatures in Celsius:", Celsius )
print("Temperatures in Kelvin:", Kelvin)
