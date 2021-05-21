from typing import Union
import json
from aiohttp import ClientSession
from io import BytesIO

class DagpiClient:
    BASE = "https://api.dagpi.xyz"
    def __init__(self, session : ClientSession, token : str):
        self.token = token
        self.session = session
        self.headers = {
            "Authorization" : self.token
        }
    
    async def request(self, route : str, **params) -> Union[BytesIO, dict]:
        image = params.pop("image", True)
        if image is True:
            async with self.session.get(self.BASE + route, params = params, headers = self.headers) as resp:
                image_data = await resp.read()
                buffer = BytesIO(image_data)
                buffer.seek(0)
                return buffer
        else:
            async with self.session.get(self.BASE + route, params = params, headers = self.headers) as resp:
                data = await resp.text()
                data = json.loads(data)
                return data







class AniListClient:
    BASE = "https://graphql.anilist.co"
    def __init__(self, session : ClientSession):
        self.session = session
    
    async def request(self, query : str, **params):
        async with self.session.post(self.BASE, json = {"query" : query,  "variables" : params}) as resp:
            data = await resp.json()
            return data



class KawaiiRedClient:
    BASE = "https://kawaii.red/api"

    def __init__(self, session : ClientSession, token : str):
        self.session = session
        self.token = token

    async def request(self, endpoint : str) -> dict:
        async with self.session.get(self.BASE + endpoint + f"token={self.token}") as resp:
            data = await resp.json()
            return data



class PistonClient:
    BASE = "https://emkc.org/api/v2"
    def __init__(self, session : ClientSession):
        self.session = session
    
    async def request(self, endpoint : str, code : str, language : str, version : str) -> dict:
        data = {
            "language": language,
            "version": version,
            "files": [
                {
                    "name": "main.py",
                    "content": code
                }
            ],
        }
        async with self.session.post(self.BASE + endpoint, json = data) as resp:
            print(resp.status)
            js = await resp.json()
            return js
            
