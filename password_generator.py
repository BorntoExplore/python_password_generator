import argparse, string, secrets

def generate_password(length,include_symbols):
    character = string.ascii_letters + string.digits
    if include_symbols:
        character += string.punctuation
    
    password = ''.join(secrets.choice(character) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a strong password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password(defauly is 12)")
    parser.add_argument("--symbols",action="store_true", help="Symbols to include in password")

    args = parser.parse_args()

    password = generate_password(args.length, args.symbols)

    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
