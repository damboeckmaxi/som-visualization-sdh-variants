import os
import subprocess
import os.path
from os import path


## check if the soms are already created and if not create and train them
def create_soms(path_to_somtools, datasets, cpus):
    for dataset in datasets:
        if not somfiles_exist(dataset):
            generate_soms(path_to_somtools, dataset, cpus)


def somfiles_exist(dataset):
    return path.exists(f'maps/{dataset}') and \
           len(os.listdir(f'maps/{dataset}')) > 0


def generate_soms(path_to_somtools, dataset, cpus=1):
    subprocess.Popen([f'{path_to_somtools}/somtoolbox.sh', 'GrowingSOM', f'datasets/{dataset}.prop', '--cpus', cpus],
                     stdout=subprocess.STDOUT,
                     stderr=subprocess.STDOUT)