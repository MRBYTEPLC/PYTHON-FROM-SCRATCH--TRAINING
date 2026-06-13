# =============================================================
# EXERCISE 10 — Modules: random and math 📦🎲
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - What a module is and why they exist
#    - Importing modules with import
#    - Module random: random numbers, shuffling, choosing
#    - Module math: advanced mathematical functions
#    - Combining everything learned in the course
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  A MODULE is a file containing Python code (functions, variables)
#  that you can import and use in your own programs.
#
#  Python ships with many built-in modules called the "Standard Library".
#  You do NOT need to install them — just import them!
#
#  Ways to import:
#    import math                  → use as math.sqrt(), math.pi
#    from math import sqrt, pi   → use as sqrt(), pi  (no prefix needed)
#    import math as m             → use as m.sqrt()   (shorter alias)
#
#  MODULE: random
#    Provides functions to generate random numbers and make random choices.
#    Useful for: games, simulations, shuffling, testing.
#
#  MODULE: math
#    Provides advanced mathematical functions and constants.
#    Useful for: geometry, trigonometry, logarithms, rounding.
#
# ─────────────────────────────────────────────────────────────

# ── IMPORTING MODULES ────────────────────────────────────────

import random      # import the entire random module
import math        # import the entire math module

# ── RANDOM MODULE ────────────────────────────────────────────

print("=== random MODULE ===\n")

# random.randint(a, b) → random INTEGER between a and b (both included)
dice_roll = random.randint(1, 6)
print(f"Rolling a die: {dice_roll}")

# random.random() → random FLOAT between 0.0 and 1.0
probability = random.random()
print(f"Random probability: {probability:.4f}")

# random.uniform(a, b) → random FLOAT between a and b
temperature = random.uniform(15.0, 35.0)
print(f"Random temperature: {temperature:.2f}°C")

# random.choice(sequence) → picks ONE random item from a list
colors = ["red", "green", "blue", "yellow", "purple"]
chosen_color = random.choice(colors)
print(f"Random color chosen: {chosen_color}")

# random.choices(sequence, k=n) → picks n items (repetition allowed)
lottery = random.choices(range(1, 50), k=6)
print(f"Lottery numbers: {sorted(lottery)}")

# random.shuffle(list) → shuffles a list IN PLACE (modifies it!)
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)            # rearranges the list in random order
print(f"Shuffled deck (first 5): {cards[:5]}")

# random.sample(sequence, k) → picks k UNIQUE items (no repetition)
team = ["Alice", "Bob", "Carlos", "Diana", "Emma", "Frank"]
selected = random.sample(team, 3)        # pick 3 unique people
print(f"Randomly selected team: {selected}")

# random.seed(n) → sets starting point so results are REPRODUCIBLE
# Useful for testing: same seed → same "random" sequence every run
random.seed(42)                          # always produces the same sequence
print(f"Seeded random: {random.randint(1, 100)}")

# ── MATH MODULE ──────────────────────────────────────────────

print("\n=== math MODULE ===\n")

# math constants
print(f"Pi (π)     = {math.pi}")           # 3.141592653589793
print(f"Euler (e)  = {math.e}")            # 2.718281828459045
print(f"Infinity   = {math.inf}")          # ∞

# math.sqrt(x) → square root of x
print(f"\n√144       = {math.sqrt(144)}")  # 12.0
print(f"√2         = {math.sqrt(2):.6f}") # 1.414214

# math.pow(x, y) → x to the power y (returns float, unlike **)
print(f"3^4        = {math.pow(3, 4)}")   # 81.0

# abs() → absolute value (built-in, no math prefix needed)
print(f"|−15|      = {abs(-15)}")          # 15

# Rounding functions
x = 4.7
print(f"\nmath.floor({x}) = {math.floor(x)}")   # rounds DOWN → 4
print(f"math.ceil({x})  = {math.ceil(x)}")      # rounds UP   → 5
print(f"round({x})      = {round(x)}")           # standard rounding → 5

# math.log() → natural logarithm (base e)
print(f"\nln(1)      = {math.log(1)}")           # 0.0
print(f"log10(100) = {math.log10(100)}")         # 2.0
print(f"log2(8)    = {math.log2(8)}")            # 3.0

# Trigonometry — angles must be in RADIANS
# math.radians() converts degrees → radians
angle_deg = 90
angle_rad = math.radians(angle_deg)
print(f"\nsin(90°)   = {math.sin(angle_rad):.4f}")   # 1.0
print(f"cos(90°)   = {math.cos(angle_rad):.4f}")     # ~0.0
print(f"tan(45°)   = {math.tan(math.radians(45)):.4f}")  # 1.0

# ── PRACTICAL COMBINATION: Final Guessing Game ───────────────

print("\n=== GUESSING GAME WITH RANDOM ===")
secret_number = random.randint(1, 20)    # random generates the secret number
max_attempts  = 5
attempts      = 0

print(f"Guess the number between 1 and 20. You have {max_attempts} tries.")

while attempts < max_attempts:
    guess      = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
    attempts  += 1
    difference = abs(guess - secret_number)   # abs() for absolute distance

    if guess == secret_number:
        print(f"✅ CORRECT! You got it in {attempts} attempt(s)!")
        break
    elif difference <= 2:
        print("🔥 Very close!")
    elif difference <= 5:
        print("🌡 Warm, getting closer.")
    else:
        hint = "higher" if guess < secret_number else "lower"
        print(f"❄ Cold. Try {hint}.")
else:                                    # runs when while ends WITHOUT break
    print(f"❌ Out of attempts. The number was {secret_number}.")

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Simulate a CUSTOM DIE using random and math:
# 1. Ask the user how many sides the die has (e.g. 6, 12, 20)
# 2. Ask how many times to roll it
# 3. Roll the die that many times using random.randint
# 4. Store all results in a list
# 5. Display: all results, the sum, the average, the max and min
# 6. Use math.floor() to show the average rounded down
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")
# ✏️ WRITE YOUR CODE HERE:
