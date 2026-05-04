import random


def gen_player_achievements(archiv: list[str]) -> set[str]:

    num_rand = random.randint(6, 9)
    return set(random.sample(archiv, num_rand))


def ft_achievement_tracker() -> None:

    players = ["Alice", "Bob", "Charlie", "Dylan"]
    archiv = ['Crafting Genius', 'Strategist', 'World Savior',
                'Speed Runner', 'Survivor', 'Master Explorer',
                'Treasure Hunter', 'Unstoppable', 'First Steps',
                'Collector Supreme', 'Untouchable', 'Sharp Mind',
                'Boss Slayer']
    players_data: list[set[str]] = []

    for player in players:
        players_data += [gen_player_achievements(archiv)]
    common_data = set.intersection(*players_data)
    
    print("=== Achievement Tracker System ===\n")

    for i in range(len(players)):
        print(f"Player {players[i]}: {players_data[i]}")
    print(f"\nAll distinct achievements: {archiv}\n")
    print(f"Common achievements: {common_data}\n")
    for i in range(len(players)):
        unique = players_data[i]
        for j in range(len(players)):
            if j == i:
                continue
            unique = set.difference(unique, players_data[j])
        print(f"Only {players[i]} has: {unique}")
    
    print("")
    for i in range(len(players)):
        missing = set.difference(set(archiv), players_data[i])
        print(f"{players[i]} is missing: {missing}")

if __name__ == "__main__":
    ft_achievement_tracker()
