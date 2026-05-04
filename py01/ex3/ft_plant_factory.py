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


plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 360),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 145),
        ("Fern", 15, 120)
        ]


def ft_main() -> None:
    plants = [Plant(n, h, a) for n, h, a in plant_data]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    ft_main()
