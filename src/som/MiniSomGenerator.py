from src.som.SomGenerator import SomGenerator
from minisom import MiniSom
import pandas as pd
import numpy as np
from src.utils.FileUtils import read_input_vector_file


class MiniSomGenerator(SomGenerator):
    def __init__(self, dataset, som_x, som_y, sigma=0.3, learning_rate=0.6, iterations=100):
        super().__init__(dataset)
        self.som_x = som_x
        self.som_y = som_y
        self.sigma = sigma
        self.learning_rate = learning_rate
        self.iterations = iterations

    def _generate(self):
        input_vectors, vec_dim = read_input_vector_file(self.dataset)
        som = MiniSom(self.som_x, self.som_y, vec_dim, self.sigma, self.learning_rate)
        som.train_batch(input_vectors.to_numpy()[0], self.iterations)
        df = pd.DataFrame()
        for x in som.get_weights():
            df = df.append(pd.DataFrame(x))
        return df
