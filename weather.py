import urllib.request, urllib.error  # 制定URL，获取网页数据
from bs4 import BeautifulSoup

context = ''


def askURL(url):
    head = {  # 模拟服务器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    # 用户代理表示告诉豆瓣我们是什么样的机器，本质上是告诉我们可以接受什么样的内容

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getLocation(url):
    html = askURL(url)
    soup = BeautifulSoup(html, 'html.parser')
    paras = soup.select('.topbar h2')
    paras = paras[0].get_text() + "\n"
    return paras


def getWeather(url):
    html = askURL(url)
    soup = BeautifulSoup(html, 'html.parser')
    paras = soup.select('.txt')
    paras = "今天" + paras[0].get_text() + "\n"
    if paras.find("雨") + 1:
        paras += "出门记得带伞(～￣▽￣)～\n "
    if paras.find("晴") + 1:
        paras += "美美的享受你的阳光呀q(≧▽≦q)\n "
    if paras.find("云") + 1:
        paras += "乌云也遮不住你的好心情呀(^///^)\n "
    return paras


def getWet(url):
    html = askURL(url)
    soup = BeautifulSoup(html, 'html.parser')
    paras = soup.select('.b2')
    paras = paras[0].get_text() + "\n"
    return paras


def getWind(url):
    html = askURL(url)
    soup = BeautifulSoup(html, 'html.parser')
    paras = soup.select('.b3')
    paras = paras[0].get_text() + "\n\n"
    return paras


def saveFile(text):
    global context
    context += text


def getAll(url):
    location = getLocation(url)
    saveFile(location)
    weather = getWeather(url)
    saveFile(weather)
    wet = getWet(url)
    saveFile(wet)
    wind = getWind(url)
    saveFile(wind)


def Weather():
    wuhan = 'https://m.tianqi.com/wuhan/'
    dalian = 'https://m.tianqi.com/dalian/'
    getAll(wuhan)
    getAll(dalian)
    return context
