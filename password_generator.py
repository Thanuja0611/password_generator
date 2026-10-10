import secrets
import string
import sys


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_ambiguous: bool = False,
) -> str:
    """Generate a cryptographically secure random password.

    Args:
        length: Desired password length (minimum 4).
        use_upper: Include uppercase letters (A-Z).
        use_lower: Include lowercase letters (a-z).
        use_digits: Include digits (0-9).
        use_symbols: Include punctuation symbols.
        exclude_ambiguous: Exclude characters that look similar (l, 1, I, O, 0).

    Returns:
        A securely generated random password string.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    pools = []
    guaranteed = []

    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"

    if exclude_ambiguous:
        ambiguous = "il1Lo0O"
        upper_chars = "".join(c for c in upper_chars if c not in ambiguous)
        lower_chars = "".join(c for c in lower_chars if c not in ambiguous)
        digit_chars = "".join(c for c in digit_chars if c not in ambiguous)

    if use_upper and upper_chars:
        pools.append(upper_chars)
        guaranteed.append(secrets.choice(upper_chars))
    if use_lower and lower_chars:
        pools.append(lower_chars)
        guaranteed.append(secrets.choice(lower_chars))
    if use_digits and digit_chars:
        pools.append(digit_chars)
        guaranteed.append(secrets.choice(digit_chars))
    if use_symbols and symbol_chars:
        pools.append(symbol_chars)
        guaranteed.append(secrets.choice(symbol_chars))

    if not pools:
        raise ValueError("At least one character set must be selected.")

    # Combine all characters
    combined_pool = "".join(pools)

    # Fill the remaining length with cryptographically secure random selections
    remaining_length = length - len(guaranteed)
    remaining_chars = [secrets.choice(combined_pool) for _ in range(remaining_length)]

    # Combine and shuffle
    password_chars = guaranteed + remaining_chars
    # Fisher-Yates shuffle using secrets.randbelow
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def interactive_menu():
    print("=" * 45)
    print("        SECURE PASSWORD GENERATOR            ")
    print("=" * 45)

    try:
        raw_len = input("Enter password length [default: 16]: ").strip()
        length = int(raw_len) if raw_len else 16
        if length < 4:
            print("Length adjusted to minimum of 4.")
            length = 4

        raw_count = input("How many passwords to generate? [default: 1]: ").strip()
        count = int(raw_count) if raw_count else 1

        include_symbols = input("Include symbols (!@#$..)? [Y/n]: ").strip().lower() != "n"
        include_digits = input("Include digits (0-9)? [Y/n]: ").strip().lower() != "n"
        exclude_similar = input("Exclude ambiguous characters (0, O, l, 1)? [y/N]: ").strip().lower() == "y"

        print("\nGenerated Passwords:")
        print("-" * 45)
        for idx in range(1, count + 1):
            pwd = generate_password(
                length=length,
                use_symbols=include_symbols,
                use_digits=include_digits,
                exclude_ambiguous=exclude_similar,
            )
            print(f"[{idx}] {pwd}")
        print("-" * 45)

    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(0)


if __name__ == "__main__":
    interactive_menu()
