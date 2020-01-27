import os
import argparse

from src.som.ToolboxGenerator import ToolboxGenerator
from src.utils.FileUtils import read_weight_file, read_input_vector_file


# Define the argument parser for this program (including the --help-page)
def set_argument_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path_to_somtools', help='The absolute system path to SOMTools')
    parser.add_argument('dataset_prop_file',
                        help='The name of the file containing the dataset-properties that get visualized'
                             ', ending with .prop. (i.e.: 10clusters_large.prop)')
    parser.add_argument('input_vector_file', help='The name of the file containing the input-vectors'
                                                  ', ending with .vec (i.e.: 10clusters.vec')
    parser.add_argument('-c', '--cpus', help='The number of cpus that can be used for processing', type=int)
    return parser


# Parse the args needed for this step and create the som
def parse_args_and_create_som(args):
    path_to_somtools = args.path_to_somtools
    dataset_prop_file = args.dataset_prop_file
    cpus = args.cpus
    if cpus is None or not cpus > 1:
        cpus = 1
    generator = ToolboxGenerator(dataset_prop_file, path_to_somtools, cpus)
    generator.generate()


def main():
    parser = set_argument_parser()
    args = parser.parse_args()
    parse_args_and_create_som(args)
    weight_vectors = read_weight_file(args.dataset_prop_file.split('.')[0])
    input_vectors = read_input_vector_file(args.input_vector_file)
    print(weight_vectors)
    print(input_vectors)


if __name__ == '__main__':
    main()
