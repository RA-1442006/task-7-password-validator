import getpass
import string
import sys

# minimum length rule
MIN_LENGTH = 8


def get_password_input(prompt="Enter password (or type 'exit' to quit): "):
    # use getpass when running in interactive terminal so password isn't visible
    if sys.stdin.isatty():
        try:
            return getpass.getpass(prompt)
        except Exception:
            return input(prompt)
    else:
        # fallback to regular input for automated tests or piped input
        return input(prompt)


def check_password(password):
    errors = []

    # check if password is empty
    if not password:
        errors.append("Password cannot be empty.")
        return errors

    # check minimum length
    if len(password) < MIN_LENGTH:
        errors.append(f"Must be at least {MIN_LENGTH} characters long.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # check each character
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in string.punctuation:
            has_special = True

    # check all rule flags
    if not has_upper:
        errors.append("Must contain at least one uppercase letter (A-Z).")
    if not has_lower:
        errors.append("Must contain at least one lowercase letter (a-z).")
    if not has_digit:
        errors.append("Must contain at least one number (0-9).")
    if not has_special:
        errors.append("Must contain at least one special character (!@#$%^&* etc.).")

    return errors


def main():
    print("=" * 45)
    print("       Simple Password Validator")
    print("=" * 45)
    print("Rules for a valid password:")
    print(f"- At least {MIN_LENGTH} characters long")
    print("- At least one uppercase letter (A-Z)")
    print("- At least one lowercase letter (a-z)")
    print("- At least one number (0-9)")
    print("- At least one special character (!@#$%^&* etc.)")
    print("Type 'exit' anytime to quit.")
    print("(Note: Keystrokes are hidden while typing for privacy. Just type and press Enter!)\n")

    # keep asking for passwords until user types exit
    while True:
        try:
            password = get_password_input("Enter password (hidden): ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program.")
            break

        # check if user wants to quit
        if password.strip().lower() == "exit":
            print("Exiting password validator. Goodbye!")
            break

        # handle empty input gracefully
        if not password:
            print("[!] Password cannot be empty. Please try again.\n")
            continue

        # run validation checks
        errors = check_password(password)

        if not errors:
            print("[SUCCESS] Password is strong and valid!\n")
        else:
            print("[FAILED] Password requirements not met:")
            for err in errors:
                print(f"  - {err}")
            print()


if __name__ == "__main__":
    main()
