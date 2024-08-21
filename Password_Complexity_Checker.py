import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria])

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*()).")

    if criteria_met == 5:
        strength = "Strong"
    elif 3 <= criteria_met < 5:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

def main():
    while True:
        password = input("Enter a password to assess its strength: ")
        strength, feedback = assess_password_strength(password)
        
        print(f"Password strength: {strength}")
        if feedback:
            print("Feedback:")
            for item in feedback:
                print(f"- {item}")
        
        another = input("Would you like to assess another password? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
