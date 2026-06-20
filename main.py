import secrets
import string
import random

sysrand = random.SystemRandom()

def get_yes_no(prompt, default='y'):
    while True:
        s = input(prompt).strip().lower()
        if s == '' and default is not None:
            s = default
        if s in ('y', 'yes'):
            return True
        if s in ('n', 'no'):
            return False
        print("Please answer y or n.")

def get_int(prompt, min_val=4, default=12):
    while True:
        s = input(prompt).strip()
        if s == "" and default is not None:
            return default
        try:
            n = int(s)
            if n < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            return n
        except ValueError:
            print("Please enter a valid integer.")

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    sets = []
    if use_lower:
        sets.append(string.ascii_lowercase)
    if use_upper:
        sets.append(string.ascii_uppercase)
    if use_digits:
        sets.append(string.digits)
    if use_symbols:
        sets.append("!@#$%^&*()-_=+[]{};:,.<>/?")

    if not sets:
        sets = [string.ascii_letters, string.digits]

    password_chars = [secrets.choice(s) for s in sets]

    all_chars = "".join(sets)
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(all_chars) for _ in range(remaining)]

    sysrand.shuffle(password_chars)
    return "".join(password_chars)

def try_copy_to_clipboard(text):
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except Exception:
        return False

def main():
    print("=== Secure Password Generator ===")
    length = get_int("Password length (default 12): ", min_val=4, default=12)
    use_lower = get_yes_no("Include lowercase letters? (Y/n): ", default='y')
    use_upper = get_yes_no("Include uppercase letters? (Y/n): ", default='y')
    use_digits = get_yes_no("Include digits? (Y/n): ", default='y')
    use_symbols = get_yes_no("Include symbols? (Y/n): ", default='y')

    pwd = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    print("\nGenerated password:\n", pwd)
    if try_copy_to_clipboard(pwd):
        print("(Password copied to clipboard.)")
    else:
        print("(Install 'pyperclip' to enable auto-copy: pip install pyperclip)")

if __name__ == "__main__":
    main()
