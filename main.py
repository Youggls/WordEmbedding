from onehot import onehot
from util import save_onehot
from util import load_onehot, save_word2vec
from word2vec import word2vec

if __name__ == '__main__':
    data = open('./data/part.txt', mode='r', encoding='utf8')
    # sentences = []
    # for line in data.readlines():
    #     line = line.strip('\n')
    #     sentences.append(line.split(' '))
    # voca = onehot(sentences)
    # w = word2vec(100, 1, 3)
    # w.train(sentences)
    w = load_onehot('data/word2vec.model')
    print(w.calc_similarity('实木床', '质量'))

