# =============================================================
# EXERCISE 06 — The for Loop 🔁
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - Repeating code with the for loop
#    - Using range() to generate number sequences
#    - Iterating over strings and lists
#    - Accumulators: summing or counting inside a loop
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  A for loop REPEATS a block of code for each item in a sequence.
#
#  Structure:
#     for variable in sequence:
#         code that runs each repetition
#
#  range() generates a sequence of numbers:
#     range(5)        → 0, 1, 2, 3, 4        (stops before 5)
#     range(1, 6)     → 1, 2, 3, 4, 5        (start=1, stop=6)
#     range(0, 10, 2) → 0, 2, 4, 6, 8        (start, stop, step)
#     range(5, 0, -1) → 5, 4, 3, 2, 1        (counting down)
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

# --- Basic for with range ---
print("Counting from 1 to 5:")
for i in range(1, 6):                # i takes values: 1, 2, 3, 4, 5
    print(f"  Number: {i}")          # this line runs 5 times

# --- Counting down ---
print("\nLaunch countdown:")
for i in range(5, 0, -1):           # step = -1 counts downward
    print(f"  {i}...")
print("  🚀 LAUNCH!")

# --- Iterate over a string: visits each character one by one ---
word = "PYTHON"
print(f"\nLetters in '{word}':")
for letter in word:                  # letter = P, then Y, then T, etc.
    print(f"  {letter}")

# --- ACCUMULATOR PATTERN: building a total inside a loop ---
# An accumulator starts at 0 and grows with each iteration
total = 0                            # accumulator starts at zero
for n in range(1, 11):              # numbers 1 through 10
    total = total + n                # add current number to total
    # shorthand: total += n
print(f"\nSum of 1 to 10 = {total}")    # 55

# --- Multiplication table ---
number = int(input("\nEnter a number for its multiplication table: "))
print(f"\n--- Table of {number} ---")
for i in range(1, 11):              # multipliers 1 to 10
    result = number * i
    print(f"  {number} x {i:2} = {result}")
    # :2 inside { } means: use at least 2 characters width (aligns neatly)

# --- Counter: how many even numbers between 1 and 20 ---
even_count = 0                       # counter starts at 0
for num in range(1, 21):            # 1 to 20
    if num % 2 == 0:                # modulo 2 == 0 means it's even
        even_count += 1             # add 1 to the counter
print(f"\nEven numbers from 1 to 20: {even_count}")

# --- Nested for loops (a loop inside a loop) ---
print("\nMultiplication mini-table (1 to 3):")
for row in range(1, 4):             # outer loop: row 1, 2, 3
    for col in range(1, 4):         # inner loop: col 1, 2, 3 (runs 3x per row)
        print(f"{row}x{col}={row*col}", end="  ")  # end="  " stays on same line
    print()                         # new line after each row

# --- Building a pattern with nested loops ---
print("\nStaircase pattern:")
rows = 5
for i in range(1, rows + 1):       # i = 1, 2, 3, 4, 5
    print("* " * i)                # prints * repeated i times

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# 1. Ask the user for a positive integer n
# 2. Use a for loop to calculate the FACTORIAL of n
#    Factorial of 5 = 5 × 4 × 3 × 2 × 1 = 120
#    (start with result = 1 and multiply each iteration)
# 3. Show the operation step by step and the final result:
#    1 x 1 = 1
#    2 x 1 = 2
#    3 x 2 = 6
#    4 x 6 = 24
#    5 x 24 = 120
#    5! = 120
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")
# ✏️ WRITE YOUR CODE HERE:
