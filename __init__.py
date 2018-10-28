#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 上午 11:27
# @Author  : Aaron Chou
# @Site    : https://github.com/InsaneLife

import numpy as np

out_path = "./vocab/google_in_vocab_embedding.npy"
ss = np.load(out_path)
new = []
for each in ss:
    new.append(np.array(each))
new = np.array(new)
out_path = "./vocab/google_in_vocab_embedding1.npy"
ss1 = np.load(out_path)
# np.save(out_path, new)
pass