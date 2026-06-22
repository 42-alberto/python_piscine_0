#!/usr/bin/env python

def ft_count_days_recursive(days: int) -> None:
    if days < 1:
        return
    if days > 1:
        ft_count_days_recursive(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    ft_count_days_recursive(int(input("Days until harvest: ")))
    print("Harvest time!")
