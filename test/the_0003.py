import redis
import random


r = redis.Redis(host='0.0.0.0', port=6379)


def make_random():
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(seed)-1
    string = ''
    for x in range(4):
        for j in range(4):
            string += random.choice(seed)
        if x != 3:
            string += '-'
    return string


if __name__ == '__main__':
    for i in range(200):
        s = make_random()
        r.set('key'+str(i), s)
        print(s)
    print('/')
    for i in range(200):
        print('key' + str(i))
        print(r.get('key'+str(i)))

#不是很理解nosql的用途，redis和MySQL用完之后都已经卸载了，什么时候用再现装吧
