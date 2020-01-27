from src.sdh.BaseSdh import BaseSdh


# Concrete implementation of sdh variant
class NormalizedSdh(BaseSdh):

    def _function(self, distances, df):
        return NotImplementedError()
