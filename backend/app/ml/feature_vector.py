import numpy as np
import pandas as pd


class FeatureVector:
    """
    Represents the feature vector used by
    the ML model for prediction.
    """

    def __init__(self, features):

        self.features = features

        self._df = pd.DataFrame(
            np.zeros((1, len(features))),
            columns=features,
        )

    def activate(self, feature: str):
        """
        Activate a symptom feature.
        """

        if feature in self._df.columns:
            self._df.loc[0, feature] = 1

    def deactivate(self, feature: str):
        """
        Deactivate a symptom feature.
        """

        if feature in self._df.columns:
            self._df.loc[0, feature] = 0

    def is_active(self, feature: str) -> bool:
        """
        Check whether a feature is active.
        """

        return bool(self._df.loc[0, feature])

    def to_dataframe(self):
        """
        Return the underlying DataFrame.
        """

        return self._df

    def active_features(self):
        """
        Return only active symptoms.
        """

        return self._df.loc[
            :,
            (self._df != 0).any(axis=0)
        ]