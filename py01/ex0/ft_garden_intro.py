#!/usr/bin/env python3

class plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

def ft_garden_intro() -> None:
    name: str = "Rose"
    height: int = 25
    age: int = 30

    plant1: plant = plant(name, height, age)
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant1.name}")
    print(f"Height: {plant1.height}cm")
    print(f"Age: {plant1.age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()


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
