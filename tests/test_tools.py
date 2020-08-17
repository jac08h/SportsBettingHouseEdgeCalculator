import tools as he_calc_tools


def test_get_odds_from_text():
    text = """FC Sevilla3.07
Draw3.22
Manchester U.2.46"""
    odds = [3.07, 3.22, 2.46]
    assert he_calc_tools.get_odds_from_text(text) == odds

    text = ""
    assert he_calc_tools.get_odds_from_text(text) == []
