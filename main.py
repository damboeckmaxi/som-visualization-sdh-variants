import argparse

from src.sdh.EqualSdh import EqualSdh
from src.sdh.NormalizedSdh import NormalizedSdh
from src.sdh.NormalizedWeightedSdh import NormalizedWeightedSdh
from src.sdh.WeightedSdh import WeightedSdh
from src.som.ToolboxGenerator import ToolboxGenerator
from src.som.MiniSomGenerator import MiniSomGenerator
from src.utils.FileUtils import read_weight_file, read_input_vector_file
from src.utils.Visualization import visualize


# Define the argument parser for this program (including the --help-page)
def set_argument_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path_to_somtools', help='The absolute system path to SOMTools')
    parser.add_argument('dataset_prop_file',
                        help='The name of the file containing the dataset-properties that get visualized'
                             ', ending without .prop. (i.e.: 10clusters_large)')
    # TODO either both files with or both without fileending (.prop, .vec)
    parser.add_argument('input_vector_file', help='The name of the file containing the input-vectors'
                                                  ', ending without .vec (i.e.: 10clusters)')
    parser.add_argument('-c', '--cpus', help='The number of cpus that can be used for processing', type=int)
    parser.add_argument('-v', '--variant', help='The SDH-variant that is used for the visualization, standard is equal',
                        choices=['equal', 'weighted', 'normalized', 'normalized-weighted'], default='equal')
    parser.add_argument('-n', '--n', help='The parameter n for the SDH-variant, i.e. match n-best matching units.',
                        default=1, type=int)
    return parser


# Parse the args needed for this step and create the som
def parse_args_and_create_som(args):
    path_to_somtools = args.path_to_somtools
    dataset_prop_file = args.dataset_prop_file
    cpus = args.cpus
    if cpus is None or not cpus > 1:
        cpus = 1
    # generator = ToolboxGenerator(dataset_prop_file, path_to_somtools, cpus)
    generator = MiniSomGenerator(args.dataset_prop_file, 20, 25)
    return generator.generate()


def choose_variant(variant_name, weight_vectors, input_vectors, n):
    variants = {
        'equal': EqualSdh(weight_vectors, input_vectors, n),
        'weighted': WeightedSdh(weight_vectors, input_vectors, n),
        'normalized': NormalizedSdh(weight_vectors, input_vectors, n),
        'normalized-weighted': NormalizedWeightedSdh(weight_vectors, input_vectors, n)
    }
    return variants.get(variant_name)


def main():
    parser = set_argument_parser()
    args = parser.parse_args()
    som = parse_args_and_create_som(args)
    if som is not None:
        weight_vectors = som
    else:
        weight_vectors = read_weight_file(args.dataset_prop_file.split('.')[0])
    input_vectors, vec_dim = read_input_vector_file(args.input_vector_file)
    variant = choose_variant(args.variant, weight_vectors, input_vectors, args.n)
    sdh_weight_grid = variant.calculate()
    visualize(sdh_weight_grid)


if __name__ == '__main__':
    main()