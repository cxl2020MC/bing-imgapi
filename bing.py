from flask import Flask, redirect
import requests
app = Flask(__name__)

@app.route('/')
def index():
   # return 'Hello World'
   # https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN
   url = 'https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
   data = requests.get(url).json()
   print(data)
   imgurl = data["images"][0]["url"]
   returl = 'https://cn.bing.com' + imgurl
   print('imgurl:', returl)
   return redirect(returl)

if __name__ == '__main__':
   app.run()