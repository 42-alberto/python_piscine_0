def secure_archive(
        f_name: str,
        action: str,
        text = ""
        )-> tuple[True|False, str]:

    action = action.lower()

    try:
        if action == "r":
            with open(f_name, "rt") as file:
                return (True, file.read()) 

        if action == "w":
            with open(f_name, "wt") as new_file:
                new_file.write(text)
                return(True, "Content successfully written to file")

    except OSError as e:
        return (False, str(e))


def ft_vault_security() -> None:

    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive("/not/existing/file", "r")}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive("../forbiden_text.txt", "R")}\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive("../ancient_fragment.txt", "r")}\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive("../borrar.txt", "w", "Surprise!!!")}\n")


if __name__ == "__main__":
    ft_vault_security()
