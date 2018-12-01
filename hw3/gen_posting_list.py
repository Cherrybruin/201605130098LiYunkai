import re
import json
import sys
class PostingListTerm():
    # 这是一条 termId->docId
    # 包含了新增(append)，取并(union)，取交(retain)
    def __init__(self, *kwags):
        self.doclist = []
        for i in kwags:
            self.doclist.append(i)
    def append(self, *kwags):
        for i in kwags:
            self.doclist.append(i)
        self.doclist.sort()
    def __str__(self,):
        return f'PostingListTerm{self.doclist}'
    def union(self, another):
        i, j = 0, 0 
        len_i, len_j = len(self.doclist), len(another.doclist)
        result = PostingListTerm()
        while i < len_i and j < len_j :
            if self.doclist[i] == another.doclist[j]:
                result.append(self.doclist[i])
                i, j = i+1, j+1
            elif self.doclist[i] > another.doclist[j]:
                result.append(another.doclist[j])
                j += 1
            else:
                result.append(another.doclist[i])
                i += 1
        while i < len_i:
            result.append(another.doclist[i])
            i += 1
        while j < len_j:
            result.append(another.doclist[j])
            j+=1
        return result
    def retain(self,another):
        i, j = 0, 0 
        len_i, len_j = len(self.doclist), len(another.doclist)
        result = PostingListTerm()
        while i < len_i and j < len_j :
            if self.doclist[i] == another.doclist[j]:
                result.append(self.doclist[i])
                i, j = i+1, j+1
            elif self.doclist[i] > another.doclist[j]:
                j += 1
            else:
                i += 1
        return result
    def items(self):
        for i in self.doclist:
            yield i
    
class PostingList():
    # 这是整个的termId->docId的映射表
    # 包含了新增（update），按termId索引
    def __init__(self,*kwags):
        self._postinglist = {}
    def update(self, key, value):
        try:
            self._postinglist[key].append(value)
        except Exception:
            self._postinglist.update({
                key:PostingListTerm(value),
            })
    def items(self):
        for a,b in self._postinglist.items():
            yield (a,b)
    def keys(self):
        for i in self._postinglist.keys():
            yield i
    def __str__(self):
        return f'PostingList:{self._postinglist}'
    def __getitem__(self, str):
        return self._postinglist[str]

postinglist = PostingList()
tweets = {}
'''
    tweets {
        tweetId(int) :{
            username:
            clusterNo:
            text:
            timeStr:
            tweetId:
            errorCode: 200(string)
            textCleaned:
            relevance:
        }
    }
'''
word_re = re.compile(r'\w+')
num_re = re.compile(r'\d+')

# 每次引入的时候只要从文件读取即可
# posting_list.txt 是termID->docId
# tweets 是 docId -> tweet 
with open('../hw3/postinglist.txt','r',encoding ='utf-8') as fp:
    for i in fp:
        # print(i,'\n')
        i = i.split(':')
        term, b = i[0], i[1]
        term = term.strip()
        for i in num_re.findall(b):
            postinglist.update(term,int(str(i)))
with open("../hw3/tweets.txt",'r') as fp:
    try:
        for i in fp:
            tweet = json.loads(i)
            tweets.update({
                int(tweet['tweetId']):tweet,
            })
    except Exception:
        print("load tweets.txt failed")
if __name__ == "__main__":
    # 这个是生成posting_list.txt 
    # 一般如果正确这个文件之北执行一次
    with open("tweets.txt",'r') as fp:
        try:
            for i in fp:
                tweet = json.loads(i)
                # print(tweet['text'])
                for i in word_re.findall(tweet['text']):
                    t = str(i).lower()
                    postinglist.update(t,tweet['tweetId'])
        except Exception:
            print("json load failed")
# print(list(postinglist.keys()))
    with open('postinglist.txt','w',encoding="utf-8") as fp:
        for a,b in postinglist.items():
            fp.write(f'{a}:{b}\n')
