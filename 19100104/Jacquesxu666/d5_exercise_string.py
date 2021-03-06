text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text = text.replace(',', ' ').replace('.', ' ').replace(  '--', ' ').replace('!', ' ').replace('*', ' ')
a = text.split()  # 2.将字符串中含"ea"的单词删除
for i in a :  
    if "ea" in i:
       del i   
print(a)

print(text.replace('better', 'worse')) #3.将字符串中的better替换成worse

print(text.swapcase())  #4.将字符串中的大写转小写，小写转大写

print(sorted(a, key=str.lower)) #5.将所有单词按a...z升序排列




