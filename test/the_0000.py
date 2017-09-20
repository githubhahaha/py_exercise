from PIL import Image, ImageDraw,ImageFont

url = '/home/xingubuntu/Desktop/tmp.jpg'
text = u'4'


def add4(pic,txt):
    im = Image.open(pic)
    draw = ImageDraw.Draw(im)
    myfont=ImageFont.truetype('/usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-R.ttf',size=60)
    draw.text((160,0), txt,font=myfont,fill = '#ff0000')
    im.show()
    im.save('/home/xingubuntu/Desktop/add_4.jpg','jpeg')


if __name__ == '__main__':
    add4(url,text)