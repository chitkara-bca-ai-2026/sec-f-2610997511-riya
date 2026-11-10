
import math

num = int(input("Enter a number: "))
exp = int(input("Enter the exponent: "))
deci = float(input("Enter a decimal measurement: "))

power = math.pow(num, exp)
sqroot = math.sqrt(num)
ceiling = math.ceil(deci)
floor = math.floor(deci)

print("===========================================")
print("      ENGENEERING CALCULATION TOOL      ") 
print("===========================================")

print("Number entered:", num)
print("Exponent entered:", exp)
print("Decimal measurement entered:", deci)

print("--------------------RESULTS----------------------")
print("Value                  : ", num)
print("Exponent               : ", exp)
print("Power                  : ", power)
print("Square Root            : ", sqroot)
print("Ceiling of Decimal     : ", ceiling)
print("Floor of Decimal       : ", floor)
print("=================================================")
