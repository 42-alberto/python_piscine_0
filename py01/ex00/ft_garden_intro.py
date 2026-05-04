#!/usr/bin/env python3
"""
Docstrings:
Create an instance of a rose usint the class Plant
And the test that only works if this is the main module
"""


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_main() -> None:
    rose = Plant("Rose", 24, 30)
    print("=== Welcome to my Garden ===")
    print(f"Plant: {rose.name}")
    print(f"Height: {rose.height}cm")
    print(f"Age: {rose.age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_main()
