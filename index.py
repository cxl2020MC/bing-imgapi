from flask import Flask, redirect, request, jsonify
import requests
import api
# import requests
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def index():
   类型 = request.args.get('api')
   if 类型 == 'bing':
      idx = request.args.get('idx')
      uhd = request.args.get('uhd')
      returl = api.bing(idx, uhd)
      return redirect(returl)
   elif 类型 == 'info':
      return api.info()
   else:
      return redirect('https://api.cxl2020mc.top?api=bing')
   
@app.route('/ip/')
def get_ip():
   ip = request.remote_addr
   data = requests.get("https://api.live.bilibili.com/client/v1/Ip/getInfoNew?ip=" + ip).json()
   return jsonify(data)

if __name__ == '__main__':
    app.run()
