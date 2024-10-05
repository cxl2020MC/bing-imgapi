import aiohttp
import time

api_url = 'https://cn.bing.com/HPImageArchive.aspx'


async def bing(idx, UHD):
    # https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN
    # url = f'{idxurl}/HPImageArchive.aspx?format=js&idx={idx}&n=1&mkt=zh-CN'
    parms = {'format': 'js', 'idx': idx, 'n': 1, 'mkt': 'zh-CN'}
    # print('url:', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=parms) as response:
            data = response.json()
            print(data)
            imgurl = data["images"][0]["url"]
            if UHD:
                imgurl = imgurl.replace('_1920x1080', '_UHD')
            returl = 'https://cn.bing.com' + imgurl
            print('imgurl:', returl)
            return returl
