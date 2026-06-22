#!/usr/bin/env python3

def ft_harvest_total() -> None:
    total: int = 0
    i: int = 0
    while i < 3:
        i += 1
        total += int(input(f"Day {i} harvest: "))
    print(f"Total harvest: {total}")
