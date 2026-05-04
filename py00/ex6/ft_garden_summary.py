"""
Docstrings:
Ask for name and number of plants and show the data
And the test that only works if this is the main module
"""


def ft_garden_summary() -> None:
    name = input("Enter garden name: ")
    plants_num = int(input("Enter number of plants: "))
    print(f"Garden: {name}")
    print(f"Plants: {plants_num}")
    print("Status: Growing well!")


if __name__ == "__main__":
    ft_garden_summary()
