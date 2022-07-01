from flask import Flask, redirect, request
import api
# import requests
app = Flask(__name__)


@app.route('/')
def index():
   类型 = request.args.get('api')
   if 类型 == 'bing':
      idx = request.args.get('idx')
      returl = api.bing(idx)
      return redirect(returl)
   else:
      return redirect('https://www.cxl2020mc.top')


if __name__ == '__main__':
    app.run()
