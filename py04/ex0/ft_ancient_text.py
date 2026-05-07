import sys
import typing


def ft_print_raw_file(file: str) -> None:
    print(f"Accessing file '{file}'")
    text: typing.TextIO = open(file, "rt")
    print("---\n")
    print(f"{text.read()}")
    print("---")

    text.close()
    print(f"File '{file}' closed\n")


def ft_ancient_text() -> None:

    args: list[str] = sys.argv
    if len(args) != 2:
        print(f"Usage: {args[0]} <file>\n")
        return
    file: str = args[1]

    print("=== Cyber Archives Recovery ===")

    try:
        ft_print_raw_file(file)

    except PermissionError as e:
        print(f"Error opening file '{file}': {e} Permission denied:\n '{file}'")

    except IOError as e:
        print(f"Error opening file '{file}': {e}\n")


if __name__ == "__main__":
    ft_ancient_text()
