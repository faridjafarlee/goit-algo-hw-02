def check_brackets(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    opens = set(pairs.values())
    stack = []

    for ch in s:
        if ch in opens:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def main() -> None:
    samples = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
    ]

    for t in samples:
        print(f"{t}: {'Симетрично' if check_brackets(t) else 'Несиметрично'}")

    user = input("\nEnter your string: ").strip()
    if user:
        print("Симетрично" if check_brackets(user) else "Несиметрично")


if __name__ == "__main__":
    main()
