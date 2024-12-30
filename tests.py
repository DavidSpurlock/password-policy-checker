import unittest
from checker import validate_password, calculate_entropy

class TestPasswordChecker(unittest.TestCase):
    def test_validate_password(self):
        self.assertEqual(validate_password("WeakPass"), [
            "Password must be at least 12 characters long.",
            "Password must contain at least one number.",
            "Password must contain at least one special character."
        ])

    def test_calculate_entropy(self):
        self.assertAlmostEqual(calculate_entropy("StrongP@ssw0rd"), 75.0, delta=5)

if __name__ == '__main__':
    unittest.main()

