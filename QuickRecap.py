#(>>>) stands for Read-Evaluate-Print-Loop
print ("Hello World")
'''Variables'''

Greetings = "Hey, How are you?"
print(Greetings)

'''Operators'''

sum = 2 + 2
print(sum)
subtraction = 4-2
print(subtraction)
division = 3/4
print(division)
modulus = 3%3
print(modulus)
multiplication = 2*3
print(multiplication)
exponentiation = 3**4
print("Exponentiation:",exponentiation)
Floor = 3//3
print(Floor)
#- as a unary operator
print(-4)

'''Comparison'''
a = 4
b = 8

print(a == b)
print (a != b)
print(a > b)
print( a<= b)
age = 1
print(type(age) == int)
#Converting from float to int
fraction = 0.1
intFraction = int(fraction)
print(intFraction)
'''not, or, and'''

gender1 = input("Enter Gender: ")
gender2 = input("Enter Gender: ")

if gender1 and gender2 != "Male":
    print("Not the same gender.")
elif gender1 or gender2 == "Female":
    print("One is definitely female.")
else:
    print("It is neither.")
    
output = len(gender1)
print("Gender One is: ", output)
'''The ternary Operator'''
def is_adult(age):
    return True if age > 18 else False

'''multiline strings(use three quotes)'''

print("""Roger is


   8
   
   
   
   years old.""")