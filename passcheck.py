import os
import string
import random
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Easy/common/leaked passwords (extended list)
easy_words = set([
    "123456", "123456789", "password", "qwerty", "12345678", "111111", "123123", "1234567",
    "dragon", "baseball", "abc123", "football", "monkey", "letmein", "admin", "welcome",
    "login", "iloveyou", "sunshine", "1234", "passw0rd", "000000", "superman", "qazwsx",
    "asdfgh", "1q2w3e4r", "zaq1zaq1", "starwars", "freedom", "batman", "trustno1"
])

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    title = pyfiglet.figlet_format("PassCheck", font="slant")
    print(Fore.CYAN + title)
    subtitle = pyfiglet.figlet_format("DoomSlayer", font="standard")
    print(Fore.RED + subtitle)
    print(Style.RESET_ALL)

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 2
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 2

    if password.lower() in easy_words:
        return score, "Very Weak", "This password is very common and unsafe!"

    if score <= 2:
        return score, "Very Weak", "Use a longer password with uppercase, digits, and symbols."
    elif score <= 4:
        return score, "Weak", "Add uppercase letters, digits, and symbols to strengthen your password."
    elif score <= 6:
        return score, "Medium", "Try adding more length and special characters."
    elif score <= 8:
        return score, "Strong", "Good! You can make it very strong by adding more variety."
    else:
        return score, "Very Strong", "Great password! Adding length can make it excellent."

def color_and_print(password, score, strength, advice):
    if password.lower() in easy_words:
        color = Fore.RED
        strength = "LEAKED/COMMON - CHANGE IMMEDIATELY!"
    else:
        if strength == "Very Weak":
            color = Fore.RED
        elif strength == "Weak":
            color = Fore.RED
        elif strength == "Medium":
            color = Fore.YELLOW
        elif strength in ["Strong", "Very Strong"]:
            color = Fore.GREEN
        else:
            color = Fore.CYAN

    print(f"{color}{password}: {strength} (Score: {score}/10)")
    if strength.startswith("LEAKED") or strength in ["Very Weak", "Weak", "Medium"]:
        print(f"{Fore.MAGENTA}  Advice: {advice}")
    print(Style.RESET_ALL)

def main():
    print_banner()
    print("Type a password to check its strength.")
    print("Or type 'generate' to get a strong password.")
    print("Type 'exit' to quit.\n")

    while True:
        pwd = input("Enter a password: ").strip()
        if pwd.lower() == "exit":
            print("Exiting. Stay safe!")
            break
        elif pwd.lower() == "generate":
            generated = generate_strong_password()
            print(Fore.GREEN + f"Generated password: {generated}\n")
            continue
        elif not pwd:
            continue

        score, strength, advice = check_password_strength(pwd)
        color_and_print(pwd, score, strength, advice)

if __name__ == "__main__":
    main()
