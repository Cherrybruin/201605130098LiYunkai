import spacy
from os import path, listdir
from spacy.lang.en import English
import threading
from time import sleep
nlp = spacy.load('en')
# tokenizer = English().Defaults.create_tokenizer(nlp)

resource_path = r'../20news'

IDF = {}
TF = {}



def _add(string, fir_path):
    global IDF
    global TF
    if string not in TF[dir_path].keys():
        TF[dir_path].update({
            string: 1
        })
    else:
        TF[dir_path][string] = TF[dir_path][string]+1
    if string in IDF.keys():
        IDF[string] += 1
    else:
        IDF.update({
            string:1
        })

class MyTokenization(threading.Thread):
    def __init__(self, MyFilepath):
        super().__init__()
        self.file = MyFilepath

    def run(self):
        nlp = spacy.load('en')
        with open(file_path, 'rb') as fp:
            for string in fp:
                string = str(string, 'utf-8', 'ignore')
                # print(string)
                # if len(all_string + string) > 1000000:
                #     _fit(all_string, dir_path)
                #     all_string = ''
                # all_string = all_string + string
                for d in nlp(string):
                    _add(d.lemma_, self.file)

def _fit(string, dir_path, ):
    global IDF
    global TF
    doc = nlp(all_string)
    for token in doc:
        # print(token.text)
        _add(token.lower, dir_path)


for dir_path in listdir(resource_path):
    # print(dir_path)
    TF.update({
                dir_path:{}
            })
    all_string = ''
    for file_path in listdir(path.join(resource_path,dir_path)):
        file_path = path.join(resource_path,dir_path,file_path)
        print('\t\t',file_path)
        
        # MyTokenization(file_path).start()
        with open(file_path,'rb') as fp:
            for line in fp:
                line = str(line,'utf-8','ignore')
                if len(all_string + line) > 1000000:
                    for doc in nlp.pipe(all_string):
                        if doc != ' ':
                            print(doc, end='')
                        elif doc == ' ':
                            print(doc)
                    all_string = ''
                all_string += line
    for doc in nlp.pipe(all_string,n_threads=10):
        if doc:
            print(doc, end='')
        elif doc == ' ':
            print('')
    all_string = ''
sleep(10)
print(IDF)