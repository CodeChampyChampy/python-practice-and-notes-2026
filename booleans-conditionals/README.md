
---

# Practice Rules (Non-Negotiable)

These apply to **every exercise**.

1. You define the function name.
2. One function per exercise.
3. Functions must **return**, never `print`.
4. No global variables.
5. No explicit comparisons to `None` or `""` unless explicitly allowed.
6. Use boolean logic (`and`, `or`, `not`) where appropriate.
7. Code must be readable and minimal.
8. After each exercise, add **at least one insight** to `notes.md`.

---

# Exercise Set — Booleans & Conditionals

---

## Exercise 1 — Age Category Resolver

### Objective

Determine a person’s age category using conditional logic.

### Input

* One integer representing an age.
* Assume the age is always a non-negative integer.

### Output

* A string representing the category.

### Business Rules

| Age Range | Output       |
| --------- | ------------ |
| < 13      | `"child"`    |
| 13–17     | `"teenager"` |
| 18–64     | `"adult"`    |
| ≥ 65      | `"senior"`   |

### Constraints

* Use `if / elif / else`
* No nested conditionals
* Exactly **one** return value must be produced

### Acceptance Tests

```text
10  → "child"
13  → "teenager"
18  → "adult"
65  → "senior"
```

### Real-World Use

User profiling, content restrictions, UI personalization.

---

## Exercise 2 — System Access Authorization

### Objective

Decide whether a user is allowed to access a system.

### Input

* Boolean: user is authenticated
* Boolean: user is banned

### Output

* Boolean indicating access permission

### Business Rules

Access is granted **only if**:

* the user is authenticated
* the user is not banned

### Constraints

* Must use boolean operators (`and`, `not`)
* No `if` nesting

### Acceptance Tests

```text
(True, False)  → True
(True, True)   → False
(False, False) → False
```

### Real-World Use

Authentication middleware, admin panels, dashboards.

---

## Exercise 3 — Required Field Validation

### Objective

Validate that a required field contains usable data.

### Input

* A single value (string or None)

### Output

* Boolean indicating validity

### Business Rules

* `None` → invalid
* Empty string → invalid
* Any non-empty string → valid

### Constraints

* ❌ Do NOT use `== ""`
* ❌ Do NOT use `== None`
* Use truthy/falsy behavior only

### Acceptance Tests

```text
"john" → True
""     → False
None   → False
```

### Real-World Use

Form validation, API payload checks.

---

## Exercise 4 — Discount Eligibility Engine

### Objective

Determine if a user qualifies for a discount.

### Input

* Integer: age
* Boolean: student status

### Output

* Boolean indicating discount eligibility

### Business Rules

Discount applies if:

* age is under 18
  **OR**
* the user is a student

### Constraints

* Must use the `or` operator
* No nested `if`

### Acceptance Tests

```text
(16, False) → True
(25, True)  → True
(25, False) → False
```

### Real-World Use

Pricing rules, promotions, e-commerce logic.

---

## Exercise 5 — Default Value Resolver (Short-Circuit Logic)

### Objective

Return a safe default when input is missing.

### Input

* One value (string or None)

### Output

* A string

### Business Rules

* If input is truthy → return it
* Otherwise → return `"Anonymous"`

### Constraints

* Must rely on short-circuit behavior
* No `if` statements allowed

### Acceptance Tests

```text
"Alice" → "Alice"
""      → "Anonymous"
None    → "Anonymous"
```

### Real-World Use

Configuration defaults, user display names.

---

## Exercise 6 — Guard Clause Practice

### Objective

Reject invalid input early.

### Input

* Boolean: system is online
* Boolean: user is admin

### Output

* String message

### Business Rules

* If system is offline → `"System unavailable"`
* Else if user is not admin → `"Access denied"`
* Else → `"Access granted"`

### Constraints

* Use `if / elif / else`
* No nested `if`

### Acceptance Tests

```text
(False, True)  → "System unavailable"
(True, False)  → "Access denied"
(True, True)   → "Access granted"
```

### Real-World Use

Feature gates, admin tooling.
