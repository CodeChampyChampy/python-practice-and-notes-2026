# What I Learned From My Mistakes

## Quotes in Expected Output

At first, I thought quotes shown in examples were part of the string value.

This led me to return strings with quotes included, which is not correct in most cases.

**What I learned:**
- Quotes in examples indicate type, not content
- Adding quotes manually makes them part of the data
- `return` gives back values, `print` only displays them

I intentionally kept one implementation to remember this distinction.
