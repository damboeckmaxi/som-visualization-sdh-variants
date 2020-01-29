import pandas as pd
from scipy.spatial import distance


def _get_df_from_weight_vectors(weight_vectors):
    return pd.DataFrame().reindex_like(weight_vectors)


def _calc_distances_vector_to_weight_vectors(vector, weight_vectors):
    return weight_vectors.applymap(lambda x: _calc_vector_distance(x, vector))


def _calc_vector_distance(vec1, vec2):
    return distance.euclidean(vec1, vec2)


# Base class for sdh variants
class BaseSdh:
    def __init__(self, weight_vectors, input_vectors, n):
        self.weight_vectors = weight_vectors.copy(deep=True)
        self.input_vectors = input_vectors
        self.n = n

    def calculate(self):
        df = _get_df_from_weight_vectors(self.weight_vectors)
        df = df.fillna(0)
        input_vectors_tsf = self.input_vectors.transpose()
        for index, row in input_vectors_tsf.iterrows():
            distances = _calc_distances_vector_to_weight_vectors(row[0], self.weight_vectors)
            df = self._function(distances, df)
            # print(f'Processing input_vector nr {index}')
            # TODO verbose output parameter with all processing-progress information
        return df

    def _function(self, distances, df):
        return NotImplementedError()
