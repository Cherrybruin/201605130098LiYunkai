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
    word = re.compile(r'[a-zA-Z]+-?[a-zA-Z]+')
    num = re.compile(r'\d+')
    with open(filename, 'rb') as fp:
        for line in fp:
            temp = str(line).strip().lower()
            if not temp:
                continue
            # print(temp)
            for i in re.findall(word, temp):
                wordbag.add(i.strip())
            for i in re.findall(num, temp):
                wordbag.add(i.strip())
    return wordbag

def raw_token_list(filename:str):
    '''
        param:
        :: filename: a file path of a text file
        :: returntype: list
            return the list of all the words of the text
    '''
    wordbag = list()
    word = re.compile(r'[a-zA-Z]+-?[a-zA-Z]+')
    num = re.compile(r'\d+')
    with open(filename, 'rb') as fp:
        for line in fp:
            temp = str(line).strip().lower()
            if not temp:
                continue
            # print(temp)
            for i in re.findall(word, temp):
                wordbag.append(i.strip())
            for i in re.findall(num, temp):
                wordbag.append(i.strip())
    return wordbag

print(raw_token_list(a_file))