import bs4
import re
import requests
import numpy as np
import time
import json

"""爬取豆瓣top250的电影, ip被封, 下次再来"""


# 伪装请求头
hds = [
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
]
ip = ["119.254.94.93", "113.13.177.53", "183.195.106.118", "113.103.121.68"]

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}


def getHtml(url: str):
    # 得到html文档 设置get或post请求方式
    html = requests.get(
        url,
        proxies={'http': proxies},
        headers=hds[np.random.randint(0, len(hds))]
    )
    return html.text


def localGetHtml():
    return open("F:\\repository\\python\\src\\reptile\\douban.html", 'r', encoding='utf-8')


def calculatePage(url: str):
    html = getHtml(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    page = soup.find(
        "span", class_="next").previous_sibling.previous_sibling.text
    return int(page)


def writeFile(data: str):
    """写文件"""
    with open("F:\\repository\\python\\src\\reptile\\douban.json", "w", 1024, "UTF-8") as f:
        f.write(data)


if __name__ == "__main__":
    # data = []
    # index = 0
    # html = localGetHtml()
    # soup = bs4.BeautifulSoup(html, features='html.parser')
    # item = soup.find_all("div", class_="item")
    # for each in item:
    #     eachItem = {}
    #     img = each.find("div", class_="pic").a.img["src"]
    #     eachItem["id"] = index
    #     index += 1
    #     eachItem["img-src"] = img
    #     hd = each.find("div", class_="hd")
    #     bd = each.find("div", class_="bd")
    #     name = hd.find_all("span", class_="title")
    #     eachItem["zh-name"] = name[0].text
    #     print(index, ":"+name[0].text+" 完成!")
    #     if(len(name) > 1):
    #         eachItem["original-name"] = name[1].text[3:]
    #     timeCountryType = re.search(
    #         r"<br/>\s*(.*)\s/\s*(.*)\s/\s*(.*)\s", str(bd.p))
    #     eachItem["time"] = timeCountryType.group(1)
    #     eachItem["country"] = timeCountryType.group(2)
    #     eachItem["type"] = timeCountryType.group(3)
    #     hot = bd.div.find_all("span")
    #     eachItem["score"] = hot[1].text
    #     eachItem["number-of-people"] = re.search(
    #         r"\d+", str(hot[3].text)).group()
    #     if(bd.find("p", class_="quote")):
    #         eachItem["profile"] = bd.find("p", class_="quote").span.text
    #     data.append(eachItem)
    # writeFile(json.dumps(data, ensure_ascii=False))
    url = "https://movie.douban.com/top250"
    page = calculatePage(url)
    data = []
    index = 0
    for i in range(page):
        time.sleep(np.random.rand()*5)
        html = getHtml(url + "?start=" + str(i*25))
        html = localGetHtml()
        soup = bs4.BeautifulSoup(html, features='html.parser')
        item = soup.find_all("div", class_="item")
        for each in item:
            eachItem = {}
            img = each.find("div", class_="pic").a.img["src"]
            eachItem["id"] = index
            index += 1
            eachItem["img-src"] = img
            hd = each.find("div", class_="hd")
            bd = each.find("div", class_="bd")
            name = hd.find_all("span", class_="title")
            eachItem["zh-name"] = name[0].text
            print(name[0].text+"完成")
            if(len(name) > 1):
                eachItem["original-name"] = name[1].text[3:]
            timeCountryType = re.search(
                r"<br/>\s*(.*)\s/\s*(.*)\s/\s*(.*)\s", str(bd.p))
            eachItem["time"] = timeCountryType.group(1)
            eachItem["country"] = timeCountryType.group(2)
            eachItem["type"] = timeCountryType.group(3)
            hot = bd.div.find_all("span")
            eachItem["score"] = hot[1].text
            eachItem["number-of-people"] = re.search(
                r"\d+", str(hot[3].text)).group()
            if(bd.find("p", class_="quote")):
                eachItem["profile"] = bd.find("p", class_="quote").span.text
            data.append(eachItem)
    writeFile(json.dumps(data, ensure_ascii=False))
