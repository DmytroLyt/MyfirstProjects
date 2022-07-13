# Temperature_Converter.py
# MyfirstProjects

# Created by Dmytro Lytvynenko 6/19/2022
# This project convert Celsius temperature to Fahrenheit and opposite way



def temperature():
    convert_type = input('If you want to convert F into C, put F, if C into F, put C: ')
    degree = int(input("Put the degree that need to be converted: "))
    cel = ((9/5)*(degree+32))
    far = ((5/9)*(degree-32))
    if convert_type == "F":
        return far
    else:
        return cel
print(temperature())
