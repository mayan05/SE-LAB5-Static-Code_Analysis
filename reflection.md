# Lab 5: Static Code Analysis - Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest:**
Fixing style issues like converting to f-strings and removing unused imports was quick and simple. These didn't require changing the logic—just reformatting the code.

**Hardest:**
The mutable default argument (`logs=[]`) was tricky because it requires understanding how Python handles defaults. The fix involved changing the default to `None` and adding initialization logic inside the function, which needed careful thought.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

No, the tools were accurate. All the issues they flagged were real problems in the code. The tools correctly identified bugs, security vulnerabilities, and style violations.

## 3. How would you integrate static analysis tools into your actual software development workflow?

**Locally:**
Use pre-commit hooks to automatically run Pylint, Flake8, and Bandit before committing code. Set up your IDE to show warnings in real-time as you code.

**In CI/CD:**
Run these tools on every pull request using GitHub Actions or similar. Fail the build if critical issues are found to prevent bad code from being merged.

**Configuration:**
Create shared config files (`.pylintrc`, `.flake8`) so the entire team uses the same rules.

## 4. What tangible improvements did you observe in code quality after applying the fixes?

- **Better security:** Removed dangerous `eval()` function and added input validation
- **More readable:** Converted to f-strings and improved dictionary iteration
- **More robust:** Added proper exception handling instead of bare `except:` blocks
- **Fewer bugs:** Fixed mutable default argument that could cause hidden issues
- **Professional:** Code now follows PEP 8 standards and best practices