#!/usr/bin/env python3
"""
Docstrings:
It shows the growing of each plant in the garden
And the test that only works if this is the main module
"""


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def aging(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height)}cm, {self.age} days old")


def ft_plants_growing(plants: list, days: int) -> None:
    for _ in range(days-1):
        for plant in plants:
            plant.grow()
            plant.aging()


def ft_main() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    plants = [rose, sunflower]

    day = 1
    initial_heights = [p.height for p in plants]
    print(f"=== Day {day} ===")
    for plant in plants:
        plant.show()

    day = 7
    ft_plants_growing(plants, day)
    print(f"=== Day {day} ===")
    for plant, init_height in zip(plants, initial_heights):
        plant.show()
        print(f"Growth this week: +{plant.height - init_height}cm")


if __name__ == "__main__":
    ft_main()
