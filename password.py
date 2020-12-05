import itertools as its
#迭代器
words = '1234567890'

r = its.product(words, repeat = 5)
#保存在文件中  追加
dic = open('pass.txt','a')
for i in r:
    #123456
    #('c','c','c')
    #ccc
    dic.write("".join(i))
    #换行
    dic.write("".join("\n"))
dic.close()