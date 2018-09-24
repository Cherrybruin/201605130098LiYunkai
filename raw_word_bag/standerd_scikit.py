import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from os import listdir, path
a_tokenization = CountVectorizer()


# find a file in dirs

dir_name = '20news'
a_sub_dir = listdir(dir_name)[0]
a_file = listdir(path.join(dir_name,a_sub_dir))[0]
a_file = path.join(dir_name, a_sub_dir, a_file)


def rtos():
    for i_subdir in listdir(dir_name):
        for j_file in listdir(path.join(dir_name, i_subdir)):
            file_path = path.join(dir_name, i_subdir, j_file)
            with open(file_path,'rb') as fp:
                for i in fp:
                    try:
                        yield str(i,'gbk','ignore').lower()
                    except Exception:
                        print('error occured: ',i,'ignore')


def reduce_stoping_word(wordlist:iter):
    with open('stopword','r',encoding='utf-8') as fp:
        for i in fp:
            t = i.strip()
            if t in wordlist:
                wordlist.remove(t)
            else :
                pass
    return wordlist


if __name__ == '__main__':
    a_tokenization.fit(rtos())

    result = list(a_tokenization.vocabulary_.keys())
    result = reduce_stoping_word(result)
    print(len(result))

