# =============================================================
# EXERCISE 08 — Lists 📋
# =============================================================
# 📌 WHAT WILL YOU LEARN?
#    - Creating and accessing lists
#    - Indexes: positive and negative
#    - List methods: append, remove, sort, len, etc.
#    - Iterating over lists with for
#    - Slicing (extracting portions of a list)
# =============================================================

# ── THEORY ───────────────────────────────────────────────────
#
#  A LIST is an ordered collection of items.
#  You can store multiple values in ONE variable.
#  Lists use square brackets [ ] and items are separated by commas.
#
#  INDEXING: each item has a position number starting at 0
#    Index:  0       1        2        3       4
#    List:  ["a",  "b",    "c",    "d",   "e"]
#    Index: -5     -4      -3      -2     -1    ← negative indexes from end
#
#  MUTABLE: you CAN change items in a list after creating it.
#
# ─────────────────────────────────────────────────────────────

# ── CODE EXPLAINED ───────────────────────────────────────────

# --- Creating a list ---
fruits  = ["apple", "banana", "cherry", "mango", "grape"]
numbers = [10, 25, 3, 47, 8, 15]
mixed   = ["Python", 3, True, 4.5]     # lists can hold different types

# --- Accessing items with indexes ---
print(fruits[0])             # first item  → apple
print(fruits[2])             # third item  → cherry
print(fruits[-1])            # last item   → grape
print(fruits[-2])            # second to last → mango

# --- Changing an item ---
fruits[1] = "blueberry"      # replaces "banana" at index 1
print(f"After change: {fruits}")

# --- len(): number of items in the list ---
print(f"Number of fruits: {len(fruits)}")        # 5

# --- SLICING: extract a portion of the list ---
# list[start : stop]  → from start up to (not including) stop
print(fruits[1:4])           # items at index 1, 2, 3
print(fruits[:3])            # from beginning to index 2 (first 3 items)
print(fruits[2:])            # from index 2 to the end
print(fruits[::-1])          # reverses the list (step = -1)

# ── LIST METHODS ─────────────────────────────────────────────

colors = ["red", "blue", "green"]

# append(): add one item to the END of the list
colors.append("yellow")
print(f"\nAfter append: {colors}")

# insert(): add item at a specific position
colors.insert(1, "orange")           # insert "orange" at index 1
print(f"After insert: {colors}")

# remove(): removes the FIRST occurrence of a value
colors.remove("blue")
print(f"After remove: {colors}")

# pop(): removes and RETURNS the item at an index (default: last)
removed = colors.pop()               # removes last item
print(f"Removed: {removed}  |  List: {colors}")
removed2 = colors.pop(0)            # removes item at index 0
print(f"Removed: {removed2}  |  List: {colors}")

# sort(): sorts in ascending order (modifies the list in place)
scores = [78, 45, 92, 67, 88, 55]
scores.sort()                        # ascending (small to large)
print(f"\nSorted ascending: {scores}")
scores.sort(reverse=True)            # descending (large to small)
print(f"Sorted descending: {scores}")

# in operator: check if an item EXISTS in the list
print(f"\n'cherry' in fruits: {'cherry' in fruits}")   # True
print(f"'kiwi' in fruits: {'kiwi' in fruits}")         # False

# index(): find the position of an item
fruit_list = ["apple", "banana", "cherry"]
position = fruit_list.index("banana")
print(f"'banana' is at index: {position}")             # 1

# count(): how many times a value appears
grades = [90, 85, 90, 72, 90, 88]
print(f"Number of 90s: {grades.count(90)}")            # 3

# ── ITERATING OVER A LIST ────────────────────────────────────

print("\n--- Grocery List ---")
grocery = ["milk", "eggs", "bread", "butter"]
for item in grocery:                 # visits each item one by one
    print(f"  ☐ {item}")

# enumerate() gives both the INDEX and the VALUE at the same time
print("\n--- With numbering ---")
for index, item in enumerate(grocery, start=1):   # start=1 to count from 1
    print(f"  {index}. {item}")

# ── PRACTICAL EXAMPLE: Grade Manager ────────────────────────

print("\n=== GRADE MANAGER ===")
student_grades = []                  # start with an empty list

for i in range(1, 4):               # collect 3 grades
    grade = float(input(f"Enter grade {i}: "))
    student_grades.append(grade)    # add each grade to the list

total   = sum(student_grades)       # sum() adds all numbers in a list
average = total / len(student_grades)
highest = max(student_grades)       # max() finds the largest value
lowest  = min(student_grades)       # min() finds the smallest value

print(f"\nGrades : {student_grades}")
print(f"Average: {average:.2f}  |  Highest: {highest}  |  Lowest: {lowest}")

# ── 🔧 YOUR TURN ─────────────────────────────────────────────
# INSTRUCTIONS:
# Build a To-Do List program:
# 1. Create an empty list called tasks
# 2. Ask the user to enter 4 tasks with input() — append each one
# 3. Display the list numbered (use enumerate)
# 4. Ask which task to mark as done and remove it with remove()
# 5. Display the updated list
# ─────────────────────────────────────────────────────────────

print()
print("---- YOUR TURN ----")
# ✏️ WRITE YOUR CODE HERE:
