# =============================================================
# EXERCISE 09 — Functions 🧩
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - Creating functions with def
#    - Parameters and arguments
#    - Returning values with return
#    - Default parameter values
#    - Why we use functions (reuse, organization, clarity)
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  A FUNCTION is a reusable block of code with a name.
#  You DEFINE it once, then CALL it as many times as needed.
#
#  Structure:
#     def function_name(parameter1, parameter2):
#         """Docstring: describes what this function does"""
#         code
#         return result          ← optional: sends a value back
#
#  PARAMETER: the variable in the function definition (placeholder)
#  ARGUMENT:  the actual value you pass when calling it (real data)
#
#  return sends a value BACK to wherever the function was called.
#  Without return, the function returns None automatically.
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

# --- Function with no parameters, no return ---
def greet():
    """Prints a simple greeting message."""       # docstring (documentation)
    print("Hello! Welcome to Python.")

greet()             # CALLING the function — parentheses are always required!
greet()             # call it again — that's the power of reusability!

# --- Function with parameters ---
def greet_person(name):
    """Greets a specific person by name."""
    print(f"Hello, {name}! Great to meet you.")

greet_person("Maria")            # argument: "Maria"
greet_person("Carlos")           # same function, different argument
greet_person("Ana")

# --- Function with multiple parameters ---
def add(a, b):
    """Returns the sum of two numbers."""
    result = a + b
    return result                # sends the sum back to the caller

sum_result = add(5, 3)           # stores the returned value
print(f"\n5 + 3 = {sum_result}")
print(f"10 + 7 = {add(10, 7)}") # use returned value directly inside print

# --- Default parameter values ---
def power(base, exponent=2):
    """Raises base to exponent. Default exponent is 2 (square)."""
    return base ** exponent

print(f"\n5 squared   = {power(5)}")       # uses default exponent=2 → 25
print(f"5 cubed     = {power(5, 3)}")     # overrides default → 125
print(f"2 to the 8  = {power(2, 8)}")     # 256

# --- Practical functions ---

def celsius_to_fahrenheit(celsius):
    """Converts a Celsius temperature to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def is_even(number):
    """Returns True if the number is even, False if odd."""
    return number % 2 == 0        # the expression itself evaluates to True/False

def get_grade(score):
    """Returns a letter grade for a numeric score (0-100)."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# --- Using the functions ---
temp_c = float(input("\nEnter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.1f}°F")

num = int(input("Enter a number: "))
print(f"{num} is even: {is_even(num)}")        # True or False

score = int(input("Enter a score: "))
print(f"Grade: {get_grade(score)}")

# --- Function that returns multiple values (as a tuple) ---
def stats(numbers_list):
    """Returns the minimum, maximum and average of a list."""
    minimum = min(numbers_list)
    maximum = max(numbers_list)
    average = sum(numbers_list) / len(numbers_list)
    return minimum, maximum, average   # returns three values at once

data = [45, 82, 67, 90, 55, 78]
low, high, avg = stats(data)           # UNPACKING: 3 values into 3 variables
print(f"\nStats → Min: {low}  Max: {high}  Avg: {avg:.1f}")

# --- Functions calling other functions ---
def bmi_category(weight_kg, height_m):
    """Calculates BMI and returns the numeric value and category."""
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category               # returns two values

w = float(input("\nWeight (kg): "))
h = float(input("Height (m): "))
bmi_val, bmi_cat = bmi_category(w, h)
print(f"BMI: {bmi_val:.2f} → {bmi_cat}")

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Write 3 functions:
# 1. rectangle_area(width, length) → returns the area
# 2. circle_area(radius)           → returns the area (use π = 3.14159)
# 3. is_prime(number)              → returns True if prime, False otherwise
#    (A prime number is only divisible by 1 and itself)
#
# Then build a small menu asking the user what they want to calculate
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")
# ✏️ WRITE YOUR CODE HERE:
