import re
from os import listdir,path

dir_name = '20news'
# print(listdir(dic_name))
# print(re.findall("\w+",))


# for all the files in resource
# for i in listdir(dir_name):
#     sub_dir_name = dir_name + '/' + i
#     print(listdir(sub_dir_name))

a_sub_dir = listdir(dir_name)[0]
a_file = listdir(path.join(dir_name,a_sub_dir))[0]
a_file = path.join(dir_name, a_sub_dir, a_file)
def raw_token_set(filename:str):
    '''
        param:
        :: filename: a file path of a text file
        :: returntype: set
            return the set of all the words of the text
    '''
    wordbag = set()
    word = re.compile(r'[a-zA-Z]+')
    word_word = re.compile(r'[a-zA-Z]+-[a-zA-Z]+')
    num = re.compile(r'\d+')
    nullsplit = re.compile(r'\s+')
    with open(filename, 'rb') as fp:
        for line in fp.readlines():
            temp = str(line).strip().lower()
            if not temp:
                continue
            # print(temp)
            # for i in re.split(nullsplit, temp):
            #     i = i.strip()
            #     wordbag.add(i)
            #     for j in word.findall(i):
            #         wordbag.add(j.strip())
            #     for j in num.findall(i):
            #         wordbag.add(j.strip())
            #     for j in word_word.findall(i):
            #         wordbag.add(j.strip())
            for i in word.findall(temp):
                wordbag.add(i.strip())
            for i in word_word.findall(temp):
                wordbag.add(i.strip())
            for i in num.findall(temp):
                wordbag.add(i.strip())
    return wordbag

def normalization(wordlist:set):
    t_list = list(wordlist)
    sub_tion = re.compile(r'tion\b')
    sub_space = re.compile(r'er\b|or\b|s\b|ing\b|ed\b|es\b|ment\b|ly\b')
    result = set()
    for i in t_list:
        t = sub_space.sub(i)
        result.add(t)
    return result

def reduce_stoping_word(wordlist:iter):
    with open('stopword','r',encoding='utf-8') as fp:
        for i in fp:
            t = i.strip()
            if t in wordlist:
                wordlist.remove(t)
            else :
                pass
    return wordlist
for i in sorted(list(reduce_stoping_word(raw_token_set(a_file)))):
    print(i)


# print(raw_token_list(a_file))