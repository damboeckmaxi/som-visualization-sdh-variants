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
    order_df = pd.DataFrame()
    order_df[0] = distances[0]
    order_df[1] = 0
    for x in range(1, len(distances.columns)):
        new_col = pd.DataFrame()
        new_col[0] = distances[x]
        new_col[1] = x
        order_df = order_df.append(new_col)
    order_df = order_df.nsmallest(n, 0)
    for i in range(0,n):
        df[order_df.iloc[i][1]][order_df.iloc[i].name] += 1
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
