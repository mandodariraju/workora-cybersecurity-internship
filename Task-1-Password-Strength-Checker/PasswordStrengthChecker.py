import math
import string

# List of common weak passwords
COMMON_PASSWORDS = {
    "123456", "password", "password123", "123456789",
    "qwerty", "abc123", "admin", "welcome",
    "letmein", "iloveyou", "000000", "111111"
}


def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def password_strength(password):
    suggestions = []

    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    if not length:
        suggestions.append("Use at least 8 characters.")
    if not upper:
        suggestions.append("Add uppercase letters.")
    if not lower:
        suggestions.append("Add lowercase letters.")
    if not digit:
        suggestions.append("Include digits.")
    if not special:
        suggestions.append("Include special characters.")

    entropy = calculate_entropy(password)

    if password.lower() in COMMON_PASSWORDS:
        classification = "Weak"
        suggestions.append("Avoid common dictionary passwords.")
    else:
        score = sum([length, upper, lower, digit, special])

        if entropy < 40 or score <= 2:
            classification = "Weak"
        elif entropy < 60:
            classification = "Moderate"
        elif entropy < 80:
            classification = "Strong"
        else:
            classification = "Exceptional"

    return {
        "Length": length,
        "Uppercase": upper,
        "Lowercase": lower,
        "Digits": digit,
        "Special Characters": special,
        "Entropy": entropy,
        "Strength": classification,
        "Suggestions": suggestions
    }


def main():
    print("=" * 50)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = input("Enter your password: ")

    result = password_strength(password)

    print("\nPassword Analysis")
    print("-" * 50)

    for key in ["Length", "Uppercase", "Lowercase", "Digits", "Special Characters"]:
        print(f"{key:<20}: {'Yes' if result[key] else 'No'}")

    print(f"\nPassword Entropy : {result['Entropy']} bits")
    print(f"Password Strength: {result['Strength']}")

    if result["Suggestions"]:
        print("\nSuggestions:")
        for suggestion in result["Suggestions"]:
            print(f"- {suggestion}")
    else:
        print("\nExcellent! Your password follows recommended security practices.")


if __name__ == "__main__":
    main()
