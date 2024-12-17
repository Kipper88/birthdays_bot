from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

field = {}

field['telegram'] = '2681'
field['birthday'] = '2823'
field['name'] = '2439'
field['surname'] = '2438'
field['patronymic'] = '2434'
field['experience'] = '11620'
field['status'] = '7470'
field['position'] = '9086'
field['annualwork'] = '8997'

keyboard_gift = {
    "<1": InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Золотое Яблоко",                                  callback_data="id_AppleGold_<1")],
                [InlineKeyboardButton(text="OZON",                                            callback_data="id_OZON_<1")],
                [InlineKeyboardButton(text="Спортмастер",                                     callback_data="id_Sportmaster_<1")],
                [InlineKeyboardButton(text="Вай-тай",                                         callback_data="id_VaiTai_<1")],
                [InlineKeyboardButton(text="Читай город",                                     callback_data="id_ReadCity_<1")],
                [InlineKeyboardButton(text="Леонардо",                                        callback_data="id_Leonardo_<1")],
                [InlineKeyboardButton(text="RENDEZ-VOUS",                                     callback_data="id_RENDEZ-VOUS_<1")],
                [InlineKeyboardButton(text="Wildberries",                                     callback_data="id_Wildberries_<1")],
                [InlineKeyboardButton(text="М.Видео",                                         callback_data="id_MVideo<1")],
                [InlineKeyboardButton(text="Для неё Топ (подарочный набор)",                  callback_data="id_ForHePrestige_<1")],
                [InlineKeyboardButton(text="Семейные ценности (подарочный набор)",            callback_data="id_FamilyValues_<1")],
                [InlineKeyboardButton(text="Для него Топ (подарочный набор)",                 callback_data="id_ForHeTop_<1")]
        ]),
    "1-3": InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Золотое Яблоко",                                  callback_data="id_AppleGold_1-3")],
                [InlineKeyboardButton(text="OZON (Электронный)",                              callback_data="id_OZON_1-3")],
                [InlineKeyboardButton(text="Вай-тай",                                         callback_data="id_VaiTai_1-3")],
                [InlineKeyboardButton(text="Спирит Фитнес",                                   callback_data="id_SpiritFitnes_1-3")],
                [InlineKeyboardButton(text="Simplewine",                                      callback_data="id_Simplewine_1-3")],
                [InlineKeyboardButton(text="DNS",                                             callback_data="id_DNS_1-3")],
                [InlineKeyboardButton(text="FRENH KISS",                                      callback_data="id_FRENH_KISS_1-3")],
                [InlineKeyboardButton(text="HOFF",                                            callback_data="id_HOFF_1-3")],
                [InlineKeyboardButton(text="Для неё Элит (подарочный набор)",                 callback_data="id_ForHePrestige_1-3")],
                [InlineKeyboardButton(text="SPA & Массаж (подарочный набор)",                 callback_data="id_SPA+Massage_1-3")],
                [InlineKeyboardButton(text="Экстрим Элит (подарочный набор)",                 callback_data="id_ExtremeElite_1-3")],
                [InlineKeyboardButton(text="СПА Элит (подарочный набор)",                     callback_data="id_SPAElite_1-3")]
        ]),
    ">3": InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Золотое Яблоко ",                                callback_data="id_AppleGold_>3")],
                [InlineKeyboardButton(text="OZON (электронный)",                             callback_data="id_OZON_>3")],
                [InlineKeyboardButton(text="Вай тай",                                        callback_data="id_VaiTai_>3")],
                [InlineKeyboardButton(text="Спирит фитнес  ",                                callback_data="id_SpiritFitnes_>3")],
                [InlineKeyboardButton(text="Küchenland",                                     callback_data="id_Küchenland_>3")],
                [InlineKeyboardButton(text="Wildberries",                                    callback_data="id_Wildberries_>3")],
                [InlineKeyboardButton(text="Simplewine",                                     callback_data="id_Simplewine_>3")],
                [InlineKeyboardButton(text="Технопарк",                                      callback_data="id_Technopark_>3")],
                [InlineKeyboardButton(text="RENDEZ-VOUS",                                    callback_data="id_RENDEZ-VOUS_>3")],
                [InlineKeyboardButton(text="RANDEWOO",                                       callback_data="id_RANDEWOO_>3")],
                [InlineKeyboardButton(text="Для него Престиж (подарочный набор)",            callback_data="id_ForHePrestige_>3")],
                [InlineKeyboardButton(text="Мужской праздник (подарочный набор)",            callback_data="id_ManParty_>3")],
                [InlineKeyboardButton(text="СПА Престиж (подарочный набор)",                 callback_data="id_SPAPrestige_>3")]
        ])
}

list_kb = callback_data_list = [
    # Клавиатура "<1"
    "id_AppleGold_<1",
    "id_OZON_<1",
    "id_Sportmaster_<1",
    "id_VaiTai_<1",
    "id_ReadCity_<1",
    "id_Leonardo_<1",
    "id_RENDEZ-VOUS_<1",
    "id_Wildberries_<1",
    "id_MVideo<1",
    "id_ForHePrestige_<1",
    "id_FamilyValues_<1",
    "id_ForHeTop_<1",

    # Клавиатура "1-3"
    "id_AppleGold_1-3",
    "id_OZON_1-3",
    "id_VaiTai_1-3",
    "id_SpiritFitnes_1-3",
    "id_Simplewine_1-3",
    "id_DNS_1-3",
    "id_FRENH_KISS_1-3",
    "id_HOFF_1-3",
    "id_ForHePrestige_1-3",
    "id_SPA+Massage_1-3",
    "id_ExtremeElite_1-3",
    "id_SPAElite_1-3",

    # Клавиатура ">3"
    "id_AppleGold_>3",
    "id_OZON_>3",
    "id_VaiTai_>3",
    "id_SpiritFitnes_>3",
    "id_Küchenland_>3",
    "id_Wildberries_>3",
    "id_Simplewine_>3",
    "id_Technopark_>3",
    "id_RENDEZ-VOUS_>3",
    "id_RANDEWOO_>3",
    "id_ForHePrestige_>3",
    "id_ManParty_>3",
    "id_SPAPrestige_>3"
]