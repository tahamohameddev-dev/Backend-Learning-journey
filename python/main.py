# ####################################
# 01. SYNTAX & PRINTING
# ####################################

print("hello world")

print(2026 + 4)

# ####################################
# 02. VARIABLES & DATA TYPES
# ####################################

name = "Tom"
age = 22
is_Developer = True

print(name)

# ####################################
# 03. WORKING WITH STRINGS & NUMBERS
# ####################################

phrase = "Backend Academy"

print(phrase.upper())
print(phrase.lower())

print(phrase.isupper())
print(phrase.islower())

print(len(phrase))

print(phrase.index("B"))
print(phrase.replace("Academy","Lerning"))

# NUMBERS

my_num = 5
print(str(my_num) + " my favorite number")

print(3 + 4)
print(3 - 4)
print(3 / 4)
print(3 * 4)

print(abs(-5))
print(pow(4, 2))
print(max(9, 8))
print(min(4, 7))
print(round(7.5))

# ####################################
# 0.4 GITTING INPUT & BASIC CALCULATOR
# ####################################

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " your age " + age + "!")


# Calculator

num_1 = input("Enter number: ")
num_2 = input("Enter number: ")

Calculation = int(num_1) + int(num_2)
print(Calculation)

# ####################################
# 0.5 LISTS & LIST FUNCTIONS & TUPELS 
# ####################################

skills = ["Python", "Linux", "Git"]
skills.append("Databases")
skills.insert(1,"Docker")
skills.remove("Git")
# skills.clear()
print(skills )
print(skills.index("Python"))
print(skills.count("Linux"))

skills2 = skills.copy()

print(skills2)

# Tuples

user = [("ahmed", 25), ("sara", 30), ("ali", 22)]

# ####################################
# 0.6 FUNCTIONS & RETURN STATEMENT
# ####################################

def say_hi(name, age):
    print("hello " + name + ", you are age " + str(age))

say_hi("Tom", 19)

# RETURN STATEMENT


def cube(num):
    return num*num*num

print(cube(3))

# ####################################################
# 0.7 IF STATEMENTS & COMPARISONS & BETTER CALCULATOR
# ####################################################

age = 18
is_Developer = True 

if age >= 18 and is_Developer:
    print("Welcome to the Backend world, Tom!")
else:
    print("Keep learning!")

# Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
Calculations = max_num(6, 8, 6)

print(Calculations)

# BETTER CALCULATOR

num1 = float(input("Enter Number: "))
op = input("Select an icon>> (+, -, *,/): ")
num2 = float(input("Enter Numper: "))
def Calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Error Select an icon>> (+, -, *,/): "

Calculation = Calculator(num1, op, num2)

print(Calculation)


# ####################################
# 0.8 Dictionaries
# ####################################

months_dict = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

print(months_dict["nov"])


# ####################################
# 0.9 WHILE LOOP & WHILE LOOP CALCULATOR
# ####################################

# WHILE LOOP

i = 1
while i <= 10:
    print(i)
    i = i +1

# WHILE LOOP CALCULATOR

def Calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Error Select an icon>> (+, -, *,/): "

user_choice = "y"
while user_choice == "y":
    
    num1 = float(input("Enter Number: "))
    op = input("Select an icon>> (+, -, *,/): ")
    num2 = float(input("Enter Numper: "))

    Calculation = Calculator(num1, op, num2)
    print(Calculation)
    user_choice = input("Do you need continuation (y/n): ").lower()
    print("-"* 20)

print("Goodbye!")


# ####################################
# 0.10 FOR LOOPS & EXPONENT FUNCTION
# ####################################

for i in range(3):
    print(i)

#  EXPONENT FUNCTION

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))

# ####################################
# 0.11 2D LISTS
# ####################################

# 2D LISTS
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in number_grid:
    for col in row:
        print(col)


# ####################################
# 0.12 TRY / EXCEPT
# ####################################

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")

# ####################################
# 0.13 READING & WRITING FILES
# ####################################

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# WRITING FILES

employee_file = open("employees.txt", "a") 
employee_file.write("\nTaha - Backend Engineer")
employee_file.close()

# ############################################
# 0.14 MODULES, CLASSES & OBJECTS, INHERITANCE
# ############################################

import datetime
current_time = datetime.datetime.now()

# Classes & Objects


class phone:
    def __init__(self, type, color, is_android):
        self.type = type
        self.color = color
        self.is_android = is_android

# INHERITANCE


    def is_infinix(self):
        if self.type == "infinix":
            return True
        else:
            return False

type1 = phone("relmy", "read", True)
type2 = phone("iphone", "black", "False")
print(type1.is_android)
print(type2.is_android)
print(type1.is_infinix())




# ####################################
# 0.15 
# ####################################





