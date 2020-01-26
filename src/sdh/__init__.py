## Calculate the weight grid for the given SDH-type for the given input- and weight vectors, return DataFrame
import sys

import numpy
import pandas as pd
from scipy.spatial import distance


def calc_weight_grid(weight_vectors, input_vectors, sdh_variant, n):
    return __iterate_input_vectors__(weight_vectors.copy(deep=True), input_vectors, sdh_variant, n)


def __get_df_from_weight_vectors__(weight_vectors):
    return pd.DataFrame().reindex_like(weight_vectors)


def __iterate_input_vectors__(weight_vectors, input_vectors, sdh_variant, n):
    df = __get_df_from_weight_vectors__(weight_vectors)
    df = df.fillna(0)
    variants = {
        'equal': __calc_weight_grid_equal__,
        'weighted': __calc_weight_grid_weighted__,
        'normalized': __calc_weight_grid_normalized__,
        'normalized-weighted': __calc_weight_grid_normalized_weighted__
    }
    func = variants.get(sdh_variant)
    input_vectors_tsf = input_vectors.transpose()
    for index, row in input_vectors_tsf.iterrows():
        distances = __calc_distances_vector_to_weight_vectors__(row[0], weight_vectors)
        df = func(distances, df, n)
        print (f'Processing input_vectur nr {index}')
        ## TODO verbose output parameter with all processing-progress information
    return df


def __calc_weight_grid_equal__(distances, df, n):
    for i in range(0,n):
        min_idx = distances.idxmin()
        min_val = distances.min()
        absolute_min = min_val.idxmin()
        df[absolute_min][min_idx[absolute_min]] += 1
        distances[absolute_min][min_idx[absolute_min]] = sys.maxsize
        ## TODO optimize finding minimum
    return df


def __calc_weight_grid_weighted__(distances, df, n):
    # TODO implement
    pass


def __calc_weight_grid_normalized__(distances, df, n):
    # TODO implement
    pass


def __calc_weight_grid_normalized_weighted__(distances, df, n):
    # TODO implement
    pass


def __calc_distances_vector_to_weight_vectors__(vector, weight_vectors):
    return weight_vectors.applymap(lambda x: __calc_vector_distance__(x, vector))


def __calc_vector_distance__(vec1, vec2):
    return distance.euclidean(vec1, vec2)
