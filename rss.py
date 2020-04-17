import requests
import feedgenerator
from lxml import etree

url = 'https://ani.gamer.com.tw/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

anihtml = requests.get(url, headers=headers).text
a = etree.HTML(anihtml)
feed = feedgenerator.Rss201rev2Feed(
    title='巴哈動畫瘋', link='https://ani.gamer.com.tw', description='RSS解析版', language='zh')

for _ in a.xpath('//div[@name="newanimeul"]')[0].xpath('div/div/a'):
    aniname = _.xpath('div[@class="newanime__content__info"]/p')[0].text
    link = _.get('href')
    description = '更新至' + \
        _.xpath('div[@class="newanime__content__info"]/span')[2].text + '集'
    # _.xpath('div[@class="newanime__content__info"]/span')[1].text[:5]
    feed.add_item(title=aniname, link=link, description=description)
print(feed.writeString('utf-8'))
