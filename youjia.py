import codecs

import markdown as markdown
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

index = open('index.md', mode='w', encoding='utf-8')
index.truncate()
print("| 地区 | 89号汽油 | 92号汽油 | 95号汽油 | 98号汽油 | 0号柴油 | 更新日期 |", file=index)
print("| --- | --- | --- | --- | --- | --- | --- |", file=index)
for tr_index in range(2, 33):
    for td_xpath in range(1, 8):
        if td_xpath == 1:
            xpath = '//div[@class="cpbaojia"]/table/tr[' + str(tr_index) + ']/td[' + str(td_xpath) + ']/a/text()'
        else:
            xpath = '//div[@class="cpbaojia"]/table/tr[' + str(tr_index) + ']/td[' + str(td_xpath) + ']/text()'
        if count == 0:
            print("| " + html.xpath(xpath)[0], end="", file=index)
        elif count == 6:
            print(" | " + html.xpath(xpath)[0] + " |", file=index)
            count = 0
            continue
        else:
            print(" | " + html.xpath(xpath)[0], end="", file=index)
        count += 1

index.close()

result = codecs.open("index.md", mode="r", encoding="utf-8")
text = result.read()

readme = open('README.md', mode='w', encoding='utf-8')
readme.truncate()
read = open("index.md", encoding="utf-8")
contents = read.readlines()
readme_text = ""
for content in contents:
    readme_text += content.replace('\n', '\n')
print("## 油价", file=readme)
print(readme_text, file=readme)
print(readme_text)
read.close()
readme.close()

html = markdown.markdown(text)

index = open('index.md', mode='w', encoding='utf-8')
index.truncate()
print(html, file=index)
index.close()
