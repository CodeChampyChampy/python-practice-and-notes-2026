
# Booleans & Conditionals — Reference Notes

These notes are **not a tutorial**.
They are **rules, reminders, and long-term patterns** worth remembering.

---

## Core Boolean Rules

* All comparisons return a boolean: `True` or `False`
* `if` checks **truthiness**, not equality
* Indentation defines code blocks in Python
* In an `if / elif / else` chain, **only the first matching condition runs**
* **Order of conditions matters** when ranges or cases overlap

---

## Comparison Operators

* `==` → equality (values are equal)
* `!=` → inequality
* `>`, `<`, `>=`, `<=` → value comparisons

Common use cases:

* age checks
* limits and boundaries
* permissions
* thresholds

---

## Truthy & Falsy Values

### Falsy values in Python:

* `None`
* `False`
* `0`
* `0.0`
* `""` (empty string)
* Empty collections: `[]`, `{}`, `()`

➡️ Everything else is truthy.

---

## Truthy / Falsy Best Practices

* Truthy/falsy checks **replace explicit empty or `None` comparisons**
* Avoid explicit comparisons unless strictly required

**Preferred**

```python
if value:
```

**Avoid**

```python
if value == "":
if value == None:
```

---

## Boolean Operators

### `and`

* Returns the **first falsy value**, otherwise the **last value**
* Used when **all conditions must be true**
* Common for access control

```python
if user and user.is_active:
```

---

### `or`

* Returns the **first truthy value**
* Used for **fallback / default values**

```python
value = input_value or default_value
```

---

### `not`

* Inverts truthiness
* Used for guards and permissions

```python
if not is_admin:
```

---

## Short-Circuiting

* Expressions are evaluated **left → right**
* Evaluation stops as soon as the result is known
* Prevents unnecessary or unsafe checks

```python
if user and user.is_active:
```

---

## Boolean Functions

* Boolean functions often return **boolean expressions directly**
* Avoid wrapping logic inside unnecessary `if` blocks

**Preferred**

```python
def is_valid(age):
    return age >= 18
```

**Avoid**

```python
def is_valid(age):
    if age >= 18:
        return True
    else:
        return False
```

---

## Guard Clauses & Early Returns

* Handle failure cases **first**
* Guard clauses improve readability
* Early returns avoid unnecessary temporary variables

**Preferred**

```python
def process(user):
    if not user:
        return None
    return user.name
```

---

## Style Growth Principles

The next growth step is **not logic — it’s style refinement**:

* Fewer temporary variables
* More direct returns
* Trusting boolean expressions
* Let conditions speak for themselves

---

## Type Hints

* Type hints must match **actual return values**
* Especially important for boolean-returning functions

```python
def is_active(user) -> bool:
    return bool(user and user.enabled)
```

---

## Common Mistakes to Avoid

* Overusing nested `if` instead of boolean operators
* Explicit comparisons instead of truthy / falsy checks
* Mixing logic and output (`print` inside functions)
* Writing long, unreadable conditions
* Adding variables that exist only to be returned

