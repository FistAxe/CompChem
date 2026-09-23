"""A tiny smoke test for the repository's Python setup."""


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def main() -> None:
    result = add(2, 3)
    assert result == 5
    print(f"Dummy Python test passed: 2 + 3 = {result}")


if __name__ == "__main__":
    main()
