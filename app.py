from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import api

app = FastAPI()


@app.get("/")
async def root(idx: int = 0, uhd: bool = False):
    returl = await api.bing(idx, uhd)
    return RedirectResponse(returl)
