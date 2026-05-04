"""
Docstrings:
Inform if plants need water, last watering > 2 days
And the test that only works if this is the main module
"""


def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


if __name__ == "__main__":
    ft_water_reminder()
