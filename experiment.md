# slot-gate, 设置early stop
## 默认参数，atis数据集。full
2018-10-27 11:35:14,704 : INFO : Valid:
2018-10-27 11:35:15,144 : INFO : slot f1: 97.45985401459855
2018-10-27 11:35:15,144 : INFO : intent accuracy: 97.0
2018-10-27 11:35:15,144 : INFO : semantic error(intent, slots are all correct): 89.4
2018-10-27 11:35:15,144 : INFO : Test:
2018-10-27 11:35:15,756 : INFO : slot f1: 95.27323844667019
2018-10-27 11:35:15,757 : INFO : intent accuracy: 95.29675251959686
2018-10-27 11:35:15,757 : INFO : semantic error(intent, slots are all correct): 84.32250839865621
## 默认参数，atis数据集。intent only
2018-10-27 12:12:23,849 : INFO : Epochs: 16
2018-10-27 12:12:23,849 : INFO : Loss: 0.03368351147406169
2018-10-27 12:12:24,165 : INFO : Valid:
2018-10-27 12:12:24,590 : INFO : slot f1: 97.27672035139092
2018-10-27 12:12:24,591 : INFO : intent accuracy: 97.0
2018-10-27 12:12:24,591 : INFO : semantic error(intent, slots are all correct): 88.6
2018-10-27 12:12:24,591 : INFO : Test:
2018-10-27 12:12:25,213 : INFO : slot f1: 95.38569918985559
2018-10-27 12:12:25,213 : INFO : intent accuracy: 95.74468085106383
2018-10-27 12:12:25,213 : INFO : semantic error(intent, slots are all correct): 84.88241881298993

## 添加crf
2018-10-28 14:02:12,178 : INFO : Epochs: 47
2018-10-28 14:02:12,178 : INFO : Loss: 0.10693743729165622
2018-10-28 14:02:12,585 : INFO : Valid:
2018-10-28 14:02:13,626 : INFO : slot f1: 98.0392156862745
2018-10-28 14:02:13,626 : INFO : intent accuracy: 97.6
2018-10-28 14:02:13,626 : INFO : semantic Acc(intent, slots are all correct): 91.0
2018-10-28 14:02:13,626 : INFO : Test:
2018-10-28 14:02:15,089 : INFO : slot f1: 95.77813107224874
2018-10-28 14:02:15,089 : INFO : intent accuracy: 95.52071668533034
2018-10-28 14:02:15,089 : INFO : semantic Acc(intent, slots are all correct): 85.1063829787234
2018-10-28 14:02:15,090 : INFO : new best score: Semantic Acc91.0

# 添加learning rate decay
2018-10-28 14:21:08,549 : INFO : Step: 6160
2018-10-28 14:21:08,549 : INFO : Epochs: 22
2018-10-28 14:21:08,549 : INFO : Loss: 0.24271476002676146
2018-10-28 14:21:08,959 : INFO : Valid:
2018-10-28 14:21:09,965 : INFO : slot f1: 97.8623718887262
2018-10-28 14:21:09,966 : INFO : intent accuracy: 97.6
2018-10-28 14:21:09,966 : INFO : semantic Acc(intent, slots are all correct): 90.8
2018-10-28 14:21:09,966 : INFO : Test:
2018-10-28 14:21:11,384 : INFO : slot f1: 95.62146892655367
2018-10-28 14:21:11,384 : INFO : intent accuracy: 94.96080627099664
2018-10-28 14:21:11,384 : INFO : semantic Acc(intent, slots are all correct): 84.32250839865621
2018-10-28 14:21:11,385 : INFO : new best score: Semantic Acc90.8

# learning rate decay, batch size increase
2018-10-28 20:25:07,973 : INFO : Step: 2600
2018-10-28 20:25:07,973 : INFO : Epochs: 32
2018-10-28 20:25:07,973 : INFO : Loss: 0.3802013429813087
2018-10-28 20:25:08,404 : INFO : Valid:
2018-10-28 20:25:08,709 : INFO : slot f1: 97.71395076201641
2018-10-28 20:25:08,709 : INFO : intent accuracy: 97.2
2018-10-28 20:25:08,709 : INFO : semantic Acc(intent, slots are all correct): 90.0
2018-10-28 20:25:08,709 : INFO : Test:
2018-10-28 20:25:09,073 : INFO : slot f1: 95.28851244044469
2018-10-28 20:25:09,073 : INFO : intent accuracy: 95.40873460246361
2018-10-28 20:25:09,073 : INFO : semantic Acc(intent, slots are all correct): 84.09854423292273
2018-10-28 20:25:09,074 : INFO : new best score: Semantic Acc90.0

# add slot intention
2018-10-28 20:34:35,037 : INFO : Step: 3384
2018-10-28 20:34:35,037 : INFO : Epochs: 67
2018-10-28 20:34:35,037 : INFO : Loss: 0.3469974221661687
2018-10-28 20:34:35,388 : INFO : Valid:
2018-10-28 20:34:35,637 : INFO : slot f1: 97.39385065885797
2018-10-28 20:34:35,638 : INFO : intent accuracy: 97.2
2018-10-28 20:34:35,638 : INFO : semantic Acc(intent, slots are all correct): 89.2
2018-10-28 20:34:35,638 : INFO : Test:
2018-10-28 20:34:35,973 : INFO : slot f1: 95.46016604840136
2018-10-28 20:34:35,974 : INFO : intent accuracy: 96.30459126539753
2018-10-28 20:34:35,974 : INFO : semantic Acc(intent, slots are all correct): 85.55431131019037
2018-10-28 20:34:35,974 : INFO : new best score: Semantic Acc: 89.2
