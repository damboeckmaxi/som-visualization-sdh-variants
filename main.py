import os
import argparse
from src.som import create_som
from src.som import read_weight_file, read_input_vector_file
from src.sdh import calc_weight_grid

## Define the argumentparser for this programm (including the --help-page)
def set_argumentparser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path_to_somtools', help='The absolute system path to SOMTools')
    parser.add_argument('dataset_prop_file', help='The name of the file containing the dataset-properties that get visualized'
                                        ', ending with .prop. (i.e.: 10clusters_large.prop)')
    parser.add_argument('input_vector_file', help='The name of the file containing the input-vectors'
                                                  ', ending with .vec (i.e.: 10clusters.vec)')
    parser.add_argument('-c', '--cpus', help='The number of cpus that can be used for processing', type=int)
    parser.add_argument('-v', '--variant', help='The SDH-variant that is used for the visualization, standard is equal',
                        choices=['equal', 'weighted', 'normalized', 'normalized-weighted'], default='equal')
    parser.add_argument('-n', '--n', help='The parameter n for the SDH-variant, i.e. match n-best matching units.',
                        default=1, type=int)
    return parser


## Parse the args needed for this step and create the som
def parse_args_and_create_som(args):
    path_to_somtools = args.path_to_somtools
    dataset_prop_file = args.dataset_prop_file
    cpus = args.cpus
    if not cpus > 1:
        cpus = 1
    create_som(path_to_somtools, dataset_prop_file, cpus)


def main():
    parser = set_argumentparser()
    args = parser.parse_args()
    parse_args_and_create_som(args)
    weight_vectors = read_weight_file(args.dataset_prop_file.split('.')[0])
    input_vectors = read_input_vector_file(args.input_vector_file)
    sdh_weight_grid = calc_weight_grid(weight_vectors, input_vectors, args.variant, args.n)
    print(sdh_weight_grid)

if __name__ == '__main__':
    main()
