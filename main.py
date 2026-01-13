import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    return score, feedback

def strength_label(score):
    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"
    
def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)
    label = strength_label(score)

    print(f"\nStrength: {label} ({score}/5)")

    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print("-", tip)


if __name__ == "__main__":
    main()