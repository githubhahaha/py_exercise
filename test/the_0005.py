#1136*640
from PIL import Image
import os
import glob


path = "/home/xingubuntu/Pictures"


def convert_pic(pic_name, width=640, height=1136):
    img = Image.open(pic_name)
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(os.path.join(path+'/tmp', os.path.basename(pic_name)))


if __name__ == '__main__':
    for picname in glob.glob(path+'/*.jpg'):
        convert_pic(picname)






