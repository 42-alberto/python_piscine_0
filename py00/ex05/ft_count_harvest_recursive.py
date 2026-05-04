"""
Docstrings:
count days and advise when harvest
And the test that only works if this is the main module
"""


def ft_count_days_recursive(days) -> None:
    if days < 1:
        return
    if days > 1:
        ft_count_days_recursive(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    ft_count_days_recursive(int(input("Days until harvest: ")))
    print("Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_recursive()
