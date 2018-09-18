import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from os import listdir, path
from regex_wordbag import reduce_stoping_word
a_tokenization = CountVectorizer()


# find a file in dirs

dir_name = '20news'
a_sub_dir = listdir(dir_name)[0]
a_file = listdir(path.join(dir_name,a_sub_dir))[0]
a_file = path.join(dir_name, a_sub_dir, a_file)

def rtos(fp):
    for i in fp:
        yield str(i)

with open(a_file,'rb') as fp:
    print(a_tokenization.fit(rtos(fp)))

result = list(a_tokenization.vocabulary_.keys())
result = reduce_stoping_word(result)
for i in sorted(result):
    print(i)

