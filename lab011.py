#Online Account Registration

username = input("Enter your username: ")
password = input("Enter your password: ")

print("========================================")
print("       PASSWORD VALIDATION REPORT")
print("========================================")

print("Username:", username)
print("Password:", "*" * len(password))

print("--- Validation Rules ---")

if len(password) >= 8:
    print("[PASS] Minimum 8 characters")
    rule1 = True
else:
    print("[FAIL] Minimum 8 characters")
    rule1 = False

has_digit = False

for char in password:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    print("[PASS] At least one digit")
    rule2 = True
else:
    print("[FAIL] At least one digit")
    rule2 = False

has_upper = False

for char in password:
    if char.isupper():
        has_upper = True
        break

if has_upper:
    print("[PASS] At least one uppercase letter")
    rule3 = True
else:
    print("[FAIL] At least one uppercase letter")
    rule3 = False

print("--- Result ---")

if rule1 and rule2 and rule3:
    print("Password is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("Password is INVALID!")

print("========================================")