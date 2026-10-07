import unittest
from password_validator import check_password, MIN_LENGTH


class TestPasswordValidator(unittest.TestCase):

    def test_valid_passwords(self):
        valid_passwords = [
            "Python2026!",
            "Secure#Pass9",
            "Dev@Work2024",
            "C0ding_R0cks!",
            "Intern$hip7",
        ]
        for pwd in valid_passwords:
            errors = check_password(pwd)
            self.assertEqual(len(errors), 0, f"Expected {pwd} to be valid, but got: {errors}")

    def test_invalid_too_short(self):
        # 7 characters, missing length
        errors = check_password("Ab1!def")
        self.assertIn(f"Must be at least {MIN_LENGTH} characters long.", errors)

    def test_invalid_no_uppercase(self):
        # All lowercase + number + special + length
        errors = check_password("python2026!")
        self.assertIn("Must contain at least one uppercase letter (A-Z).", errors)

    def test_invalid_no_lowercase(self):
        # All uppercase + number + special + length
        errors = check_password("PYTHON2026!")
        self.assertIn("Must contain at least one lowercase letter (a-z).", errors)

    def test_invalid_no_digit(self):
        # Letters + special + length
        errors = check_password("PythonSpecial!")
        self.assertIn("Must contain at least one number (0-9).", errors)

    def test_invalid_no_special(self):
        # Letters + number + length
        errors = check_password("Python2026Safe")
        self.assertIn("Must contain at least one special character (!@#$%^&* etc.).", errors)

    def test_empty_password(self):
        errors = check_password("")
        self.assertIn("Password cannot be empty.", errors)


if __name__ == "__main__":
    unittest.main()
