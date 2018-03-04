# coding=utf-8
__author__ = 'pythme'

# Python之禅和他朋友们知识星球的每日一题 https://t.xiaomiquan.com/IUFmuFu
# https://github.com/pythonzhichan/DailyQuestion/tree/master/linshizuowei


"""
在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，例如：有列表 numbers = [10, 29, 30, 41]，要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)
######
for index ,value in enumerate(["abc","adorable","cute"]):
    print(index+1,value)

"""

"""
设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。
######
import random
def guess():
    randoms = random.randint(1, 101)
    print(randoms)
    n = 1
    while n <=5:
        guess_number = int(input("请输入你要猜的数字："))
        if randoms > guess_number:
            print("你猜错了，数字偏小哦！")
        elif randoms < guess_number:
            print("你猜错了，数字偏大哦！")
        else:
            print("辛运数字是："+ str(randoms)+ ", 恭喜你才对了！！！")
            break
        n += 1
guess()

######
import random
def guess_numbers():
    print 'game start'
    target_num = random.randint(1, 100)
    for times in range(5, 0, -1):
        tag = 'you have ' + str(times) + ' chances to get the special number:'
        input_num = raw_input(tag)
        for s in input_num:
            if ord(s) < 48 or ord(s) > 57:
                print 'please input a valid number'
                break
        else:
            guess_num = int(input_num)
            if guess_num == target_num:
                print 'bingo!'
                break
            elif guess_num > target_num:
                print 'too large'
            else:
                print 'too small'
    else:
        print 'What a pity! you did not got the number'
        
"""


"""
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
######
def count_words():
    words = {}
    with open('import_this.txt','r') as file:
        for line in file:
            for word in line.split():
                for i in range(len(word)):
                    if (ord(word[i]) > 64 and ord(word[i]) < 91 ) or ( ord(word[i]) > 96 and ord(word[i]) < 123 ):
                        word = word[i:]
                        break
                else:
                    continue
                for j in range(len(word)-1, -1, -1):
                    if (ord(word[j]) > 64 and ord(word[j]) < 91 ) or ( ord(word[j]) > 96 and ord(word[j]) < 123 ):
                        word = word[:j+1]
                        break
                words.setdefault(word, 0)
                words[word] += 1
    
    for out in sorted(words.values(), key=lambda x:x[0],reverse=True)[:5]:
        print out[1]

"""


"""
一个完整的URL由5部分组成，格式为：

<scheme>://<netloc>/<path>?<query_params>#<fragment>
例如

url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
解析后得到：

scheme='http'
netloc='mp.weixin.qq.com'
path='/s'
query_params='__biz=MzA4MjEyNTA5Mw==&mid=2652566513'
fragment='wechat_redirect'
问题：设计一个算法，将URL转换成5部分，注意，query_params 要转换成字典类型

query_params={'__biz': 'MzA4MjEyNTA5Mw==', 'mid=2652566513'}

######


import re

class URL(object):
    def __init__(self,url):
        self.url = url
        self.scheme = None
        self.netloc = None
        self.path = None
        self.query_params = {}
        self.fragment = None

    def url_parse(self):
        self.scheme_parse()
        self.netloc_parse()
        self.path_parse()
        self.query_parse()
        self.fragment_parse()

    def scheme_parse(self):
        if self.url:
            self.scheme = re.match(r'.*(?=:)', self.url).group()

    def netloc_parse(self):
        if self.url:
            self.netloc = re.search(r'(?<=//)[a-z]+\.[a-z]+\.[a-z]+\.[a-z]+', self.url).group()

    def path_parse(self):
        if self.url:
            self.path = re.search(r'(?<=\w/).*(?=\?)',self.url).group()

    def query_parse(self):
        if self.url:
            q_str = re.search(r'(?<=\?).*(?=#)',self.url).group()
            for item in re.split(r'&', q_str):
                index = item.find('=')
                self.query_params[item[:index]] = item[index+1:]

    def fragment_parse(self):
        if self.url:
            self.fragment = re.search(r'(?<=#).*', self.url).group()

"""


"""
设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数。尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目

例如执行：

# type用于指定文件类型
python counter.py --type python
输出：

files:10
code_lines:200
comments:100
blanks:20

######
"""

import os
import argparse
class Summarise(object):
    def __init__(self):
        self.pro_name = None
        self.type = None
        self.file_sum = None
        self.files = 0
        self.code_lines = 0
        self.comments = 0
        self.blanks = 0

    def sum_print(self):
        print ('files:', self.files)
        print ('code_lines:', self.code_lines)
        print ('comments:', self.comments)
        print ('blanks:', self.blanks)

    def summarize(self):
        if self.type == None:
            self.type = 'py'
        if self.type == 'py':
            self.file_sum = self.py_file_sum
        elif self.type == 'java':
            self.file_sum = self.java_file_sum
        for entry in os.listdir(self.pro_name):
            entry = os.path.join(self.pro_name, entry)
            if os.path.isfile(entry):
                self.file_sum(entry)
            elif os.path.isdir(entry):
                self.dir_sum(entry)
        self.sum_print()

    def py_file_sum(self, file):
        self.files += 1
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                line = line.lstrip('\t ')
                if line == '\n':
                    self.blanks += 1
                elif line.startswith('#'):
                    self.comments += 1
                elif line.startswith('"""'):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == '"""':
                            break
                elif line.startswith("'''"):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == "'''":
                            break
                else:
                    self.code_lines += 1

    def java_file_sum(self, file):
        self.files += 1
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                line = line.lstrip('\t ')
                if line == '\n':
                    self.blanks += 1
                elif line.startswith('//'):
                    self.comments += 1
                elif line.startswith('/**'):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == '*/':
                            break
                elif line.startswith('/*'):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == '*/':
                            break
                else:
                    self.code_lines += 1

    def dir_sum(self, dir):
        for entry in os.listdir(dir):
            entry = os.path.join(dir, entry)
            if os.path.isfile(entry):
                self.file_sum(entry)
            elif os.path.isdir(entry):
                self.dir_sum(entry)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a summary program',)
    parser.add_argument('--type', default='py', choices=['py','java'], help='This argument specified the language type')
    parser.add_argument('-i', default=os.getcwd(), help='Project that being summarized')
    args = parser.parse_args()
    summa = Summarise()
    summa.pro_name = args.i
    summa.type = args.type
    summa.summarize()

