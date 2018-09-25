import re
from os import listdir, path
from standerd_scikit import rtos
dir_name = '20news'
# print(listdir(dic_name))
# print(re.findall("\w+",))

sub_1 = ['s', 'e']
sub_2 = ['er','or','ly','ed','es', 'al', 'ss', 'ty', 'en']
sub_3 = ['ing','est', 'ful']
sub_4 = ['ment', 'tion', 'sion', 'ship', 'able']
#  rots :: function that yield return the strings of files

# for all the files in resource
# for i in listdir(dir_name):
#     sub_dir_name = dir_name + '/' + i
#     print(listdir(sub_dir_name))


def raw_token(raw_set:iter):
    '''
        param:
        :: raw_set :file path of a text file
        returntype: dictionary
            return the dict of all the words of the texts ans counts
    '''
    wordbag = {}
    word = re.compile(r'[a-zA-Z]+')
    word_word = re.compile(r'[a-zA-Z]+-[a-zA-Z]+')
    num = re.compile(r'\d+')
    nullsplit = re.compile(r'\s+')
    
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
                    i : 1,
                })
        for i in word_word.findall(temp):
            i = i.strip()
            if i in wordbag.keys():
                wordbag[i] = wordbag[i]+1
            else:
                wordbag.update({
                    i : 1,
                })
        for i in num.findall(temp):
            i = i.strip()
            if i in wordbag.keys():
                wordbag[i] = wordbag[i]+1
            else:
                wordbag.update({
                    i : 1,
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
    '''
    parm :    
        wordlist: iter
            the word list
    returntype:
        the wordlist without the stopping word in stopword(file)

    '''
    with open('stopword','r',encoding='utf-8') as fp:
        for i in fp:
            t = i.strip()
            if t in wordlist:
                wordlist.pop(t)
            else :
                pass
    return wordlist



rrr = set()
# a_sub_dir = listdir(dir_name)
# a_file = listdir(path.join(dir_name,a_sub_dir))
# a_file = path.join(dir_name, a_sub_dir, a_file)

# print(raw_token(rtos()))
my_wb = raw_token(rtos())

def str_traform(a:str):
    if a[-1] in sub_1:
        a=a[:-1]
    if len(a) <= 3:
        return a
    if a[-2:] in sub_2:
        a=a[:-2]
    if len(a) <=3:
        return a
    if a[-3:] in sub_3:
        a=a[:-3]
    if len(a) <=3:
        return a
    if a[-4:] in sub_4:
        a=a[:-4]
    return a


result_dictionary = dict()

for a,b in my_wb.items():
    try:
        a = str_traform(a)
    except Exception:
        pass
    if a in result_dictionary.keys():
        result_dictionary[a] += b
    else:
        result_dictionary.update({
            a: b,
        })
# print(len(rrr))
# for i in sorted(list(reduce_stoping_word(raw_token_set(a_file)))):
#     print(i)

result_dictionary = reduce_stoping_word(result_dictionary)
my_wb = result_dictionary
result_dictionary = dict()
for a,b in my_wb.items():
    if b <= 2:
        continue
    else:
        result_dictionary.update({
            a: b,
        })
# print(my_wb)
print(len(result_dictionary))
print(result_dictionary)
# print(raw_token_list(a_file))