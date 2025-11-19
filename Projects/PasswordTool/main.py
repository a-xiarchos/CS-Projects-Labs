import getpass
from checker import get_strength_score
from generator import generate_password

def check_password_flow():
    print("\n--- Check Password Strength ---")
    print("Enter a password to check its strength.")
    try:
        password = input("Password: ")
    except Exception as e:
        print(f"Error reading password: {e}")
        return

    if not password:
        print("No password entered.")
        return

    score, feedback = get_strength_score(password)
    
    strength_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print(f"\nStrength: {strength_labels[score]} (Score: {score}/4)")
    
    print("\nFeedback:")
    for item in feedback:
        print(f"- {item}")

def generate_password_flow():
    print("\n--- Generate Password ---")
    try:
        length_str = input("Enter length (default 16): ")
        length = int(length_str) if length_str else 16
    except ValueError:
        print("Invalid length. Using default 16.")
        length = 16
    
    try:
        password = generate_password(length=length)
        print(f"\nGenerated Password: {password}")
        
        # Optional: Check the strength of the generated password
        score, _ = get_strength_score(password)
        strength_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
        print(f"Strength: {strength_labels[score]}")
        
    except ValueError as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\n=== Password Tool ===")
        print("1. Check Password Strength")
        print("2. Generate Password")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            check_password_flow()
        elif choice == '2':
            generate_password_flow()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
