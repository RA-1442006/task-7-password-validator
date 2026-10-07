# Task 7: Simple Password Validator (Python)

Hi! I am a student intern working through the Python track. In this task, I built an interactive command-line password validation program that checks whether a given password meets standard security criteria.

---

## 📌 Project Overview & Objective

The goal of this project is to practice core Python fundamentals:
- Working with strings and character-level checks
- Loop iteration using `for` loops
- Conditional logic (`if` / `elif` statements)
- Input validation and defensive programming
- Standard library modules (`string` and `getpass`)
- Writing clean, readable, and human-friendly beginner code

---

## 🔒 Validation Rules

To be considered strong and valid, a password must satisfy all 5 rules:

| Rule | Requirement | Checked By | Error Message When Failed |
| :--- | :--- | :--- | :--- |
| **1. Minimum Length** | At least 8 characters long | `len(password) >= MIN_LENGTH` | `Must be at least 8 characters long.` |
| **2. Uppercase Letter** | At least one uppercase character (`A-Z`) | `ch.isupper()` | `Must contain at least one uppercase letter (A-Z).` |
| **3. Lowercase Letter** | At least one lowercase character (`a-z`) | `ch.islower()` | `Must contain at least one lowercase letter (a-z).` |
| **4. Number** | At least one digit (`0-9`) | `ch.isdigit()` | `Must contain at least one number (0-9).` |
| **5. Special Character** | At least one symbol (e.g. `!@#$%^&*`) | `ch in string.punctuation` | `Must contain at least one special character (!@#$%^&* etc.).` |

In addition, empty input is checked so the user is prompted again without crashing.

---

## 💡 My Approach

When designing this program, I wanted to keep it simple, readable, and structured like a real Python developer:

1. **Configurable Constant**: I defined `MIN_LENGTH = 8` at the top of the file so the length rule can be changed easily in one place.
2. **Boolean Flags**: Inside `check_password()`, I initialized four boolean variables (`has_upper`, `has_lower`, `has_digit`, `has_special`) to `False`.
3. **Single Loop Check**: I used a straightforward `for` loop to inspect each character in the password. For each character, an `if / elif` chain sets the corresponding flag to `True`. For special symbols, I checked membership against `string.punctuation`.
4. **Detailed Feedback**: Instead of just printing "invalid", the function appends a specific explanation to an `errors` list for every rule that fails. If the list is empty, the password is valid!
5. **Security & Privacy (No Echo)**: A real password tool shouldn't expose passwords on screen or echo them back. I used Python's `getpass` module (`getpass.getpass()`) for interactive terminals, with a graceful fallback to `input()` for piped/automated inputs.
6. **Continuous Loop**: The `main()` function keeps prompting the user in a `while True` loop until they type `exit` to quit.

---

## 📋 Examples Table (Valid & Invalid Passwords)

Here is a summary of the 5 valid and 5 invalid test passwords, showing which rules were tested and the expected outcome:

### Valid Passwords (All 5 Rules Met)

| # | Password | Length | Uppercase | Lowercase | Digit | Special | Expected Output |
| :-: | :--- | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | `Python2026!` | 11 | Yes (`P`) | Yes (`ython`) | Yes (`2026`) | Yes (`!`) | `[SUCCESS] Password is strong and valid!` |
| 2 | `Secure#Pass9` | 12 | Yes (`S, P`) | Yes (`ecure, ass`) | Yes (`9`) | Yes (`#`) | `[SUCCESS] Password is strong and valid!` |
| 3 | `Dev@Work2024` | 12 | Yes (`D, W`) | Yes (`ev, ork`) | Yes (`2024`) | Yes (`@`) | `[SUCCESS] Password is strong and valid!` |
| 4 | `C0ding_R0cks!` | 13 | Yes (`C, R`) | Yes (`ding, cks`) | Yes (`0, 0`) | Yes (`_, !`) | `[SUCCESS] Password is strong and valid!` |
| 5 | `Intern$hip7` | 11 | Yes (`I`) | Yes (`ntern, hip`) | Yes (`7`) | Yes (`$`) | `[SUCCESS] Password is strong and valid!` |

### Invalid Passwords (Rule Failures)

| # | Password | Length | Missing Requirement(s) | Expected Output / Error Messages |
| :-: | :--- | :-: | :--- | :--- |
| 1 | `short1!` | 6 | Length (< 8), Uppercase | `[FAILED] Password requirements not met:`<br>• `Must be at least 8 characters long.`<br>• `Must contain at least one uppercase letter (A-Z).` |
| 2 | `PASSWORD123!` | 12 | Lowercase (`a-z`) | `[FAILED] Password requirements not met:`<br>• `Must contain at least one lowercase letter (a-z).` |
| 3 | `password123!` | 12 | Uppercase (`A-Z`) | `[FAILED] Password requirements not met:`<br>• `Must contain at least one uppercase letter (A-Z).` |
| 4 | `PasswordSpecial!` | 16 | Number (`0-9`) | `[FAILED] Password requirements not met:`<br>• `Must contain at least one number (0-9).` |
| 5 | `Password1234` | 12 | Special character | `[FAILED] Password requirements not met:`<br>• `Must contain at least one special character (!@#$%^&* etc.).` |

---

## 🚀 How to Run the Program

### 1. Run the Interactive Validator
Make sure you are in the project folder and run:

```bash
python password_validator.py
```

- When prompted, enter a password. In the terminal, typing will be hidden for privacy.
- Type `exit` whenever you want to quit the program.

### 2. Run the Automated Tests
I also wrote unit tests to ensure all edge cases and rules stay verified:

```bash
python -m unittest test_password_validator.py -v
```

---

## 📁 Files Included

- `password_validator.py` - The main Python program with `check_password()` and `main()`
- `test_password_validator.py` - Automated test suite verifying the rules
- `test_examples.txt` - Documented sample runs and test console outputs
- `README.md` - Documentation and project guide

---

## 👤 Author

**M. Rohithanjan**  
*Python Programming Track Intern*  
*Veda Technology*  
- **GitHub**: [RA-1442006](https://github.com/RA-1442006)  
- **Repository**: [task-7-password-validator](https://github.com/RA-1442006/task-7-password-validator)

