from os import path,listdir

import json

from random import randint

# 测试随机数
# for i in range(10):
#     print(randint(0,1))

gen_train_data = {}
gen_test_data = []
gen_correct_test_data ={}
resource_path = '20news'

for dir_path in listdir(resource_path):
    for file_path in listdir(path.join(resource_path,dir_path)):
        # 随机生成训练数据，rest为测试数据
        if randint(0,1) == 0:
            gen_correct_test_data[path.join(resource_path,dir_path,file_path)] = dir_path
        else:
            gen_train_data[path.join(resource_path,dir_path,file_path)] = dir_path
        
        # 全部作为训练数据 & 测试数据
        # gen_correct_test_data[path.join(resource_path,dir_path,file_path)] = dir_path
        # gen_train_data[path.join(resource_path,dir_path,file_path)] = dir_path


print(len(gen_train_data))

with open(r'hw2/train_data.json','w') as fp:
    json.dump(gen_train_data,fp)
with open(r'hw2/test_data.json','w') as fp:
    json.dump(list(gen_correct_test_data.keys()),fp)
with open(r'hw2/correct_test_data.json','w') as fp:
    json.dump(gen_correct_test_data,fp)
with open(r'hw2/correct_test_data2.json','w') as fp:
    for a,b in gen_correct_test_data.items():
        fp.write(a+':'+b+'\n')