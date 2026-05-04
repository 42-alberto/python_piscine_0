import random


def ft_data_alchemist():

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    all_players_cap = [str.capitalize(player) for player in players]
    players_already_cap = [player for player in players if str.isupper(player[0])]
    rand_scores = {player: random.randint(0, 1000) for player in players}
    avrg_score = sum(rand_scores[key] for key in rand_scores) / len(rand_scores)
    high_scores = {key: rand_scores[key] for key in rand_scores if rand_scores[key] > avrg_score}

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_players_cap}")
    print(f"New list of capitalized names only: {players_already_cap}\n")
    print(f"Score dict: {rand_scores}")
    print(f"Score average is: {round(avrg_score, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
    