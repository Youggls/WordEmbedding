import numpy as np

class word2vec:
    def __init__(self, size, skip_gram=3, n_gram=5):
        self.__hidden_size = size
