#!/usr/bin/env python3
"""
Docstrings:
This module implements a garden ecosystem using dynamic polymorphism.
It defines a hierarchy of plant classes (Flower, Tree, Vegetable) inheriting
from a base 'Plant' class. Each subclass extends core functionality with
specific attributes, encapsulated setters for data integrity, and
specialized actions triggered through a polymorphic interface.
"""


class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0
        self.set_height(height)
        self._age = 0
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = float(height)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self._name} ({self.__class__.__name__}): "
              f"{round(self._height)}cm, {self._age} days", end="")

    def special_action(self) -> None:
        pass


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f", {self._color} color")

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def special_action(self) -> None:
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = 0.0
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        if trunk_diameter < 0:
            print(f"Error: Negative diameter {trunk_diameter} rejected")
        else:
            self._trunk_diameter = float(trunk_diameter)

    def show(self) -> None:
        super().show()
        print(f", {round(self._trunk_diameter)}cm diameter")

    def produce_shade(self) -> None:
        shade_area = round(self._height * self._trunk_diameter / 10_000, 2)
        print(f"{self._name} provides {shade_area} square meters of shade")

    def special_action(self) -> None:
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f", {self._harvest_season} harvest")

    def show_nutritional_info(self) -> None:
        print(f"{self._name} is rich in {self._nutritional_value}")

    def special_action(self) -> None:
        self.show_nutritional_info()


def main() -> None:
    print("--- 1. Testing Robustness (Error Handling) ---\n")
    weird_plant = Tree("Ghost", -10.5, -5, -2.0)
    weird_plant.show()
    print("\n")

    print("--- 2. Creating the Garden (Polymorphism) ---\n")
    garden: list[Plant] = [
        Flower("Rose", 25.4, 30, "Red"),
        Tree("Oak", 500.0, 3650, 45.8),
        Vegetable("Carrot", 15.0, 60, "Autumn", "Vitamin A"),
        Tree("Pine", 200.0, 730, -5.0)
    ]

    print("\n--- 3. Executing Garden Actions (Dynamic Dispatch) ---\n")
    for plant in garden:
        plant.show()
        print(" | Action: ", end="")
        plant.special_action()
        print("")


if __name__ == "__main__":
    main()
