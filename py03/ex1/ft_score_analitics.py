import sys


def ft_score_analitycs() -> None:
    scores_processed = []
    players = 0
    total = 0
    for arg in sys.argv[1:]:
        try:
            arg = int(arg)
            scores_processed.append(arg)
            players += 1
            total += arg
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if players == 0:
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores_processed}")
    print(f"Total players: {players}")
    print(f"Total score: {total}")
    print(f"Average score: {total / players}")
    high = scores_processed[0]
    low = scores_processed[0]
    for score in scores_processed:
        high = max(high, score)
        low = min(low, score)
    print(f"Hight score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    ft_score_analitycs()
