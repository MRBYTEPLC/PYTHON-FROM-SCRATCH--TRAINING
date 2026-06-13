# =============================================================
# EXERCISE 07 — The while Loop 🔄
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - Repeating code while a condition stays True
#    - Difference between for and while
#    - break (exit) and continue (skip) commands
#    - Avoiding infinite loops
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  while repeats a block AS LONG AS a condition stays True.
#
#  Structure:
#     while condition:
#         code block
#
#  Use while when you DON'T KNOW in advance how many times
#  something will repeat (waiting for user input, game loops, etc.)
#
#  Use for when you DO KNOW the number of repetitions.
#
#  break    → immediately exits the loop, no matter what
#  continue → skips the rest of THIS iteration, goes to next
#
#  ⚠️  INFINITE LOOP: if the condition never becomes False,
#      the loop runs forever. Always update something inside!
#      In Thonny: press the red STOP button to cancel.
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

# --- Basic while loop ---
count = 1                                # counter — MUST exist before while
while count <= 5:                        # condition checked BEFORE each run
    print(f"  Repetition {count}")
    count += 1                           # ⚠️ MUST update or loop runs forever!
print("Loop finished!")

# --- Guessing game with while ---
import random                            # import gives Python access to extra tools
                                         # random: a built-in module for random numbers

secret = random.randint(1, 10)           # randint(a,b) picks a random int from a to b
attempts = 0                             # count how many tries the user takes

print("\n=== NUMBER GUESSING GAME (1-10) ===")
while True:                              # True = loop runs until we call break
    guess = int(input("Your guess: "))
    attempts += 1                        # add 1 for each attempt

    if guess < secret:
        print("  Too low! Try higher.")
    elif guess > secret:
        print("  Too high! Try lower.")
    else:                                # guess == secret
        print(f"  ✅ Correct! The number was {secret}.")
        print(f"  You got it in {attempts} attempt(s)!")
        break                            # break exits the while loop immediately

# --- continue: skip an iteration ---
print("\nNumbers 1 to 10, skipping multiples of 3:")
n = 0
while n < 10:
    n += 1
    if n % 3 == 0:                       # is it a multiple of 3?
        continue                         # skip the print, jump back to while
    print(f"  {n}", end=" ")
print()                                  # newline at the end

# --- Input validation with while (very common pattern!) ---
print()
while True:                              # keep asking until input is valid
    age = int(input("Enter your age (must be between 1 and 120): "))
    if 1 <= age <= 120:                  # valid range
        print(f"  Age recorded: {age}")
        break                            # valid input received, exit loop
    else:
        print("  ❌ Invalid age. Try again.")

# --- Accumulator with while: sum user inputs ---
print("\nEnter numbers to add up (type 0 to stop):")
total   = 0                              # accumulator
counter = 0                              # how many numbers were entered

while True:
    num = float(input("  Enter a number (0 to stop): "))
    if num == 0:                         # sentinel value: 0 signals "stop"
        break
    total   += num                       # add to total
    counter += 1                         # count the entry

if counter > 0:
    average = total / counter
    print(f"\nYou entered {counter} numbers.")
    print(f"Total: {total:.2f}  |  Average: {average:.2f}")
else:
    print("No numbers were entered.")

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Build a "Guess the word" game:
# 1. Define a secret word (str) inside the code
# 2. Give the user a maximum of 5 attempts using while
# 3. On each attempt:
#    - If correct → print "Correct!" and stop
#    - If wrong   → show how many attempts are left
# 4. If all 5 attempts are used → reveal the secret word
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")
# ✏️ WRITE YOUR CODE HERE:
