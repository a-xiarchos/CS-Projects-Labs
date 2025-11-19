import unittest
import string
from generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_length(self):
        pwd = generate_password(length=12)
        self.assertEqual(len(pwd), 12)
        
        pwd = generate_password(length=100)
        self.assertEqual(len(pwd), 100)

    def test_character_inclusion(self):
        # Generate a password that should have all types
        pwd = generate_password(length=50, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
        
        self.assertTrue(any(c.isupper() for c in pwd), "Should contain uppercase")
        self.assertTrue(any(c.islower() for c in pwd), "Should contain lowercase")
        self.assertTrue(any(c.isdigit() for c in pwd), "Should contain digits")
        self.assertTrue(any(c in string.punctuation for c in pwd), "Should contain symbols")

    def test_custom_inclusion(self):
        # Only digits
        pwd = generate_password(length=20, use_upper=False, use_lower=False, use_digits=True, use_symbols=False)
        self.assertTrue(all(c.isdigit() for c in pwd))
        
        # Only uppercase
        pwd = generate_password(length=20, use_upper=True, use_lower=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(c.isupper() for c in pwd))

    def test_min_length_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

if __name__ == '__main__':
    unittest.main()
