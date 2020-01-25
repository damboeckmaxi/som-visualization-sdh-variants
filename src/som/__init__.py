import os
import os.path
from os import path


## check if the som is already created and if not create and train it
def create_som(path_to_somtools, dataset, cpus=1):
    if not somfiles_exist(dataset):
        generate_soms(path_to_somtools, dataset, cpus)


def somfiles_exist(dataset):
    return path.exists(f'maps/{dataset}') and \
           len(os.listdir(f'maps/{dataset}')) > 0


def generate_soms(path_to_somtools, dataset, cpus=1):
    os.system(f'{path_to_somtools}/somtoolbox.sh GrowingSOM datasets/{dataset}.prop --cpus {cpus}')
