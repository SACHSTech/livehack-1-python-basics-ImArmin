'''
-------------------------------------------------------------------------------------------
Name: problem1.py
Purpose: Convert celcius into fahrenheit.

Author: Armin

Created: date 2020-12-07
-------------------------------------------------------------------------------------------
'''

print(" Welcome to the Celcius to Fahrenheit converter ")

#get celcius
celcius = float(input("Enter the temperature in celcius: "))

# compute farhenheit
fahrenheit = (9/5 * celcius) + 32

# output farhenheit
print("The temperature " + str(celcius) + " in celcius =" + " the temperature " + str(fahrenheit) + " in fahrenheit.")