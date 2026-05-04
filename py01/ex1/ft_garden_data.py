#!/usr/bin/env python3
"""
Docstrings:
Print the full list of plants from the inventary
And the test that only works if this is the main module
"""


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_print_inventory_list(plants: list) -> None:
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def ft_main() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]

    ft_print_inventory_list(plants)


if __name__ == "__main__":
    ft_main()
