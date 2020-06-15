import re


"""
正则表达式相当于是一个抽象规则, 如线性表和顺序表和链表的关系
编程语言对这个接口进行实现, 不同编程语言有不同正则表达式函数, 但本质功能相同
查找、替换
python规则:
查找:re.match(), re.search(), re.findall()
替换:re.sub()
"""

# re.match() at the start of the string for once
# re.search() all the string for once
# re.findAll() for all the substring
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# re.I不区分大小写, re.M多行匹配
# re.sub()替换
# .groups() .group() .start() .end() .span()
# print(re.findall(r"\d+", "r12unoob 123 goo1234gle 12345"))
# print(re.search(r"([\w]+) ([\w]+)", "Hello World Wide Web").groups())
s = """<p class="">
                            导演: 陈凯歌 Kaige Chen   主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...<br/>
                            1993 / 中国大陆 中国香港 / 剧情 爱情 同性
                        </p>"""
s1 = """<p class="">
                                            导演: 万籁鸣 Laiming Wan / 唐澄 Cheng Tang   主演: 邱岳峰 Yuefeng Qiu
                                            /...<br/>
                                            1961(中国大陆) / 1964(中国大陆) / 1978(中国大陆) /
                                            2004(中国大陆) / 中国大陆 / 动画 奇幻
                                        </p>"""
data = re.search(r"<br/>\s*(.*)\s/\s*(.*)\s/\s*(.*)\s", s1)
print(data.groups())
