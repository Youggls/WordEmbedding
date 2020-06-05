import numpy as np
import pickle
from onehot import onehot

def save_onehot(obj, path):
    file = open(path, mode='wb')
    pickle.dump(obj, file)

def load_onehot(path):
    file = open(path, mode='rb')
    return pickle.load(file)

def save_word2vec(obj, path):
    file = open(path, mode='wb')
    pickle.dump(obj, file)

def softmax(x):
    max_x = np.max(x)
    return np.exp(x - max_x) / np.sum(np.exp(x - max_x))

def cosine(x1, x2):
    return np.sum(np.multiply(x1, x2)) / (np.linalg.norm(x1) * np.linalg.norm(x2))
