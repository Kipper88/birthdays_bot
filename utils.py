from aiohttp import ClientSession
from cfg import field, keyboard_gift

from db_query import get_db
from datetime import date, datetime
async def requestRuk(apiKey):  
    params = {
        'key': apiKey,  # API ключ  
        'username': 'PortalBTG24',                                   # Имя пользователя
        'password': 'PortalBTG2024',                                   # Пароль
        'action': 'select',                                    # действие
        'entity_id': '104', 
        'select_fields': f"{field['birthday']},\
                           {field['telegram']},\
                           {field['name']},\
                           {field['surname']},\
                           {field['experience']},\
                           {field['status']},\
                           {field['position']},\
                           {field['annualwork']}"
    }
    
    async with ClientSession() as sess:
        resp = await sess.get(url='https://btg-sped.ru/crm/api/rest.php',
                            params=params,
                            ssl=False
                            )
        data = await resp.json(content_type='text/html')
        data = data
    return data


async def birthdays_workers(birth_date):
    today = date.today()
    current_year = today.year

    birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()

    this_year_birthday = birth_date.replace(year=current_year)


    if this_year_birthday < today:
        this_year_birthday = birth_date.replace(year=current_year + 1)


    age = current_year - birth_date.year
    if this_year_birthday > today:
        age -= 1

    if this_year_birthday == today:
        return True
    
    
async def find_button_name(callback_id: str) -> str:
    """
    Поиск названия кнопки по её callback_data.
    :param callback_id: Строка с callback_data
    :return: Название кнопки, если найдено, иначе None
    """
    for _, keyboard_markup in keyboard_gift.items():
        for row in keyboard_markup.inline_keyboard:
            for button in row:
                if button.callback_data == callback_id:
                    return button.text
                
async def is_admin(username) -> bool:
    data = await get_db()
    try:
        if data['users'][username]['is_admin']:
            return True
    except:    
        return False
    return False