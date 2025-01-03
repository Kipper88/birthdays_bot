from aiofiles import open
import json

async def get_db_json():
    async with open('db.json', 'r', encoding='utf-8') as f: 
        return json.loads(await f.read())
    
async def insert_db_json(data):
    async with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)