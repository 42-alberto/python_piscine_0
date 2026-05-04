"""
Docstrings:
Prints the area from length and width provided by the user.
And the test that only works if this is the main module
"""


def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")


if __name__ == "__main__":
    ft_plot_area()
