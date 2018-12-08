use slot-gated model for joint Slot Filling and Intent Prediction. and add CRF layer.
# slot-gete论文解读

https://blog.csdn.net/shine19930820/article/details/83052300

# CRF
crf开关：--use_crf

# 预训练

预训练词向量加入之后，效果反而变差了，Semantic Acc: 27.40左右。具体原因不明，有了解过的请告知，感谢。

后期加入bert实验。

# 实验结果

| ATIS数据集   | crf                      | softmax                 |
| ------------ | ------------------------ | ----------------------- |
| Slot f1      | val: 97.39 ; test: 95.15 | val: 97.0; test:95.08   |
| Intent Acc   | val: 98.2; test: 95.41   | val: 97.6; test: 95.52  |
| Semantic Acc | val: 90.0; test: 83.42   | val: 89.0 ; test: 83.53 |



## Environment

tensorflow 1.11
python 3.5

the origin code : https://github.com/MiuLab/SlotGated-SLU
## Reference
1. Slot-Gated Modeling for Joint Slot Filling and Intent Prediction : http://www.aclweb.org/anthology/N18-2118

