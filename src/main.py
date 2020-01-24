import sys

from src.som import create_soms


def main():
    ## TODO check for validity of arguments, change to command line structure (i.e. -cpus 3,...)
    path_to_somtools = sys.argv[1]
    datasets = sys.argv[2].split(',')
    cpus = sys.argv[3]
    create_soms(path_to_somtools, datasets, cpus)



if __name__ == '__main__':
    main()