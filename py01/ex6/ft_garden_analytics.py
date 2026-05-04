#!/usr/bin/env python3
"""
Docstrings:

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

    def grow(self) -> None:
        self._height += 1
        print(f"{self._name} grew 1 cm")

    def get_type(self) -> str:
        return "regular"

    def show(self) -> None:
        print(f"{self._name} ({self.__class__.__name__}): "
              f"{round(self._height)}cm, {self._age} days", end="")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: float, age: int,
                 flower_color: str) -> None:
        super().__init__(name, height, age)
        self._flower_color = flower_color

    def bloom(self) -> str:
        return f"{self._flower_color} flowers (blooming)"

    def get_type(self) -> str:
        return "flowering"

    def show(self) -> None:
        super().show()
        print(f" {self.bloom()}", end="")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: float, age: int, flower_color: str,
                 prize_points: int):
        super().__init__(name, height, age, flower_color)
        self._prize_points = prize_points

    def get_type(self) -> str:
        return "prize"

    def show(self) -> None:
        super().show()
        print(f" Prize points: {self._prize_points}", end="")


class GardenManager():
    _total_gardens = 0

    def __init__(self, owner: str) -> None:
        self._owner = owner
        self._plants: list[Plant] = []
        GardenManager._total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self._plants.append(plant)
        print(f"Added {plant._name} to {self._owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self._owner} is helping all plants grow...")
        for plant in self._plants:
            plant.grow()

    def report(self) -> None:
        print(f"\n=== {self._owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self._plants:
            plant.show()
            print("")
        stats = self.GardenStats(self)
        stats.calculate_stats()

    def calculate_score(self) -> float:
        score = 0
        for plant in self._plants:
            score += plant._height
        return round(score)

    class GardenStats:
        def __init__(self, manager: "GardenManager") -> None:
            self._manager = manager

        def calculate_stats(self) -> None:
            _regular = 0
            _flowering = 0
            _prize = 0
            _plant_count = 0
            _total_growth = 0

            for plant in self._manager._plants:
                if plant.get_type() == "regular":
                    _regular += 1
                elif plant.get_type() == "flowering":
                    _flowering += 1
                elif plant.get_type() == "prize":
                    _prize += 1
                _plant_count += 1
                _total_growth += plant._height
            print(f"\nPlants added: {_plant_count}, "
                  f"Total growth: {_total_growth}cm")
            print(f"Plant types: {_regular} regular, "
                  f"{_flowering} flowering, {_prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls._total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    # 1. Crear redes de jardines (Prueba de @classmethod)
    garden1 = GardenManager("Alice")
    garden2 = GardenManager("Bob")

    # 2. Crear plantas de diferentes tipos
    oak = Plant("Oak Tree", 100.5, 365)
    rose = FloweringPlant("Red Rose", 25.0, 30, "Red")
    sunflower = PrizeFlower("Golden Sunflower", 50.0, 60, "Yellow", 50)

    # 3. Probar validaciones de seguridad (Prueba de setters y @staticmethod)
    print("Testing Security Validations:")
    print(f"Height validation (15cm): {GardenManager.validate_height(15)}")
    print(f"Height validation (-5cm): {GardenManager.validate_height(-5)}\n")

    # 4. Gestionar el primer jardín
    print("--- Filling Alice's Garden ---")
    garden1.add_plant(oak)
    garden1.add_plant(rose)
    garden1.add_plant(sunflower)

    # 5. Generar Reporte (Prueba de Inner Class GardenStats y Polimorfismo)
    garden1.report()
    garden2.report()

    # 6. Acción masiva (Prueba de grow_all)
    garden1.grow_all()
    garden1.report()

    # 7. Resultados de puntuación (Prueba de calculate_score)
    print(f"\n{garden1._owner}'s garden score: "
          f"{garden1.calculate_score()} pts")

    # 8. Estado global del sistema
    print("\n--- Global System Status ---")
    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
