"""
Docstrings:
Inform if a plant is ready to harvest or not, age > 60 days
And the test that only works if this is the main module
"""


def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


if __name__ == "__main__":
    ft_plant_age()
