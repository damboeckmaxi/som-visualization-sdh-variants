import pandas as pd
from sdh.BaseSdh import BaseSdh


# Concrete implementation of sdh variant
class EqualSdh(BaseSdh):

    def _function(self, distances, df):
        order_df = pd.DataFrame()
        order_df[0] = distances[0]
        order_df[1] = 0
        for x in range(1, len(distances.columns)):
            new_col = pd.DataFrame()
            new_col[0] = distances[x]
            new_col[1] = x
            order_df = order_df.append(new_col)
        order_df = order_df.nsmallest(self.n, 0)
        for i in range(0, self.n):
            df[order_df.iloc[i][1]][order_df.iloc[i].name] += 1
        return df
