# Password Generator & Strength Checker: Generates secure passwords and evaluates password entropy.
# Using Python's built-in secrets module (e.g., secrets.choice), not standard random, so the passwords are cryptographically secure.
import secrets, string, math

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation
pool = lowercase_letters + uppercase_letters + digits + special_characters


def generate_password(length):
    password = []
    password.append(secrets.choice(lowercase_letters))
    password.append(secrets.choice(uppercase_letters))
    password.append(secrets.choice(digits))
    password.append(secrets.choice(special_characters))

    for i in range(length-4):
        password.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password) # returns list only
    password = "".join(password)

    return password


def check_strength(password):
    score = 0
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_punct = any(char in special_characters for char in password)

    if has_uppercase:
        score += 26
    if has_lowercase:
        score += 26
    if has_digit:
        score += 10
    if has_punct:
        score += 32

    entropy = round(len(password) * math.log2(score), 1)
    if entropy < 36:
        return "WEAK"
    elif entropy >= 36 and entropy < 59:
        return "MODERATE"
    elif entropy >= 59:
        return "STRONG" 


while True:
    try:
        length = int(input("Enter the length of password in need: "))
        if length < 4:
            print("Password length must be at least 4.")
            continue
    except ValueError:
        print("Length of the password must be a natural number.")
        continue

    password = generate_password(length)
    print(password)
    strength = input("Do you want to check password strength? (y/n): ").lower()
    if strength == 'y':
        print(check_strength(password))
    else:
        break