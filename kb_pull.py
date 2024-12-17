from aiogram import Router, F, Bot 
from aiogram.types import CallbackQuery

from utils import requestRuk, find_button_name
from cfg import list_kb, field
import json
import os
import asyncio

from dotenv import load_dotenv

load_dotenv()

RUK_TOKEN = os.getenv('RUK_TOKEN')

router = Router()

@router.callback_query(F.data.in_(list_kb))
async def process_callback(query: CallbackQuery, bot: Bot):
    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await query.message.answer(f'Ваш выбор учтён!')
    
    
    with open('db.json', 'r', encoding='utf-8') as f:
        f = f.read()
        js = json.loads(f)

        resp = await requestRuk(RUK_TOKEN)
        
        workers = [(x[field['telegram']], x[field['birthday']], x[field['name']], x[field['surname']], x[field['experience']], x[field['position']], x[field['status']]) for x in resp['data']]
            
        if query.from_user.username in js['users']:
            for x in workers:
                if x[0].split('/')[-1] == query.from_user.username:
                    for j in js['admins'].items():
                        await bot.send_message(j[1]['id'], f'Будущий именинник {x[2]} {x[3]}, стаж работы {x[4]} (лет) выбрал подарок {await find_button_name(query.data)}')
                        await asyncio.sleep(5)
                    break
            