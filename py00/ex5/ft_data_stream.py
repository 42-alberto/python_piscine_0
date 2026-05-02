import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release"]
    while True:
        event = (random.choice(players), random.choice(actions))
        yield event


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:

    while len(events) > 0:
        even_rand = random.choice(events)
        events.remove(even_rand)
        yield even_rand


def ft_data_stream() -> None:

    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for n in range(0,1000):
        player, action = next(event_gen)
        print(f"Event {n}: Player {player} did action {action}")
    even_list = [next(event_gen) for _ in range (10)]
    print(f"Built list of {len(even_list)} events: {even_list}")
    for event in consume_event(even_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {even_list}")


if __name__ == "__main__":
    ft_data_stream()