import json

from os import listdir,path

import spacy
import sys
from math import log
class Classification():
    def __init__(self, input_dict:dict):
        self._language = spacy.load('en', disable=['parser','tagger','ner'])
        self.input = input_dict
        self.p_perclass = {}
        self.inverted_input = {}

        for a,b in input_dict.items():
            if b in self.inverted_input.keys():
                self.inverted_input[b].append(a)
            else:
                self.inverted_input.update({
                    b:[a,]
                })
        
        self._raw_tf = {}
        self._raw_idf = {}
        self.wordlist = {}
        self.num_of_term = {}
        self.sum_of_term = {}
        solved = 0
        tot = len(input_dict)
        for a,b in self.inverted_input.items():
            self._raw_tf[a] = {}
            self.num_of_term[a] = 0
            self.sum_of_term[a] = 0
            self.p_perclass[a] = len(b)/len(input_dict)
            all_string_list = []
            for afile in b:
                solved += 1
                sys.stdout.write('\r'+str(solved)+r'/'+str(tot))
                with open(afile,'rb') as fp:
                    all_string_list.extend([str(i,'utf-8','ignore').lower() for i in fp.readlines()])
                if len(all_string_list)>10000:
                    # print(all_string_list)
                    for doc in self._language.pipe(all_string_list):
                        for i in doc:
                            self._add_to_idf(i.lemma_)
                            self._add_to_tf(i.lemma_,a)
                    all_string_list = []
            if all_string_list:
                for doc in self._language.pipe(all_string_list):
                    for i in doc:
                        self._add_to_idf(i.lemma_)
                        self._add_to_tf(i.lemma_,a)
                all_string_list = []
        self._gen_wordlist()
        sys.stdout.flush()
        print('classification already build')
        
        
    def gen_file(self,filepath:str):
        temp_tf = {}
        num_of_term = 0
        with open(filepath,'rb') as fp:
            for doc in self._language.pipe([str(i,'utf-8','ignore').lower() for i in fp.readlines()]):
                for i in doc:
                    if i.lemma_ in temp_tf:
                        temp_tf[i.lemma_] += 1
                    else:
                        temp_tf[i.lemma_] = 1
                    num_of_term += 1
        return (num_of_term,temp_tf)
        
                    
    def _add_to_idf(self,string):
        if string in self._raw_idf.keys():
            self._raw_idf[string] += 1
        else:
            self._raw_idf.update({
                string:1
            })
    def _add_to_tf(self,string,classname):
        if string in self._raw_tf[classname].keys():
            self._raw_tf[classname][string] += 1
        else:
            self._raw_tf[classname][string] = 1
            self.num_of_term[classname] += 1
        self.sum_of_term[classname] += 1

    def _gen_wordlist(self):
        max_filelist = 0
        for a,b in self.inverted_input.items():
            if len(b) > max_filelist:
                max_filelist = len(b)
        for a,b in self._raw_idf.items():
            if b<= 1:
                continue
            elif b>max_filelist*3:
                continue
            else:
                self.wordlist[a]=True


    def train(self):
        self._gen_wordlist()
        self.p = {}
        for a,b in self._raw_tf.items():
            num_of_term = 0
            _temp_p = {}
            for c,d in b.items():
                num_of_term += b
            for c,d in b.items():
                _temp_p[c] = d/num_of_term
            self.p[a] = (num_of_term,_temp_p)
    
    def test(self,filelist:list):
        solved = 0
        num_of_wordlist = len(self.wordlist)
        result = {}
        tot = len(filelist)
        
        for afile in filelist:
            solved += 1
            sys.stdout.write('\r'+str(solved)+r'/'+str(tot))
            num, tf = self.gen_file(afile)
            result[afile] = None
            
            for a,b in self._raw_tf.items():
                # 先选类
                temp_p = 0
                
                for word,occur in tf.items():
                    # 这是去重版本
                    # try:
                    #     if self.wordlist[word] == True:
                    #         # if word in b.keys():
                    #         #     temp_p += log((b[word]+1)/(self.num_of_term[a]+self.sum_of_term[a]))
                    #         # else:
                    #         #     temp_p += log(1/(self.num_of_term[a]+self.sum_of_term[a]))
                    #         try:
                    #             temp_p += log((b[word]+1)/(self.num_of_term[a]+self.sum_of_term[a]))
                    #         except Exception:
                    #             temp_p += log(1/(self.num_of_term[a]+self.sum_of_term[a]))
                    # except Exception:
                    #     pass
                    try:
                        if self.wordlist[word] == True:
                            # if word in b.keys():
                            #     temp_p += log((b[word]+1)/(self.num_of_term[a]+self.sum_of_term[a]))
                            # else:
                            #     temp_p += log(1/(self.num_of_term[a]+self.sum_of_term[a]))
                            try:
                                temp_p += occur*log((b[word]+1)/(self.num_of_term[a]+self.sum_of_term[a]))
                            except Exception:
                                temp_p += occur*log(1/(self.num_of_term[a]+self.sum_of_term[a]))
                    except Exception:
                        pass
                temp_p += log(self.p_perclass[a])
                if result[afile]:
                    if temp_p > result[afile][1]:
                        result[afile] = (a,temp_p)
                else:
                    result[afile] = (a,temp_p)
        sys.stdout.flush()
        
        return result

if __name__ == '__main__':
    train_file = r'hw2/train_data.json'
    train_data = {}
    with open(train_file,'r') as fp:
        train_data = json.load(fp)
    nlp = Classification(train_data)
    # print(nlp._raw_tf)
    test_file = r'hw2/test_data.json'
    test_data = []
    with open(test_file,'r') as fp:
        test_data = json.load(fp)
    with open(r'hw2/answer.json','w') as fp:
        result = nlp.test(test_data)
        for i in result.keys():
            result[i] = result[i][0]
            fp.write(i+':'+result[i]+'\n')