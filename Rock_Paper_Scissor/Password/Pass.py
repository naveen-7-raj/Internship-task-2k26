import random
import string

print("🔐 Password Generator")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Characters to use in password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Display password
print("\nGenerated Password:", password)