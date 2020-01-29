from os import system, chdir
from som.SomGenerator import SomGenerator


# Concrete implementation of the generator
class ToolboxGenerator(SomGenerator):
    def __init__(self, dataset, path_to_toolbox, cpus=1):
        super().__init__(dataset)
        self.path_to_toolbox = path_to_toolbox
        self.cpus = cpus

    def _generate(self):
        chdir('../somtoolbox')
        system(f'{self.path_to_toolbox}/somtoolbox.sh GrowingSOM ../datasets/{self.dataset}.prop --cpus {self.cpus}')
        chdir('../src')
