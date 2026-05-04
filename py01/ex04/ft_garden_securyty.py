#!/usr/bin/env python3
"""
Docstrings:
Securely set and get plant values
And the test that only works if this is the main module
"""


class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


def ft_main():
    plant = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    print(f"Height updated: {plant.get_height()}cm")
    print(f"Age updated: {plant.get_age()} days")
    plant.set_height(-24)
    plant.set_age(-24)


if __name__ == "__main__":
    ft_main()
