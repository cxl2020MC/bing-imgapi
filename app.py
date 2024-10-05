from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import api

app = FastAPI()


@app.get("/")
async def root(idx=1, uhd=None):
   returl = api.bing(idx, uhd)
   return RedirectResponse(returl)
   
