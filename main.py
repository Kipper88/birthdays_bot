from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from dotenv import load_dotenv
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


import asyncio
import json
import os
import re

from utils import requestRuk, birthdays_workers, is_admin
from cfg import field, keyboard_gift
from kb_pull import router

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RUK_TOKEN = os.getenv('RUK_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(router)

async def while_check_birthdays():
    resp = await requestRuk(RUK_TOKEN)
    
    today = datetime.today().date()
        
    workers = [(x[field['telegram']], x[field['birthday']], x[field['name']], x[field['surname']], x[field['experience']], x[field['position']], x[field['status']], x[field['annualwork']]) for x in resp['data']]
        
    birthdays = []
    tech_tg = []
    annualworks = []
    for x in workers:
        if x[1] and x[1].strip() != '' and x[7] and x[7].strip() != '':
            birth_date = datetime.strptime(x[1], '%d.%m.%Y').date()
            today = datetime.today().date()
            birth_date_this_year = birth_date.replace(year=today.year)
            
            annualwork_date = datetime.strptime(x[7], '%d.%m.%Y').date()
            annualwork_date_this_year = annualwork_date.replace(year=today.year)

            if birth_date_this_year < today:
                birth_date_this_year = birth_date.replace(year=today.year + 1)
            if annualwork_date_this_year < today:
                annualwork_date_this_year = annualwork_date_this_year.replace(year=today.year + 1)

            days_difference = (birth_date_this_year - today).days
            days_difference_annualwork = (annualwork_date_this_year - today).days
            if x[6] != 'Уволен':
                if days_difference == 7:
                    birthdays.append(f"- {birth_date_this_year}: {x[2]} {x[3]}, {x[5]}, стаж {x[4]} (лет)")
                if days_difference == 3:    
                    tech_tg.append((x[0].split('/')[-1], int(x[4]), x[2], x[3]))
                if days_difference_annualwork == 7:
                    annualworks.append(f"- {annualwork_date_this_year}: {x[2]} {x[3]}, {x[5]}, стаж {x[4]} (лет)")
    
    if len(birthdays) > 0:
        text = f'🎉 Напоминание!\nЧерез 7 дней ({today + timedelta(days=7)}) празднует(-ют) день рождения:\n'
            
        for i in birthdays:
            text += f'{i}\n'
        with open('db.json', 'r', encoding='utf-8') as f:
            js = json.load(f)
        
        for i in js['admins'].items(): 
            await bot.send_message(i[1]['id'], text)
            await asyncio.sleep(3)
       
    if len(tech_tg) > 0: 
        with open('db.json', 'r', encoding='utf-8') as f:
            f = f.read()
            js = json.loads(f)
        for i in tech_tg:
            if i[0] in js['users']:   
                if i[1] < 1:
                    inline_kb = keyboard_gift['<1']    
                if i[1] in [1,2,3]:
                    inline_kb = keyboard_gift['1-3']   
                if i[1] > 3:
                    inline_kb = keyboard_gift['>3']
                await bot.send_message(js['users'][i[0]]["id"], f'С наступающим днём рождения, {i[2]} {i[3]}!\nВыберите свой подарок, нажав на кнопку', reply_markup=inline_kb)
                await asyncio.sleep(3)

    if len(annualworks) > 0:
        text = f'🎉 Напоминание!\nЧерез 7 дней ({today + timedelta(days=7)}) празднует(-ют) годовщину принятия на работу:\n'
            
        for i in birthdays:
            text += f'{i}\n'
        with open('db.json', 'r', encoding='utf-8') as f:
            js = json.load(f)
        
        for i in js['admins'].items(): 
            await bot.send_message(i[1]['id'], text) 
            await asyncio.sleep(3)
        
            
            
@dp.message(Command("birthdays"))
async def birthday(msg: Message):
    if not await is_admin(msg.from_user.username, msg.from_user.id):
        return
    
    resp = await requestRuk(RUK_TOKEN)
    
    today = datetime.today().date()
    
    workers = [(x[field['telegram']], x[field['birthday']], x[field['name']], x[field['surname']], x[field['experience']], x[field['status']]) for x in resp['data']]
    
    birthdays = []
    for x in workers:
        if x[1] and x[1].strip() != '' and x[5] != 'Уволен':
            birth_date = datetime.strptime(x[1], '%d.%m.%Y').date()
            today = datetime.today().date()
            birth_date_this_year = birth_date.replace(year=today.year)

            if birth_date_this_year < today:
                birth_date_this_year = birth_date.replace(year=today.year + 1)

            days_difference = (birth_date_this_year - today).days
            if days_difference <= 14:
                birthdays.append(f"- {birth_date_this_year.strftime('%d-%m-%Y')}: {x[2]} {x[3]}, стаж работы {x[4]} (лет)")
    
    text = '🎂 Ближайшие дни рождения:\n'
    
    for i in birthdays:
        text += f'{i}\n' if i != '' else ''
    
    
    await msg.reply(text)
    
    
@dp.message(Command('annualwork'))
async def lalala(msg):
    if not await is_admin(msg.from_user.username, msg.from_user.id):
        return
    
    resp = await requestRuk(RUK_TOKEN)
    
    today = datetime.today().date()
    
    workers = [(x[field['telegram']], x[field['name']], x[field['surname']], x[field['experience']], x[field['annualwork']], x[field['status']]) for x in resp['data']]

    birthdays = []
    for x in workers:
        if x[1] and x[1].strip() != '' and x[4].strip() != '' and x[5] != 'Уволен':
            annualwork_date = datetime.strptime(x[4], '%d.%m.%Y').date()
            today = datetime.today().date()
            annualwork_date_this_year = annualwork_date.replace(year=today.year)

            if annualwork_date_this_year < today:
                annualwork_date_this_year = annualwork_date.replace(year=today.year + 1)

            days_difference = (annualwork_date_this_year - today).days
            if days_difference <= 14:
                birthdays.append(f"- {annualwork_date_this_year.strftime('%d-%m-%Y')}: {x[1]} {x[2]}, стаж работы {x[3]} (лет)")
    
    text = 'Ближайшие годовщины:\n' if len(birthdays) > 0 else 'Ближайших годовщин за 14 дней нет'
    
    for i in birthdays:
        text += f'{i}\n' if i != '' else ''
    
    
    await msg.reply(text)
    
    
        
@dp.message(Command('setadmin'))
async def setuser(msg: Message):
    if not await is_admin(msg.from_user.username, msg.from_user.id):
        return
    pattern = r"/setadmin\s+(\w+)\s+(\d+)"
    match = re.search(pattern, msg.text)
    if match:
        username = match.group(1)
        userid = match.group(2)
    else:
        await msg.reply('Произошла непредвиденная ошибка. Возможно, Вы ввели данные неверно, попробуйте еще раз.\nПример:\n/setuser\nusername\nuserid')    
        return
    
    try:
        username = str(username)
        userid = int(userid)
        
        with open('db.json', 'r', encoding='utf-8') as f:
            f = f.read()
            js = json.loads(f)
            
        js['admins'][username] = {
            "id": userid
        }
        
        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, ensure_ascii=False)
        
        await msg.reply('Админ успешно добавлен')
        
    except Exception:
        await msg.reply('Произошла непредвиденная ошибка. Возможно, Вы ввели данные неверно, попробуйте еще раз.')
        
        
@dp.message(Command('deleteadmin'))
async def deleteadmin(msg: Message):
    if not await is_admin(msg.from_user.username, msg.from_user.id):
        return
    
    pattern = r"/deleteadmin\s+(\w+)"
    match = re.search(pattern, msg.text)
    if match:
        username = match.group(1)
    
    with open('db.json', 'r', encoding='utf-8') as f:
            f = f.read()
            js = json.loads(f)
    
    try:
        username = str(username)
        
        del js['admins'][username]
        
        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, ensure_ascii=False)
        
        await msg.reply('Админ успешно удален')
    except Exception:
        await msg.reply('Произошла непредвиденная ошибка. Возможно, Вы ввели данные неверно, попробуйте еще раз.')    
        
@dp.message(Command('showadmins'))
async def showadmins(msg: Message):
    if not await is_admin(msg.from_user.username, msg.from_user.id):
        return
    
        
    with open('db.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
            
    text = ''
    for x in js['admins']:
        text += f"\nusername: {x}\n\tuserid: {js['admins'][x]['id']}\n"
                
    # for x in js['admins']:
    #     for j in workers:
    #         if j[0].split('/')[-1] == x:
    #             text += f"{j[1]} {j[2]}\n\tusername: {x}\n\tuserid: {js['admins'][x]['id']}\n"
    
    await msg.reply(text if text != '' else 'Администраторы не найдены')
    
@dp.message(CommandStart())
async def start(msg: Message):
    with open('db.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
        
    resp = await requestRuk(RUK_TOKEN)
    
    workers = [(x[field['telegram']], x[field['birthday']]) for x in resp['data']]
    
    for i in workers:
        if msg.from_user.username == i[0].split('/')[-1]:
            if msg.from_user.username not in js['users']:
                js['users'][msg.from_user.username] = {
                    "id": msg.from_user.id,
                    "is_admin": False
                }
                with open('db.json', 'w', encoding='utf-8') as f:
                    js = json.dump(js, f, indent=4)
                    
                await msg.reply('Вы были зарегистрированы! ✅')
            else:
                await msg.reply('Вы уже зарегистрированы! ❌')
            
            return
    await msg.reply('Вас нет в базе данных CRM (возможно нет только Telegram аккаунта) ❌')
    
async def main():
    asyncio.create_task(check_schedule())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def check_schedule():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        while_check_birthdays, 
        trigger=CronTrigger(hour=10),
        id="check_birthdays",
        replace_existing=True,
    )

    scheduler.start()
        
        
if __name__ == "__main__":
    asyncio.run(main())