import math


def get_player_pos(coordinates: str) -> tuple[float, float, float]:

    x = None
    y = None
    z = None
    parts = coordinates.split(",")
    for part in parts:
        part.strip()
        try:
            if x is None:
                x = float(part)
            elif y is None:
                y = float(part)
            elif z is None:
                z = float(part)
            else:
                print("Error: To many parameters, only 3 needed")
                return None
        except ValueError:
            if x is None:
                print("Invalid syntax")
            else:
                print(f"Error on parameter '{part}': "
                      f"could not convert string to float: '{part}'")
            return None
    possition = (x, y, z)
    return possition


def ft_coordinate_system() -> None:

    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    point1 = None
    while (point1 is None):
        coord = input("Enter new coordinates as floats in format 'x,y,z': ")
        point1 = get_player_pos(coord)
    print(f"Got a first tuple: {point1}")
    print(f"It includes: X={point1[0]}, Y={point1[1]}, Z={point1[2]}")
    distance = math.sqrt(point1[0]**2 + point1[1]**2 + point1[2]**2)
    print(f"Distance to center: {distance:.4f}\n")

    print("Get a second set of coordinates")
    point2 = None
    while (point2 is None):
        coord = input("Enter new coordinates as floats in format 'x,y,z': ")
        point2 = get_player_pos(coord)
    distance = math.sqrt((point1[0] - point2[0])**2 +
                         (point1[1] - point2[1])**2 +
                         (point1[2] - point2[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    ft_coordinate_system()
