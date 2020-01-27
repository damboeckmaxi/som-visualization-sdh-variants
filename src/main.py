import os
import argparse

from src.som.ToolboxGenerator import ToolboxGenerator


# Define the argument parser for this program (including the --help-page)
def set_argument_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path_to_somtools', help='The absolute system path to SOMTools')
    parser.add_argument('dataset', help='The name of the dataset-prop file that gets '
                                        'visualized without .prop (i.e.: 10clusters_large)')
    parser.add_argument('-c', '--cpus', help='The number of cpus that can be used for processing', type=int)
    return parser


# Parse the args needed for this step and create the som
def parse_args_and_create_som(parser):
    args = parser.parse_args()
    path_to_somtools = args.path_to_somtools
    dataset = args.dataset
    cpus = args.cpus
    if cpus is None or not cpus > 1:
        cpus = 1
    generator = ToolboxGenerator(dataset, path_to_somtools, cpus)
    generator.generate()


def main():
    parser = set_argument_parser()
    parse_args_and_create_som(parser)


if __name__ == '__main__':
    main()
