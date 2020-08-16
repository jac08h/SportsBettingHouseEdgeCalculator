import house_edge_calculator as he_calc


def test_probability_from_odds():
    assert he_calc.probability_from_odds(1.9) == 1 / 1.9
    assert he_calc.probability_from_odds(2.5) == 1 / 2.5


def test_calculate_house_edge():
    odds = [2.6, 7.8, 2.1]
    correct_result = sum([1 / i for i in odds]) - 1
    assert he_calc.calculate_house_edge(odds) == correct_result
