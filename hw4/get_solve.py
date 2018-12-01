# coding=utf-8
# import spacy
import re, json
from math import log
# nlp = spacy.load('en',disable=["tagger", "parser", "ner"])
re_word = re.compile(r"\w+")
import json
tweets = {}
posting_list = {}

def re_get_word_count(text:str):
    '''
        params:
            text: str
            文本
        return type:
            yield tuple(word,word_count)
    '''
    _temp_dict = {}
    for i in re_word.findall(text):
        try:
            # tweet_wb[i.lemma_] += 1
            _temp_dict[str(i)] += 1

        except Exception:
            # tweet_wb.update({i.lemma_:1})
            _temp_dict.update({str(i):1})
    _temp_list = []
    for a,b in _temp_dict.items():
        yield (a,b)

avdl = 0
with open("../hw3/tweets.txt",'r',encoding='utf-8') as fp:
    for i in fp:
        tweet = json.loads(i)
        tweetId = int(tweet['tweetId'])
        text = tweet['text'].lower()
        tweets.update({
            int(tweetId):text
        })
        avdl += len(text)
        # print(text)
        # af = nlp(text.lower())
        for i in re_get_word_count(text):
            try:
                posting_list[i[0]].append((tweetId,i[1]))
            except Exception:
                posting_list[i[0]] = []
                posting_list[i[0]].append((tweetId,i[1]))
    ''' 
        af = re_word.findall(text)
        tweet_wb = {}
        temp_posting_list = []
        for i in af:
            try:
                # tweet_wb[i.lemma_] += 1
                tweet_wb[str(i)] += 1

            except Exception:
                # tweet_wb.update({i.lemma_:1})
                tweet_wb.update({str(i):1})

        for a,b in tweet_wb.items():
            # temp_posting_list.append((a,b))
            try:
                posting_list[a].append((tweetId,b))
            except Exception:
                posting_list[a] = []
                posting_list[a].append((tweetId,b))
    # print(len(posting_list.keys()))
    '''

print(avdl / len(tweets))
tf = {}
df = {}
# compute tf
for a,b in posting_list.items():
    s = 0
    for j in b:
        s += j[1]
    tf.update({a:s})
    df.update({a:len(b)})
# print(tf)

with open("query171-225_cleaned.txt",'r',encoding='utf-8') as fp:
    querys = json.load(fp)

avdl = 8
for query_Id,query_text in querys.items():
    # print(type(a))
    query_Id = int(query_Id)
    # print(a)
    envalue = {i:0 for i in tweets.keys()}
    for query_word,query_word_count in re_get_word_count(query_text):
        # print(a)
        def VSM_F(c_w_q,c_w_d,tweet_l,df_w,b=0.5,avdl=108,M=len(tweets)):
            return c_w_q*(log(1+log(1+c_w_d))/(1-b+b*(tweet_l/avdl)))*(log((M+1)/df_w))
        def BM25(c_w_q,c_w_d,tweet_l,df_w,k=8,b=0.5,avdl=108,M=len(tweets)):
            return c_w_q*((k+1)*c_w_d/(c_w_d+k*(1-b+b*(tweet_l/avdl))))*(log((M+1)/df_w))
        
        if query_word in posting_list.keys():
            # if found: only deal with word which is found
            _temp_word_posting_list = posting_list[query_word]
            for tweetId,tweet_word_count in _temp_word_posting_list:
                envalue[tweetId] += VSM_F(query_word_count,tweet_word_count,len(tweets[tweetId]),df[query_word])
                # envalue[tweetId] += BM25(query_word_count,tweet_word_count,len(tweets[tweetId]),df[query_word])
        else:
            # if not found: deal with all word which contain query_word
            for tweet_word,doc_id_list in posting_list.items():
                if query_word in tweet_word:
                    for tweetId,tweet_word_count in doc_id_list:
                        envalue[tweetId] += VSM_F(query_word_count,tweet_word_count,len(tweets[tweetId]),df[query_word])
                        # envalue[tweetId] += BM25(query_word_count,tweet_word_count,len(tweets[tweetId]),df[query_word])
    sorted_envalue = []
    for i,j in envalue.items():
        sorted_envalue.append((i,j))
    sorted_envalue.sort(key=lambda x:x[1],reverse=True)
    with open('VSM_result.txt','a+',encoding='utf-8') as fp3:
        for i in sorted_envalue:
            fp3.write(f'{query_Id} {i[0]}\n')