# =============================================================
# EXERCISE 04 — Math Operations 🔢
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - The 7 arithmetic operators in Python
#    - Floor division (//) and modulo (%)
#    - Exponentiation (**)
#    - Operator precedence (order of operations)
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  Python arithmetic operators:
#
#   +   Addition           5 + 3  = 8
#   -   Subtraction        5 - 3  = 2
#   *   Multiplication     5 * 3  = 15
#   /   Division           5 / 2  = 2.5    (always returns float!)
#   //  Floor division     5 // 2 = 2      (drops the decimal part)
#   %   Modulo             5 % 2  = 1      (remainder of division)
#   **  Exponentiation     2 ** 3 = 8      (2 to the power of 3)
#
#  ORDER of operations (same as in math class):
#  1. **  (exponent — highest priority)
#  2. * / // %  (multiplication and division)
#  3. + -  (addition and subtraction — lowest priority)
#  Use parentheses ( ) to change the order!
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

a = 10
b = 3

# --- Basic operations ---
print(f"{a} + {b} = {a + b}")        # addition       → 13
print(f"{a} - {b} = {a - b}")        # subtraction    → 7
print(f"{a} * {b} = {a * b}")        # multiplication → 30

# --- Division: two types! ---
print(f"{a} / {b} = {a / b}")        # regular division → 3.3333... (float)
print(f"{a} // {b} = {a // b}")      # floor division   → 3  (integer result)

# --- Modulo: gives the REMAINDER after division ---
# Great for: checking even/odd, grouping, time conversions
print(f"{a} % {b} = {a % b}")        # 10 ÷ 3 = 3 remainder 1 → prints 1

# --- Exponentiation ---
print(f"2 ** 8 = {2 ** 8}")          # 2 to the 8th power → 256
print(f"9 ** 0.5 = {9 ** 0.5}")     # square root of 9 (power of 0.5) → 3.0

# ── ORDER OF OPERATIONS ──────────────────────────────────────

# Python follows PEMDAS / BODMAS
result1 = 2 + 3 * 4          # multiplication first → 2 + 12 = 14
result2 = (2 + 3) * 4        # parentheses first    → 5 * 4  = 20
print(f"\n2 + 3 * 4  = {result1}")   # 14
print(f"(2 + 3)*4  = {result2}")     # 20

# ── PRACTICAL EXAMPLES ───────────────────────────────────────

# Example 1: How many boxes fit and how many items are left over?
total_items = 47
items_per_box = 6
full_boxes = total_items // items_per_box   # floor division: complete boxes
leftover   = total_items % items_per_box    # modulo: remaining items
print(f"\n{total_items} items: {full_boxes} full boxes + {leftover} left over")

# Example 2: Is a number even or odd?
number = 17
if number % 2 == 0:                         # remainder of dividing by 2 is 0?
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")               # remainder is 1, so it's odd

# Example 3: Convert seconds to hours, minutes, seconds
total_seconds = 3725
hours     = total_seconds // 3600           # 3600 seconds in 1 hour
remaining = total_seconds % 3600            # seconds left after extracting hours
minutes   = remaining // 60                 # 60 seconds in 1 minute
seconds   = remaining % 60                  # final leftover seconds
print(f"\n{total_seconds} seconds = {hours}h {minutes}m {seconds}s")

# Example 4: Area and perimeter of a rectangle
width  = float(input("\nRectangle width (cm): "))
length = float(input("Rectangle length (cm): "))
area      = width * length
perimeter = 2 * (width + length)
print(f"Area      = {area:.2f} cm²")
print(f"Perimeter = {perimeter:.2f} cm")

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Ask the user for two integers (num1 and num2).
# Display all 7 operators applied to those two numbers
# in a clean format like this:
#
#   num1 = 10  |  num2 = 4
#   +   → 14
#   -   → 6
#   *   → 40
#   /   → 2.5
#   //  → 2
#   %   → 2
#   **  → 10000
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")
# ✏️ WRITE YOUR CODE HERE:
