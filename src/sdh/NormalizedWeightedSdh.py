from src.sdh.BaseSdh import BaseSdh


# Concrete implementation of sdh variant
class NormalizedWeightedSdh(BaseSdh):

    def _function(self, distances, df):
        return NotImplementedError()
