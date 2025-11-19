import math
import string

def check_length(password):
    """Returns True if password length is at least 8, else False."""
    return len(password) >= 8

def check_complexity(password):
    """
    Returns a dictionary with boolean values for:
    - has_upper
    - has_lower
    - has_digit
    - has_symbol
    """
    return {
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_symbol": any(c in string.punctuation for c in password)
    }

def calculate_entropy(password):
    """
    Calculates the entropy of the password in bits.
    Entropy = L * log2(R)
    L = length of password
    R = size of the pool of unique characters used
    """
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in string.punctuation for c in password): pool_size += 32
    
    if pool_size == 0:
        return 0
    
    return len(password) * math.log2(pool_size)

def get_strength_score(password):
    """
    Returns a tuple (score, feedback_list).
    Score is 0-4 (0=Very Weak, 4=Very Strong).
    """
    length_ok = check_length(password)
    complexity = check_complexity(password)
    entropy = calculate_entropy(password)
    
    score = 0
    feedback = []
    
    # Base score on entropy
    if entropy < 28:
        score = 0 # Very Weak
        feedback.append("Password is very weak. It's vulnerable to instant cracking.")
    elif entropy < 36:
        score = 1 # Weak
        feedback.append("Password is weak. Consider making it longer.")
    elif entropy < 60:
        score = 2 # Moderate
        feedback.append("Password is okay, but could be stronger.")
    elif entropy < 128:
        score = 3 # Strong
        feedback.append("Strong password!")
    else:
        score = 4 # Very Strong
        feedback.append("Very strong password!")

    # Penalize for missing character types
    if not complexity['has_upper']:
        feedback.append("Add uppercase letters.")
    if not complexity['has_lower']:
        feedback.append("Add lowercase letters.")
    if not complexity['has_digit']:
        feedback.append("Add numbers.")
    if not complexity['has_symbol']:
        feedback.append("Add symbols (e.g., !@#$).")
        
    if not length_ok:
        feedback.append("Password is too short. Make it at least 8 characters.")
        # Cap score if too short
        score = min(score, 1)

    return score, feedback
