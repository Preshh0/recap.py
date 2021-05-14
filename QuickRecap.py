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

gender1 = "Male"#input("Enter Gender: ")
gender2 = "Female"#input("Enter Gender: ")

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

'''Lists'''


Animals = ["Dog", "Cats", "Birds", "Reptiles", "Fishes"]
file = Animals[1]
Animals.append("Whale")
#Or#
Animals += ["Dolphins"]

Animals.remove("Dolphins")
#Animals.insert("Test", 1 ) Find out what is wrong, later.
#Animals.sort() # this method doesn't work if there is a mixture of both integers and strings

print("Cats" in Animals)
print(Animals)
print(len(Animals))
print(sorted(Animals, key=str.lower))
print(file)

'''Tuples'''
names = ("Roger", "Syd", "John", "Mike", "Felix")
print(len(names))
print(sorted(names))#USING sORTED
newTuple = names + ('Vanille', 'Vivian')
print("Roger" in names)
print(names[0])
print(names[0:1])
print (newTuple)

'''Dictionaries'''
Animalia = { "Name": "Dog",
             "Age": 2,
             "Height": 5
            }

print(Animalia)