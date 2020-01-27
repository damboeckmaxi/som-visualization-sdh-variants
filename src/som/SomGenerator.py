from os import path, listdir


def som_files_exist(dataset):
    return path.exists(f'../maps/{dataset}') and len(listdir(f'../maps/{dataset}')) > 0


# Base class to generate a som
class SomGenerator:
    def __init__(self, dataset):
        self.dataset = dataset

    def generate(self, force=False):
        if force or not som_files_exist(self.dataset):
            self._generate()

    def _generate(self):
        pass
