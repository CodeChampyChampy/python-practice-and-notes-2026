# 🧠 Exception Handling — Practical Learning Path (Simplified)

## 🎯 Goal

* Learn **how developers think about failures**
* Practice **core exception handling** (the 80/20)
* Build a **clean, consistent Python learning repo**
* Stay aligned with FreeCodeCamp level + real usage

You will **NOT** do:

* ❌ File handling (4)
* ❌ Data pipelines (5)
* ❌ Custom exceptions (6)


# 🧩 EXERCISES (FINAL VERSION)

---

## 🧠 01 — Thinking in Failures (FOUNDATION)

📄 **File:** `01_thinking_in_failures.md`
📌 **Type:** Reasoning only (NO CODE)

### Purpose

Train yourself to **anticipate errors before writing code**.
This is a **core developer skill**, not Python-specific.

---

### Rules

* ❌ No Python code
* ❌ No functions
* ❌ No `try/except`
* ✅ Only reasoning and written analysis

---

### Task

For each operation, write:

1. What can go wrong?
2. Why this matters in real programs

---

### Operations to analyze

* `int(input())`
* Division (`a / b`)
* Accessing a dictionary key
* Calling an external API (simulated)

---

### Required Template

```md
## Operation: int(input())

Possible failures:
- ...
- ...

Why this matters:
- ...
```

---

### Expected Outcome

You should **instinctively see failure points** before coding.

---

## 🧪 02 — Safe User Input

📄 **File:** `02_safe_user_input.py`
📌 **Focus:** Protecting user input

---

### Rules

* ✅ Use **one function**
* ✅ Use `try / except`
* ❌ No loops
* ❌ No `else` or `finally` yet

---

### Task

* Ask the user for a number
* Convert it to `int`
* If valid → print the number
* If invalid → print a clear error message

---

### Why This Matters

User input is **untrusted by default**.
This pattern is used in:

* CLI tools
* Forms
* Scripts
* Backend endpoints

---

## 🧮 03 — Safe Calculator (CORE PRACTICE)

📄 **File:** `03_safe_calculator.py`
📌 **Focus:** Multiple failure points in one program

---

### Rules

* ✅ Use functions
* ✅ Use `try / except / else`
* ❌ No loops
* ❌ No custom exceptions

---

### Task

* Ask for:

  * First number
  * Second number
  * Operation (`+ - * /`)
* Handle:

  * Invalid numbers
  * Division by zero
  * Invalid operation

---

### Why This Matters

This simulates:

* Real validation logic
* Multiple error sources
* Clean separation between success and failure

```md
# Exception Handling — Core Practice

This folder contains beginner-to-intermediate exercises focused on
understanding how and why exception handling is used in Python.

## Files
- 01_thinking_in_failures.md → learning to anticipate errors
- 02_safe_user_input.py → validating user input
- 03_safe_calculator.py → handling multiple failure cases
- Bonus: debug-in-vs-code.py
```

---

# 📝 learning-notes/exceptions (Reflection Only)

This file is **not exercises**.

Sections to keep:

```md
## When exceptions are necessary
## What should be validated with if vs try/except
## Common mistakes I made
## Patterns I recognize now
```

