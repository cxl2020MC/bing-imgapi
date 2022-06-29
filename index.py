from flask import Flask, redirect, request
import requests
app = Flask(__name__)

@app.route('/bing/')
def bing():
   # https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN
   idx = request.args.get('idx')
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
   return redirect(returl)

if __name__ == '__main__':
   app.run()
