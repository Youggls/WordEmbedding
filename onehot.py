import numpy as np
import pickle
class onehot:
    def __init__(self, sentences):
        self.__sentences = sentences
        self.__data = {}
        self.__count = {}
        self.__build()

    def __build(self):
        self.__word_num = 1
        for sentence in self.__sentences:
            for word in sentence:
                if word in self.__data:
                    self.__count[word] += 1
                else:
                    self.__count[word] = 1
                    self.__data[word] = self.__word_num
                    self.__word_num += 1

    def __getitem__(self, word):
        if word not in self.__data:
            print('Error! The word not in it\'s map!')
        else:
            ret = np.zeros((self.__word_num - 1, 1))
            ret[self.__data[word] - 1] = 1
            return ret

    def get_voca_size(self):
        return self.__word_num - 1

    def get_word_frequency(self, word):
        if word not in self.__data:
            print('Error! The word not in it\'s map!')
        else:
            return self.__count[word]

    def get_index_of_word(self, word):
        if word not in self.__data:
            print('Error! The word not in it\'s map!')
        else:
            return self.__data[word] - 1
