from bs4 import BeautifulSoup
import json
with open('query171-225.txt', 'r', encoding='utf-8') as fp:
    # print (fp.readlines())
    t = BeautifulSoup(''.join(fp.readlines()),'html.parser')
    zz = {}

    for i in t.find_all('top'):

            # print(i.num.text[-4:-1], i.query.text)
        zz.update({int(i.num.text[-4:-1]):i.query.text.strip().lower()})
                
    with open('query171-225_cleaned.txt','w',encoding='utf-8') as fp2:
        json.dump(zz,fp2)