from src.sdh.BaseSdh import BaseSdh


# Concrete implementation of sdh variant
class WeightedSdh(BaseSdh):

    def _function(self, distances, df):
        return NotImplementedError()
