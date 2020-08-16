from typing import Iterable


def calculate_house_edge(odds_iterable: Iterable[float]):
    probabilities_sum = sum(map(probability_from_odds, odds_iterable))
    return probabilities_sum - 1


def probability_from_odds(odds: float):
    return 1 / odds


if __name__ == '__main__':
    odds = [2.22, 7.7, 1.92]
    result = calculate_house_edge(odds)
    print(result)
