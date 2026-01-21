from collections import deque


def is_palindrome(text: str) -> bool:
    normalized = "".join(ch.lower() for ch in text if not ch.isspace())

    d = deque(normalized)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


def main() -> None:
    s = input("Enter string: ")
    print("Palindrome" if is_palindrome(s) else "Not palindrome")


if __name__ == "__main__":
    main()
