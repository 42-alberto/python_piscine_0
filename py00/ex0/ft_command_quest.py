import sys


def ft_command_quest() -> None:
    arg_len = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if arg_len == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_len - 1}")
    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {arg_len}")


if __name__ == "__main__":
    ft_command_quest()
