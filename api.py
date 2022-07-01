import requests


def bing(idx):
    # https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN
    if idx != None:
        url = 'https://bing.com/HPImageArchive.aspx?format=js&idx=' + idx + '&n=1&mkt=zh-CN'
    else:
        url = 'https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    print('url:', url)
    data = requests.get(url).json()
    print(data)
    imgurl = data["images"][0]["url"]
    returl = 'https://cn.bing.com' + imgurl
    print('imgurl:', returl)
    return returl
