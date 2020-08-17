import re
from typing import List

float_pattern = re.compile(r"\d+\.\d+")


def get_odds_from_text(text: str) -> List[float]:
    all_finds = re.findall(float_pattern, text)
    return list(map(float, all_finds))
