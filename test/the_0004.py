

foo = open('/home/xingubuntu/Documents/py-0004.txt', 'r')
text = foo.read()
sentence = text.split()

word = list(set(sentence))
#集合真好用

if __name__ == '__main__':
    for w in word:
        print(w + ':' + str(text.count(w)))


