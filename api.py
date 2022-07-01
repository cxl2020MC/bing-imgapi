import requests, time


def bing(idx, UHD):
    # https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN
    idxurl = 'https://cn.bing.com'
    if idx != None:
        url = idxurl + '/HPImageArchive.aspx?format=js&idx=' + idx + '&n=1&mkt=zh-CN'
    else:
        url = idxurl + '/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    print('url:', url)
    data = requests.get(url).json()
    print(data)
    imgurl = data["images"][0]["url"]
    if UHD != None:
        imgurl = imgurl.replace('_1920x1080', '_UHD')
    returl = 'https://cn.bing.com' + imgurl
    print('imgurl:', returl)
    return returl

def info():
    cn_url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    en_url = 'https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    # print('url:', url)
    开始时间 = time.time()
    data = requests.get(cn_url).json()
    结束时间 = time.time()
    print(data)
    中国节点用时 = 结束时间 - 结束时间
    开始时间 = time.time()
    data = requests.get(en_url).json()
    结束时间 = time.time()
    print(data)
    全球节点用时 = 结束时间 - 开始时间
    msg = '''info：
bing壁纸api请求用时

中国: {中国节点用时} s

全球: {全球节点用时} s'''.format(中国节点用时 = 中国节点用时, 全球节点用时 = 全球节点用时)
    return msg