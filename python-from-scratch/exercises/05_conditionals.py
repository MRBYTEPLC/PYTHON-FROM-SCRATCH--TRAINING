# =============================================================
# EXERCISE 05 — Conditionals (if / elif / else) 🔀
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - Making decisions in code with if / elif / else
#    - Comparison operators: ==, !=, >, <, >=, <=
#    - Logical operators: and, or, not
#    - Indentation: why spaces matter in Python
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  Conditionals let your program make DECISIONS.
#
#  Structure:
#     if   condition:          ← checked first
#         code block
#     elif other_condition:    ← checked if the first was False
#         code block
#     else:                    ← runs if NOTHING above was True
#         code block
#
#  COMPARISON operators (return True or False):
#   ==  equal to           5 == 5  → True
#   !=  not equal to       5 != 3  → True
#   >   greater than       5 > 3   → True
#   <   less than          5 < 3   → False
#   >=  greater or equal   5 >= 5  → True
#   <=  less or equal      3 <= 5  → True
#
#  LOGICAL operators:
#   and  → both conditions must be True
#   or   → at least one condition must be True
#   not  → reverses True to False and vice versa
#
#  ⚠️  INDENTATION: Python uses 4 spaces to define code blocks.
#      Everything inside an if MUST be indented (Thonny does it for you).
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

# --- Simple if/else ---
temperature = 35

if temperature > 30:                          # condition: hotter than 30?
    print("It's very hot! Drink water.")     # runs only if True
else:
    print("The temperature is comfortable.") # runs if False

# --- if / elif / else: multiple conditions ---
score = int(input("\nEnter a score (0-100): "))

if score >= 90:                               # 90 or more → A
    grade = "A — Excellent!"
elif score >= 80:                             # between 80 and 89 → B
    grade = "B — Good"
elif score >= 70:                             # between 70 and 79 → C
    grade = "C — Acceptable"
elif score >= 60:                             # between 60 and 69 → D
    grade = "D — Needs improvement"
else:                                         # below 60 → F
    grade = "F — Failed"

print(f"Score: {score} → Grade: {grade}")

# --- Logical operators: and, or, not ---
age    = int(input("\nEnter your age: "))
has_id = input("Do you have ID? (yes/no): ").lower()  # .lower() → lowercase

# and: BOTH conditions must be True
if age >= 18 and has_id == "yes":
    print("Access allowed.")
elif age >= 18 and has_id != "yes":
    print("You need to show your ID.")
else:
    print(f"Sorry, you must be 18. You are {age}.")

# --- not operator ---
is_raining = False
if not is_raining:                            # not False → True
    print("\nNo umbrella needed today!")

# --- Nested conditionals (if inside an if) ---
print()
day       = input("Is today a weekday or weekend? (weekday/weekend): ").lower()
time_hour = int(input("What hour is it? (0-23): "))

if day == "weekday":
    if time_hour < 8:                         # nested if
        print("Time to get up for school!")
    elif time_hour < 17:
        print("You should be in class.")
    else:
        print("Homework time!")
else:                                         # weekend
    if time_hour < 10:
        print("Sleeping in on the weekend!")
    else:
        print("Enjoy your free time!")

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Create a BMI (Body Mass Index) classifier:
# 1. Ask the user for weight (kg) and height (m)
# 2. Calculate BMI = weight / (height ** 2)
# 3. Classify using these rules:
#    BMI < 18.5          → "Underweight"
#    18.5 ≤ BMI < 25     → "Normal weight ✅"
#    25 ≤ BMI < 30       → "Overweight"
#    BMI ≥ 30            → "Obese"
# 4. Print the BMI with 2 decimal places and the category
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")
# ✏️ WRITE YOUR CODE HERE:
