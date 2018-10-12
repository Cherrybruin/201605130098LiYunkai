import json

IDF = {}
TF = {}

# 对于iDF做处理，去掉多余3k和次数为1的。
# with open('IDF.json','r') as fp:
#     IDF = json.load(fp)
#     t = list(IDF.keys())
#     for i in t:
#         if(IDF[i] == 1):
#             IDF.pop(i)
#         elif i.strip() == '':
#             IDF.pop(i)
#         elif IDF[i] > 3000:
#             IDF.pop(i)
#     # print(len(IDF))
#     # print(IDF)

# with open('IDF.json', 'w') as fp:
#     json.dump(IDF,fp)

# with open('IDF.json','r') as fp:
#     IDF = json.load(fp):

# with open('TF.json','r') as fp:
#     TF = json.load(fp)

result = {}
with open(r'hw2/correct_test_data2.json','r') as fp:
    with open(r'hw2/answer.json','r') as fp2:
        i1 = fp.readlines()
        i2 = fp2.readlines()
        tot = 0
        correct = 0
        for i in range(len(i1)):
            if i1[i] == i2[i]:
                correct += 1
            tot+=1
        print(correct/tot)