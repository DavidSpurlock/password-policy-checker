import re
import math

def validate_password(password):
    policies = {
        "min_length": 12,
        "uppercase": True,
        "lowercase": True,
        "numbers": True,
        "special_characters": True,
    }

    errors = []

    # Check length
    if len(password) < policies["min_length"]:
        errors.append(f"Password must be at least {policies['min_length']} characters long.")

    # Check character types
    if policies["uppercase"] and not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter.")
    if policies["lowercase"] and not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter.")
    if policies["numbers"] and not re.search(r'[0-9]', password):
        errors.append("Password must contain at least one number.")
    if policies["special_characters"] and not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        errors.append("Password must contain at least one special character.")

    return errors

def calculate_entropy(password):
    pool_size = 0
    if re.search(r'[a-z]', password): pool_size += 26
    if re.search(r'[A-Z]', password): pool_size += 26
    if re.search(r'[0-9]', password): pool_size += 10
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password): pool_size += 32

    entropy = len(password) * math.log2(pool_size)
    return entropy

