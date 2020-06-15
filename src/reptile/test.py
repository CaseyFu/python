import requests
import bs4


# 获取总共的页码
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # previous_sibling的意思是找前一个兄弟节点
    depth = soup.find(
        "span", class_="next").previous_sibling.previous_sibling.text
    return int(depth)

# 主函数


def main():
    # 如果没有指定User-Agent，python会用默认的。网站会拒绝访问，这里指定了具体的浏览器访问
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

    host = "https://movie.douban.com/top250"
    res = requests.get(host, headers=headers)
    depth = find_depth(res)

    for i in range(depth):
        url = host + '/?start=' + str(25*i)
        res = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        # print(soup)
        # <div class="hd">
        #                         <a href="https://movie.douban.com/subject/1292052/" class="">
        #                             <span class="title">肖申克的救赎</span>
        #                                     <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
        #                                 <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
        #                         </a>
        #                             <span class="playable">[可播放]</span>
        #                     </div>
        # 由于div下的class跟python中的class重名，所以这里用的是class_
        # targets = soup.find_all("div", class_="hd")
        print(soup)
        # for each in targets:
        # each.a.span.text默认只会获取a标签下的第一个span，如果是each.a.contents就会获取a标签下的所有标签
        # print(each.a.span.text)


if __name__ == '__main__':
    main()
