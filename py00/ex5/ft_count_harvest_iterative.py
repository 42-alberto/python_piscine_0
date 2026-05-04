"""
Docstrings:
count days and advise when harvest
And the test that only works if this is the main module
"""


def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day: {i}")
    print("Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_iterative()
