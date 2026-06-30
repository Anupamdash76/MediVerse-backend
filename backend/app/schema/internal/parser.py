from dataclasses import dataclass
from typing import List

import pandas as pd


@dataclass
class SymptomMatch:
    """
    Represents one semantic symptom match.
    """

    input: str
    matched: str
    score: float


@dataclass
class ParserResult:
    """
    Result returned by the SymptomParser.
    """

    feature_vector: pd.DataFrame
    matches: List[SymptomMatch]