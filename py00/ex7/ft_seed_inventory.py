"""
Docstrings:
Ask for seeds, quantities and units and show the data
And the test that only works if this is the main module
"""


def ft_seed_inventory(seed_tipe: str, quantity: int, unit: str) -> None:
    unit = unit.lower()
    seed_tipe = seed_tipe.capitalize()
    if unit == "packets":
        print(f"{seed_tipe} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_tipe} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_tipe} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")


if __name__ == "__main__":
    seed_tipe = input("Tipe of seed: ")
    unit = input("Format (packets, grams, area): ")
    quantity = int(input("Number of units: "))
    ft_seed_inventory(seed_tipe, quantity, unit)
