# coding = utf-8
from gen_posting_list import postinglist, word_re, PostingListTerm,tweets

def query(search_string:str):
    this_step = '' # 这一层所有操作相同
    # 处理空串
    search_string = search_string.strip()
    if not search_string:
        return None

    # 处理括号
    stack = []
    kuohao = []
    for i in range(len(search_string)):
        if search_string[i] == '(':
            stack.append(i)
        elif search_string[i] == ')':
            if len(stack) == 1:
                kuohao.append((stack[0],i))
            stack.pop()

    # 找到这一层的操作
    if kuohao:
        if 'OR' in search_string[:kuohao[0][0]]:
            this_step = 'OR'
        elif 'AND' in search_string[:kuohao[0][0]]:
            this_step = 'AND'
        elif 'AND' in search_string[kuohao[-1][1]+1:]:
            this_step = 'AND'
        elif 'OR' in search_string[kuohao[-1][1]+1:]:
            this_step = 'OR'
        j = 0
        while not this_step and j<len(kuohao)-1:
            if 'OR' in search_string[kuohao[j][1]+1:kuohao[j+1][0]]:
                this_step = 'OR'
            elif 'AND' in search_string[kuohao[j][1]+1:kuohao[j+1][0]]:
                this_step = 'AND'
        # 开始计算
        if not this_step and len(kuohao):
            return query(search_string[1:-1])
        elif not this_step and not len(kuohao):
            try:
                return postinglist[search_string]
            except Exception:
                return PostingListTerm()
        if this_step == 'OR':
            result = PostingListTerm()
            i, j = 0, 0
            for a,b in kuohao:
                result.union(query(search_string[a+1:b]))
            for a,b in kuohao.reverse():
                search_string = search_string[:a]+search_string[b+1:]
            result_list = search_string.split(this_step)
            for i in result_list:
                i = i.strip()
                result.union(query(i))
            return result
        if this_step == 'AND':
            result = PostingListTerm()
            i, j = 0, 0
            for a,b in kuohao:
                result.retain(query(search_string[a+1:b]))
            for a,b in kuohao.reverse():
                search_string = search_string[:a]+search_string[b+1:]
            result_list = search_string.split(this_step)
            for i in result_list:
                i = i.strip()
                if i:
                    result.retain(query(i))
            return result
    else:
        if 'OR' in search_string:
            this_step = 'OR'
        elif 'AND' in search_string:
            this_step = 'AND'

        if not this_step:
            try:
                return postinglist[search_string.strip()]
            except Exception:
                return None
        elif this_step == 'OR':
            
            result = PostingListTerm()
            for i in search_string.split(this_step):
                try:
                    result = result.union(postinglist[i.strip()])
                except Exception:
                    pass
            return result
        elif this_step == 'AND':
            result_list = search_string.split(this_step)
            result = postinglist[result_list[0].strip()]
            # print(len(result.doclist))

            for i in result_list[1:]:
                if i.strip():
                    try:
                        result = result.retain(postinglist[i.strip()])
                        # print(len(postinglist[i.strip()].doclist))
                        # print(len(result.doclist))
                    except Exception :
                        return PostingListTerm()
            return result

if __name__ == "__main__":
    # print(tweets)
    # print(postinglist)
    t= input()
    t = t.strip()
    for i in query(t).items():
        print(tweets[i]['tweetId'],":  ",tweets[i]['text'])
        # pass