# =============================================================
# EXERCISE 03 — User Input ⌨️
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - How to ask data from the user with input()
#    - Why input() always returns a string
#    - How to convert types: int(), float(), str()
#    - Building a simple interactive program
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  input() pauses the program and waits for the user to type
#  something and press Enter.
#
#  IMPORTANT: input() ALWAYS returns a string (str), even if
#  the user types a number like 25.
#
#  To work with numbers, you must CONVERT (cast) the string:
#    int("25")    → 25      (whole number)
#    float("3.5") → 3.5     (decimal number)
#    str(25)      → "25"    (back to text)
#
#  If you try to do math on a string, Python gives a TypeError!
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

# --- Basic input ---
# input("message") shows the message then waits for typing
user_name = input("What is your name? ")    # stores whatever the user types
print(f"Hello, {user_name}!")               # greets the user

# --- input always returns a string ---
age_text = input("How old are you? ")       # user types e.g. 15
print(type(age_text))                       # shows: <class 'str'>  — it's text!

# --- Converting string to integer ---
# int() converts text to a whole number so we can do math with it
age_number = int(age_text)                  # "15" → 15
next_year_age = age_number + 1              # math works now!
print(f"Next year you will be {next_year_age} years old.")

# --- Converting string to float ---
height_text = input("Your height in meters (e.g. 1.70): ")
height = float(height_text)                # "1.70" → 1.70
height_cm = height * 100                   # convert meters to centimeters
print(f"Your height is {height_cm:.1f} cm")
# :.1f inside { } means: show 1 decimal place

# --- Converting in one line (the common way) ---
# You can nest int() or float() directly around input()
weight = float(input("Your weight in kg: "))   # read AND convert in one step
bmi = weight / (height ** 2)                    # BMI formula: weight / height²
print(f"Your approximate BMI is: {bmi:.2f}")    # 2 decimal places

# ── MINI PROGRAM: Simple Receipt ─────────────────────────────

print()
print("=== MINI STORE ===")
product  = input("Product name: ")         # text — no conversion needed
quantity = int(input("Quantity: "))        # must be whole number
price    = float(input("Price per unit: $")) # can have decimals

total = quantity * price                   # calculate total

print()
print("=== RECEIPT ===")
print(f"Product   : {product}")
print(f"Quantity  : {quantity}")
print(f"Unit price: ${price:.2f}")
print(f"TOTAL     : ${total:.2f}")

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Create a program that:
# 1. Asks the user for their name (str)
# 2. Asks for a temperature in Celsius (float)
# 3. Converts it to Fahrenheit with the formula: F = (C × 9/5) + 32
# 4. Prints: "Hello [name]! [C]°C equals [F]°F"
#
# Example:
#   Hello Ana! 25°C equals 77.0°F
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")

# ✏️ WRITE YOUR CODE HERE:
