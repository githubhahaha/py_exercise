import random


def make_random():
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(seed)-1
    string = ''
    for i in range(4):
        for j in range(4):
            string += random.choice(seed)
        if i != 3:
            string += '-'
    return string


if __name__ == '__main__':
    for i in range(200):
        print(make_random())
