import markdown
import requests
from mdx_math import MathExtension
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

html_head = """
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<link href="https://cdn.jsdelivr.net/gh/RookieFanzk/link/github.css" rel="stylesheet">
</head>

<body>
<h2>油价</h1>
"""
html_tail = "\n</body>\n</html>"

exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc', MathExtension(enable_dollar_delimiter=True)]

result = open("index.md", mode="r", encoding="utf-8")
readme = open('README.md', mode='w', encoding='utf-8')
readme.truncate()
text = result.read()
result.close()
body = markdown.Markdown(extensions = exts)
html = html_head + body.convert(text) + html_tail
print(html, file=readme)
readme.close()
print(html)
