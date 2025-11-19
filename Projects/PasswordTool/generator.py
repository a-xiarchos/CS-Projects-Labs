import secrets
import string

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Generates a secure random password.
    Ensures at least one character from each selected category is included.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4")

    alphabet = ""
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    if not alphabet:
        raise ValueError("At least one character type must be selected")

    # Ensure at least one of each selected type
    password = []
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(alphabet))

    # Shuffle to avoid predictable patterns (e.g. first char always upper)
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)
