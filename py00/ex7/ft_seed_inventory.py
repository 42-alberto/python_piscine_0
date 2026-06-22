#!/usr/bin/env python

def ft_seed_inventory(seed_tipe: str, quantity: int, unit: str) -> None:
    unit = unit.lower()
    seed_tipe = seed_tipe.lower()
    seed_tipe = seed_tipe.capitalize()
    if unit == "packets":
        print(f"{seed_tipe} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_tipe} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_tipe} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
