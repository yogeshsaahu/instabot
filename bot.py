import requests
import time
from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys
from instabot import Bot
import schedule
from operator import itemgetter



"""this function used for get data from api and coverted into image"""
def image_create():
        response = requests.get('https://zenquotes.io/api/today')
        change = response.json()
        title = list(map(itemgetter('q'), change))
        author = list(map(itemgetter('a'), change))
        title = ''.join(title)
        author = ''.join(author)

        print(str(title))
        print(str(author))

        astr = title
        para = textwrap.wrap(astr, width=30)

        MAX_W, MAX_H = 1080, 1080
        # im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
        im = Image.open('banner1.jpeg')
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('arial.ttf', 35,)
        font2 = ImageFont.truetype('arial.ttf', 25,)

        current_h, pad = 500, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill=(0, 0, 0))

            current_h += h + pad

        draw.multiline_text((700, 700), author, align="center", font=font2, fill=(0, 0, 0))

        im.save('img.jpg')


""" this is instagram bot section """
def bot():
    bot = Bot()
    bot.login(username="cyber_annex", password="teamannex360@")
    hashtags = " follow us - #quotes #love #motivation #life #quoteoftheday #instagram #inspiration " \
               "#motivationalquotes #instagood #quote #follow #inspirationalquotes #like #success #bhfyp " \
               "#positivevibes #lovequotes #poetry "

    bot.upload_photo("images/img.jpg", caption=hashtags)


def run_bot():
    img = image_create()
    time.sleep(10)
    start = bot()


if __name__ == "__main__":
    schedule.every(12).hours.do(run_bot)

    while True:
        schedule.run_pending()
        time.sleep(1)
