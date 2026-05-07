import sys
import typing


def ft_print_raw_file(text: str, file: str) -> None:

    print("---\n")
    print(f"{text}")
    print("---")


def ft_transform_data(text: str) -> str:

    print("Transform data:")

    lines: list[str] = text.splitlines()
    new_lines: list[str] = [f"{line}#" for line in lines]
    new_text: str = "\n".join(new_lines) + "\n"
    print("---\n")
    print(new_text)
    print("---")
    return new_text


def ft_save_data(new_text: str, f_name: str) -> None:

    try:
        file: typing.TextIO = open(f_name, "wt")
        file.write(new_text)
        file.close()
    except OSError as e:
        print(f"Error opening file '{f_name}': {e}\n")
        print("Data not saved.")


def ft_create_file(text: str) -> None:

    new_text: str = ft_transform_data(text)
    f_name: str = input("Enter new file name (or empty):")

    if f_name:
        print(f"Saving data to '{f_name}'")
        ft_save_data(new_text, f_name)
        print(f"Data saved in file '{f_name}'.")
    else:
        print("Not saving data.")


def ft_archive_creation() -> None:

    args: list[str] = sys.argv
    if len(args) != 2:
        print(f"Usage: {args[0]} <file>\n")
        return

    file: str = args[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file}'")

    try:
        text: typing.TextIO = open(file, "rt")
        text_read: str = text.read()
        ft_print_raw_file(text_read, file)

        text.close()
        print(f"File '{file}' closed\n")

        ft_create_file(text_read)

    except PermissionError as e:
        print(f"Error opening file '{file}': {e} Permission denied:\n '{file}'")

    except OSError as e:
        print(f"Error opening file '{file}': {e}\n")


if __name__ == "__main__":
    ft_archive_creation()

