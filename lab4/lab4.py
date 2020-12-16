from  decorator_time import time_work_func
import time
import plotly.express as px
import pandas

def is_word_in_str(str, word):
    len_word=len(word)
    for i in range(len(str)-len_word):
        if str[i:len_word+i]==word:
            return True
    return False

def sort_words_in_str(str):
    words=str.split()
    new_words=sorted(words)
    return new_words
def find_words(str):
    sepator=[' ',',','.','!',':','?']
    start_word=0
    words=[]
    i=0
    while i<len(str):
        if(str[i] in sepator):
           words.append(str[start_word:i])
           if(str[i]==' '):
               start_word=i+1
           else:
               start_word=i+2
               i+=1
        i+=1
    new_words=sorted(words)
    return new_words
def print_words(words):
    for word in words:
        print(word)

# count=4000
str="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# chart_data=[]
# for _ in range(10):
#     words = find_words(str * count)
#     start_time = time.time()
#     res=find_words(words)
#     res_time=time.time() - start_time
#     chart_data.append(dict(size=count, time=res_time))
#     count+=250
#
# fig = px.line(chart_data, x="size", y="time")
# fig.show()
# print(str[0:5])

print(is_word_in_str(str,"sed"))
print(sort_words_in_str(str))
# count=4000
# chart_data=[]
# for _ in range(10):
#     start_time = time.time()
#     print(is_word_in_str(str,"sed"))
#     print(sort_words_in_str(str))
#     res_time = time.time() - start_time
#     chart_data.append(dict(size=count, time=res_time))
#     count+=250

#print_words(words)

