#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 下午 08:55
# @Author  : Aaron Chou 
# @Site    : https://github.com/InsaneLife

import gensim
import numpy as np

data_root = 'E:\project_data\word_vector/'
model_path = data_root + 'GoogleNews-vectors-negative300.bin.gz'
# 导入模型
model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
# model.save_word2vec_format(data_root + 'GoogleNews-vectors-negative300.txt', binary=False)
google_embedding_path = data_root + 'GoogleNews-vectors-negative300.txt'

print(model['to'])

def get_embedding_map(path):
    map = {}
    with open(path, 'r',encoding="utf-8") as f:
        for each in f.readlines():
            each = each.strip().split()
            map[each[0]] = [float(x) for x in each[1:]]
    return map

def write_vector2file(embedding_map, vocab_path, out_path, dim):
    with open(vocab_path) as vocabs:
        vocabs = vocabs.readlines()
        embedding = np.zeros([len(vocabs), dim])
        for i, v in enumerate(vocabs):
            v = v.strip()
            try:
                embedding[i] = np.array(embedding_map[v])
            except:
                continue
        np.save(out_path, embedding)


def write_model_vector2file(model, vocab_path, out_path, dim):
    with open(vocab_path) as vocabs:
        vocabs = vocabs.readlines()
        embedding = np.zeros([len(vocabs), dim])
        for i, v in enumerate(vocabs):
            v = v.strip()
            try:
                embedding[i] = np.array(model[v])
            except:
                print("do not have: {}".format(v))
                continue
        np.save(out_path, embedding)

vocab_path = "./vocab/in_vocab"
out_path = "./vocab/google_in_vocab_embedding.npy"
dim = 300
# embedding_map = get_embedding_map(google_embedding_path)
# write_vector2file(embedding_map, vocab_path, out_path, dim)
write_model_vector2file(model, vocab_path, out_path, dim)
