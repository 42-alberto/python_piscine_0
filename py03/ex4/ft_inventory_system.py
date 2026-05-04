import sys


def ft_parser_arg(items: list[str]) -> dict[str, int]:

    inventory = dict()
    for item in items:
        object = item.split(":")
        if len(object) != 2:
            print(f"Error - invalid parameter '{item}'")
            continue
        try:
            int(object[1])
        except:
            print(f"Quantity error for '{object[0]}': invalid "
                   f"literal for int() with base 10: '{object[1]}'")
            continue
        if object[0] in inventory.keys():
            print(f"Redundant item '{object[0]}' - discarding")
            continue
        inventory[object[0]] = int(object[1])
    return inventory


def ft_inventory_system() -> None:

    print("=== Inventory System Analysis ===")
    inventory = ft_parser_arg(sys.argv[1:])

    if len(sys.argv) == 1:
        print("Empty inventory")
        inventory.update({"Magic_item": 1}) 
        print(f"Updated inventory: {inventory}")
        return

    total_items = sum(inventory.values())
    m_abund = None
    l_abun = None
    for item in inventory:
        if m_abund is None or inventory[m_abund] < inventory[item]:
            m_abund = item
        if l_abun is None or inventory[l_abun] > inventory[item]:
            l_abun = item
    
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {total_items}")
    for item in inventory:
        percent = round(100 * inventory[item] / total_items, 1) 
        print(f"Item {item} represents {percent}%")
    print(f"Item most abundant: {m_abund} with quantity {inventory[m_abund]}")
    print(f"Item least abundant: {l_abun} with quantity {inventory[l_abun]}")
    inventory.update({"Magic_item": 1}) 
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()