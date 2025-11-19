import unittest
from checker import get_strength_score, check_length, check_complexity, calculate_entropy

class TestPasswordChecker(unittest.TestCase):
    def test_length(self):
        self.assertTrue(check_length("12345678"))
        self.assertFalse(check_length("1234567"))

    def test_complexity(self):
        comp = check_complexity("Aa1!")
        self.assertTrue(comp['has_upper'])
        self.assertTrue(comp['has_lower'])
        self.assertTrue(comp['has_digit'])
        self.assertTrue(comp['has_symbol'])
        
        comp = check_complexity("password")
        self.assertFalse(comp['has_upper'])
        self.assertFalse(comp['has_digit'])

    def test_entropy(self):
        # "password" -> 8 chars, lowercase only (pool 26). 8 * log2(26) approx 37.6
        e = calculate_entropy("password")
        self.assertGreater(e, 37)
        self.assertLess(e, 38)

    def test_strength_score(self):
        # Very weak
        score, _ = get_strength_score("12345")
        self.assertEqual(score, 0) # Short and simple
        
        # Strong
        # "CorrectHorseBatteryStaple" -> 25 chars, mixed case.
        score, _ = get_strength_score("CorrectHorseBatteryStaple")
        self.assertGreaterEqual(score, 3)

if __name__ == '__main__':
    unittest.main()
