# =============================================================
# EXERCISE 01 — Hello World 🌍
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - How to display text on screen using print()
#    - What a string (text value) is
#    - How to add comments to your code
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  print() is a BUILT-IN FUNCTION.
#  A function is a command that tells Python to DO something.
#  print() shows text (or values) on the screen.
#
#  A STRING is any text written between quotes: "hello" or 'hello'
#  Both single quotes and double quotes work the same way.
#
#  A COMMENT starts with #  —  Python ignores everything after it.
#  Comments are notes for humans, not for the computer.
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

print("Hello, World!")          # prints the classic first-program message
print('Hello again!')           # same function, single quotes also work

print()                         # print() with nothing inside = blank line

# You can print multiple things separated by commas
# Python adds a space between them automatically
print("My name is", "Python")   # output: My name is Python

# You can print numbers without quotes
print(2025)                     # prints the number 2025

# You can print math results directly
print(3 + 4)                    # Python calculates 7 and prints it

# The end= parameter changes the character printed at the end
# By default print() ends with a new line (\n)
print("Line one ", end="")      # end="" means: do NOT add a new line
print("same line!")             # this appears on the same line as above

# sep= changes the separator between items (default is a space)
print("A", "B", "C", sep="-")  # output: A-B-C

# ── EXPECTED OUTPUT ──────────────────────────────────────────
# Hello, World!
# Hello again!
#
# My name is Python
# 2025
# 7
# Line one same line!
# A-B-C
# ─────────────────────────────────────────────────────────────


# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# 1. Change the print() message to include YOUR NAME
# 2. Add a line that prints your city and your age, separated by " | "
# 3. Run the program with F5 and check the output
#
# Example of what you should see:
#   Hello! My name is Maria
#   Chicago | 15
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")

# ✏️ WRITE YOUR CODE HERE:
print("Hello! My name is YOUR_NAME")        # change YOUR_NAME
print("YOUR_CITY", "|", "YOUR_AGE", sep=" ") # change the values
