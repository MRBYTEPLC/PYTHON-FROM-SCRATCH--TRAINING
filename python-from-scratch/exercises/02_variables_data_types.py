# =============================================================
# EXERCISE 02 — Variables and Data Types 📦
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - What a variable is and how to create one
#    - The 4 basic data types: int, float, str, bool
#    - How to check a variable's type using type()
#    - f-strings to display variables inside text
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  A VARIABLE is like a labeled box where you store a value.
#  You CREATE a variable by writing:  name = value
#  The = sign is the ASSIGNMENT operator (it stores the value).
#
#  Python has 4 basic DATA TYPES:
#
#  int   → whole numbers           example: 10, -3, 0
#  float → decimal numbers         example: 3.14, -0.5, 2.0
#  str   → text (string)           example: "hello", 'yes'
#  bool  → True or False ONLY      example: True, False
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

# --- int (integer): whole numbers, no decimals ---
age = 15                        # stores the integer 15 in variable called age
temperature = -8                # integers can be negative
year = 2025                     # year is stored as int

# --- float: numbers with a decimal point ---
height = 1.72                   # meters, stored as float
price = 19.99                   # currency values use float
pi_approx = 3.14159             # mathematical constant approximation

# --- str (string): text between quotes ---
name = "Maria"                  # double quotes work
city = "Chicago"                # single quotes also work: 'Chicago'
greeting = "Hello, how are you?" # spaces are allowed inside strings

# --- bool (boolean): only two possible values ---
is_student = True               # capital T required — True, not true
has_homework = False            # capital F required — False, not false

# ── DISPLAYING VARIABLES ─────────────────────────────────────

# Method 1: pass the variable directly to print()
print(age)                      # prints: 15
print(name)                     # prints: Maria

# Method 2: f-string (f before the quote lets you embed variables)
# Any variable inside { } gets replaced with its value
print(f"My name is {name} and I am {age} years old.")
print(f"I live in {city}. Height: {height} m")
print(f"Am I a student? {is_student}")

# ── CHECKING THE TYPE ────────────────────────────────────────

# type() returns the data type of any variable
print(type(age))                # <class 'int'>
print(type(height))             # <class 'float'>
print(type(name))               # <class 'str'>
print(type(is_student))         # <class 'bool'>

# ── CHANGING A VARIABLE ──────────────────────────────────────

# Variables can be reassigned at any time
score = 0                       # score starts at 0
print(f"Initial score: {score}")
score = 100                     # now score is 100
print(f"New score: {score}")

# You can also do math with the current value
score = score + 50              # take old value, add 50, store back
print(f"After bonus: {score}")  # prints 150

# Shorthand: score += 50  means the same as  score = score + 50
score += 25
print(f"Final score: {score}")  # prints 175

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Create the following variables with YOUR real data:
#   your_name    (str)  → your full name
#   your_age     (int)  → your age
#   your_height  (float)→ your height in meters (e.g. 1.65)
#   like_python  (bool) → True or False
#
# Then print an introduction using f-strings like this:
#   "Hi, I am [name], I am [age] years old, I am [height]m tall."
#   "Do I like Python? [answer]"
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")

# ✏️ WRITE YOUR CODE HERE:
your_name = "YOUR_NAME"                 # replace with your name
your_age = 0                            # replace with your age
your_height = 0.0                       # replace with your height
like_python = True                      # True or False

print(f"Hi, I am {your_name}, I am {your_age} years old, I am {your_height}m tall.")
print(f"Do I like Python? {like_python}")
