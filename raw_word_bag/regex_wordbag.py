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
with open(a_file, 'rb') as fp:
    print(fp.read())