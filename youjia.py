import requests

from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
}

url = "http://youjia.chemcp.com/"

response = requests.get(url, headers=headers)
response.encoding = 'gb2312'

html = etree.HTML(response.text)

count = 0
el = {}
result = []

for tr_index in range(2, 33):
    for td_xpath in range(1, 8):
        if td_xpath == 1:
            xpath = '//div[@class="cpbaojia"]/table/tr[' + str(tr_index) + ']/td[' + str(td_xpath) + ']/a/text()'
        else:
            xpath = '//div[@class="cpbaojia"]/table/tr[' + str(tr_index) + ']/td[' + str(td_xpath) + ']/text()'
        if count == 0:
            el['地区'] = html.xpath(xpath)[0]
        elif count == 1:
            el['89号汽油'] = html.xpath(xpath)[0]
        elif count == 2:
            el['92号汽油'] = html.xpath(xpath)[0]
        elif count == 3:
            el['95号汽油'] = html.xpath(xpath)[0]
        elif count == 4:
            el['98号汽油'] = html.xpath(xpath)[0]
        elif count == 5:
            el['0号柴油'] = html.xpath(xpath)[0]
        elif count == 6:
            el['更新日期'] = html.xpath(xpath)[0]
            result.append(el)
            el = {}
            count = 0
            continue
        count += 1

print(result)

