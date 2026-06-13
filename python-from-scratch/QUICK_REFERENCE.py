# =============================================================
# 📄 QUICK REFERENCE — Python from Scratch
# =============================================================
# Keep this file handy! It's your "cheat sheet" whenever you
# forget how to write something. Refer to it anytime!
# =============================================================

# ─── DATA TYPES ──────────────────────────────────────────────
integer = 10            # int    → whole numbers
decimal = 3.14          # float  → numbers with decimal point
text    = "hello"       # str    → string (text)
logical = True          # bool   → True or False only

# ─── OUTPUT / INPUT ──────────────────────────────────────────
print("Hello")                        # displays on screen
print(f"Value: {integer}")            # f-string with variable
name = input("What is your name? ")   # waits for user to type
age  = int(input("Age: "))            # converts input to integer
height = float(input("Height: "))     # converts input to float

# ─── TYPE CONVERSION ─────────────────────────────────────────
int("25")           # "25"  → 25
float("3.5")        # "3.5" → 3.5
str(100)            # 100   → "100"

# ─── ARITHMETIC OPERATORS ────────────────────────────────────
# +   addition           10 + 3  = 13
# -   subtraction        10 - 3  = 7
# *   multiplication     10 * 3  = 30
# /   division           10 / 3  = 3.333...
# //  floor division     10 // 3 = 3
# %   modulo (remainder) 10 % 3  = 1
# **  exponentiation     2 ** 8  = 256

# ─── COMPARISON OPERATORS ────────────────────────────────────
# ==   equal to          5 == 5  → True
# !=   not equal to      5 != 3  → True
# >    greater than      5 > 3   → True
# <    less than         3 < 5   → True
# >=   greater or equal  5 >= 5  → True
# <=   less or equal     3 <= 5  → True

# ─── LOGICAL OPERATORS ───────────────────────────────────────
# and  → both conditions must be True
# or   → at least one condition must be True
# not  → reverses True/False

# ─── CONDITIONALS ────────────────────────────────────────────
x = 10
if x > 5:
    print("greater than 5")
elif x == 5:
    print("equal to 5")
else:
    print("less than 5")

# ─── FOR LOOP ────────────────────────────────────────────────
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):        # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8
    print(i)

my_list = ["a", "b", "c"]
for item in my_list:         # iterate over a list
    print(item)

for idx, item in enumerate(my_list):  # with index
    print(idx, item)

# ─── WHILE LOOP ──────────────────────────────────────────────
counter = 0
while counter < 5:
    print(counter)
    counter += 1

while True:                  # controlled infinite loop
    user_input = input("Type 'quit' to stop: ")
    if user_input == "quit":
        break                # exits the while loop

# ─── LISTS ───────────────────────────────────────────────────
my_list = [1, 2, 3, 4, 5]
my_list[0]               # first element  → 1
my_list[-1]              # last element   → 5
my_list[1:3]             # slice          → [2, 3]
len(my_list)             # number of items → 5

my_list.append(6)        # add to the end
my_list.insert(0, 0)     # insert at position 0
my_list.remove(3)        # remove the value 3
my_list.pop()            # remove and return last item
my_list.sort()           # sort ascending
my_list.sort(reverse=True)  # sort descending
sum(my_list)             # sum all elements
max(my_list)             # maximum value
min(my_list)             # minimum value
3 in my_list             # is 3 in the list? → True/False

# ─── FUNCTIONS ───────────────────────────────────────────────
def greet(name, greeting="Hello"):     # default parameter value
    """Prints a greeting."""           # docstring
    print(f"{greeting}, {name}!")

def add(a, b):
    return a + b                       # returns a value

greet("Ana")                           # uses default greeting
greet("Luis", "Good morning")          # overrides the default
result = add(5, 3)                     # stores the return value

# ─── MODULE: random ──────────────────────────────────────────
import random

random.randint(1, 10)         # random integer between 1 and 10
random.random()               # random float between 0.0 and 1.0
random.uniform(1.0, 5.0)      # random float between 1.0 and 5.0
random.choice([1, 2, 3])      # pick one item at random from list
random.shuffle(my_list)       # shuffle the list (modifies original)
random.sample(my_list, 2)     # pick 2 unique items at random

# ─── MODULE: math ────────────────────────────────────────────
import math

math.pi                       # 3.141592653589793
math.e                        # 2.718281828459045
math.sqrt(16)                 # square root → 4.0
math.pow(2, 10)               # 2^10 → 1024.0
math.floor(4.9)               # round DOWN → 4
math.ceil(4.1)                # round UP   → 5
math.log10(100)               # base-10 log → 2.0
math.sin(math.radians(90))    # sin of 90°  → 1.0
math.cos(math.radians(0))     # cos of 0°   → 1.0
abs(-7)                       # absolute value → 7 (built-in, no math needed)

# ─── NUMBER FORMATTING IN f-strings ─────────────────────────
value = 3.14159
print(f"{value:.2f}")         # 2 decimal places → 3.14
print(f"{value:.4f}")         # 4 decimal places → 3.1416
print(f"{100:05d}")           # pad with zeros   → 00100
print(f"{1000000:,}")         # thousands separator → 1,000,000

# ─── THONNY KEYBOARD SHORTCUTS ───────────────────────────────
# F5           → Run the program
# Ctrl+Z       → Undo
# Ctrl+S       → Save
# Ctrl+/       → Comment / uncomment selected line(s)
# Tab          → Indent
# Shift+Tab    → Remove indentation

# ─── COMMON ERRORS ───────────────────────────────────────────
# SyntaxError       → Typo in code (missing : " ) etc.)
# NameError         → Used a variable that doesn't exist yet
# TypeError         → Operation between incompatible types (str + int)
# ValueError        → Failed conversion: int("hello") — not a number
# IndexError        → Index out of range on a list
# ZeroDivisionError → Divided by zero
