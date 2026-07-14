import re

# Common weak passwords
common_passwords = ["123456", "password", "admin", "qwerty", "welcome"]

password = input("Enter your password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1
else:
    print("❌ Password should be at least 8 characters long.")

# Uppercase check
if re.search(r"[A-Z]", password):
    score += 1
else:
    print("❌ Add at least one uppercase letter.")

# Lowercase check
if re.search(r"[a-z]", password):
    score += 1
else:
    print("❌ Add at least one lowercase letter.")

# Number check
if re.search(r"[0-9]", password):
    score += 1
else:
    print("❌ Add at least one number.")

# Special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    print("❌ Add at least one special character.")

# Common password check
if password.lower() in common_passwords:
    print("❌ This is a commonly used password.")
else:
    score += 1

# Display strength
print("\nPassword Strength:")

if score <= 2:
    print("🔴 Weak")
elif score <= 4:
    print("🟡 Medium")
else:
    print("🟢 Strong")

# Suggestion
if score < 6:
    print("\nSuggested Strong Password:")
    print("Example@123")
