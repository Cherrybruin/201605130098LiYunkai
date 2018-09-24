import re
from os import listdir, path
from standerd_scikit import rtos
dir_name = '20news'
# print(listdir(dic_name))
# print(re.findall("\w+",))


# for all the files in resource
# for i in listdir(dir_name):
#     sub_dir_name = dir_name + '/' + i
#     print(listdir(sub_dir_name))


def raw_token(raw_set:iter):
    '''
        param:
        :: raw_set :file path of a text file
        returntype: dictionary
            return the set of all the words of the text
    '''
    wordbag = {}
    word = re.compile(r'[a-zA-Z]+')
    word_word = re.compile(r'[a-zA-Z]+-[a-zA-Z]+')
    num = re.compile(r'\d+')
    nullsplit = re.compile(r'\s+')
    sub_1 = ['s']
    sub_2 = ['er','or','ly','ed','es',]
    sub_3 = ['ing','est']
    sub_4 = ['ment']
    for temp in raw_set:
        # sub lastfix
        if not temp:
            continue 
        temp = str(temp).strip()
        for i in word.findall(temp):
            i = i.strip()
            if i in wordbag.keys():
                wordbag[i] = wordbag[i]+1
            else:
                wordbag.update({
                    i : 0,
                })
        for i in word_word.findall(temp):
            i = i.strip()
            if i in wordbag.keys():
                wordbag[i] = wordbag[i]+1
            else:
                wordbag.update({
                    i : 0,
                })
        for i in num.findall(temp):
            i = i.strip()
            if i in wordbag.keys():
                wordbag[i] = wordbag[i]+1
            else:
                wordbag.update({
                    i : 0,
                })
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
    return wordbag


def reduce_stoping_word(wordlist:iter):
    with open('stopword','r',encoding='utf-8') as fp:
        for i in fp:
            t = i.strip()
            if t in wordlist:
                wordlist.remove(t)
            else :
                pass
    return wordlist



rrr = set()
# a_sub_dir = listdir(dir_name)
# a_file = listdir(path.join(dir_name,a_sub_dir))
# a_file = path.join(dir_name, a_sub_dir, a_file)

# print(raw_token(rtos()))
my_wb = raw_token(rtos())
for a,b in my_wb.keys():
    my_wb.pop(a)
    try:
        if a[-1] == 's':
            a=a[:-1]
        if len(a)<6:
            
        if a[-2:] in sub_2:
            a=a[:-2]
        if a[-3:] in sub_3:
            a=a[:-3]
        if a[-4:] in sub_4:
            a=[:-4]
    except Exception:
        pass
    if a in 
# print(len(rrr))
# for i in sorted(list(reduce_stoping_word(raw_token_set(a_file)))):
#     print(i)


# print(raw_token_list(a_file))