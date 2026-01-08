# Learning Notes — Python Numbers

This file contains **conceptual notes, decisions, and rules** collected during the learning process.
It is meant as a **personal reference**, not a tutorial.

---

## 1. Function Naming Conventions

### Rule
Prefer **verb-first, descriptive, natural English** function names.

Function names should read like:
> "what the function does"

### Examples

❌ Weak / unnatural:
- two_num_sum
- num_type
- int_check

✅ Preferred:
- sum_two_numbers
- add_two_numbers
- convert_string_to_int
- calculate_total_price

### Reasoning
- Matches natural English phrasing
- Improves readability
- Scales better in real codebases
- Easier to understand during code review

> If the name sounds unnatural when read out loud, it’s probably not ideal.

---

## 2. Avoid Redundant Abstractions

### Rule
Do **not** create functions that only wrap built-in functions **without adding logic**.

❌ Bad example:
```python
def get_type(x):
    return type(x)

✅ Acceptable when learning or when logic will be added later:

3. Augmented Assignments 

Augmented assignments (+=, -=, *=, etc.) were intentionally removed from current practice.

---

## 4. Commit Often, Push Reasonably

### Rule
- Make **small, meaningful commits** whenever you finish a logical unit of work.
- Push to the remote repository at the end of a session or after a milestone.
- Avoid waiting until the very end to commit or push.

### Reasoning
- Keeps a clear history of your progress.
- Makes it easier to rollback or track changes.
- Mirrors **real-world development workflows**.
- Keeps your learning repository as a **chronological log** of improvements.

### Example
```bash
git add .
git commit -m "practice(numbers): add basic arithmetic functions"
git push

Commits tell your story. Pushes publish it.