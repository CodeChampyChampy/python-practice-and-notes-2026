# Python Strings — Notes & Mental Models

## 🎯 Goal
Learn string manipulation by purpose, not memorization.

---

## 🔥 Tier 1 — Must-Know (Daily Use)

| Method | Purpose |
|------|--------|
| `strip()` | Clean user input |
| `lower()` | Normalize text |
| `upper()` | Formatting |
| `replace()` | Mask / correct text |
| `split()` | Parse input |
| `join()` | Rebuild strings |
| `startswith()` | Validate prefixes |
| `endswith()` | Validate suffixes |

---

## ⚡ Tier 2 — Very Common (Weekly Use)

| Method | Purpose |
|------|--------|
| `find()` | Locate text |
| `count()` | Count occurrences |
| `capitalize()` | UI formatting |
| `title()` | Titles / headers |

---

## 🧪 Tier 3 — Validation & Edge Cases

| Method | Purpose |
|------|--------|
| `isdigit()` | Numeric input |
| `isalpha()` | Letters only |
| `isalnum()` | Letters + digits |
| `isspace()` | Whitespace |

---

## 🧠 Mental Model

Instead of thinking:
> “Which method should I use?”

Think:
> “What do I want to do to this text?”

| Goal | Method |
|----|------|
| Clean | `strip()` |
| Normalize | `lower()` |
| Split | `split()` |
| Rebuild | `join()` |
| Validate | `is*()` |

---

## 🧪 Exercises Implemented

1. Clean user input
2. Validate CSV file
3. Hide sensitive information
4. Split sentence into words
5. Build file path
6. Validate sudo command
7. Locate keyword in message
8. Count character occurrence
9. Format title
10. Capitalize sentence
11. Validate Gmail address
