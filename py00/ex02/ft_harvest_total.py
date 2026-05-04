"""
Docstrings:
Calculate the sum of three work days
And the test that only works if this is the main module
"""


def ft_harvest_total() -> None:
    total = 0
    i = 0
    while i < 3:
        i += 1
        aux = int(input(f"Day {i} harvest: "))
        total += aux
    print(f"Total harvest: {total}")


if __name__ == "__main__":
    ft_harvest_total()
