import gzip
import os
import os.path
import pandas as pd
from os import path


## check if the som is already created and if not create and train it
def create_som(path_to_somtools, dataset_prop_file, cpus=1):
    if not __somfiles_exist__(dataset_prop_file.split('.')[0]):
        __generate_soms__(path_to_somtools, dataset_prop_file, cpus)


def __somfiles_exist__(dataset):
    return path.exists(f'maps/{dataset}') and \
           len(os.listdir(f'maps/{dataset}')) > 0


def __generate_soms__(path_to_somtools, dataset_prop_file, cpus=1):
    os.system(f'{path_to_somtools}/somtoolbox.sh GrowingSOM datasets/{dataset_prop_file} --cpus {cpus}')


## Read the input-vector file with the trainingsdata and export as one-dimensional Dataframe containing the vectors
def read_input_vector_file(input_vector_file):
    df = pd.DataFrame()
    with open(f'datasets/{input_vector_file}', 'rb') as file:
        df = __read_vector_file_to_df__(df, file)
    file.close()
    return df


## Read the trained weight-vectors file and export as a DataFrame with corresponding weight-vectors
def read_weight_file(dataset):
    df = pd.DataFrame()
    with gzip.open(f'maps/{dataset}/{dataset}.wgt.gz', 'rb') as file:
        df = __read_vector_file_to_df__(df, file)
    file.close()
    return df


def __read_vector_file_to_df__(df, file):
    xdim, ydim, vec_dim, xunit, yunit = 0, 0, 0, 0, 0
    for byte in file:
        line = byte.decode('UTF-8')
        if line.startswith('$'):
            xdim, ydim, vec_dim = __parse_vector_file_metadata__(line, xdim, ydim, vec_dim)
            if xdim > 0 and ydim > 0 and len(df.columns) == 0:
                df = pd.DataFrame(index=range(0, ydim), columns=range(0, xdim))
        else:
            if len(df.columns) == 0 or vec_dim == 0:
                raise ValueError('Weight file has no correct Dimensional information.')
            xunit, yunit = __parse_weight_file_data__(line, xdim, ydim, vec_dim, xunit, yunit, df)
    return df


def __parse_weight_file_data__(line, xdim, ydim, vec_dim, xunit, yunit, df):
    cell=[]
    splitted=line.split(' ')
    for i in range(0, vec_dim):
        cell.append(float(splitted[i]))
    if xunit < xdim:
        df[xunit][yunit] = cell
    else:
        xunit = 0
        yunit += 1
        df[xunit][yunit] = cell
    xunit += 1
    if yunit >= ydim:
        raise ValueError('The input-vector file does not match its unit-dimension.')
    return xunit, yunit


def __parse_vector_file_metadata__(line, xdim, ydim, vec_dim):
    splitted = line.split(' ')
    if splitted[0] == '$XDIM':
        xdim = int(splitted[1])
    elif splitted[0] == '$YDIM':
        ydim = int(splitted[1])
    elif splitted[0] == '$VEC_DIM':
        vec_dim = int(splitted[1])
    return xdim, ydim, vec_dim
