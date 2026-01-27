from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, ReplyKeyboardRemove
from translations import STRINGS

def lang_keyboard():
    kb = [
        [InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇺🇸 English", callback_data="lang_en")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def main_menu(lang='uz', is_admin=False):
    s = STRINGS[lang]
    url = f"https://khamidovkhusnidd1n.github.io/Yummy/?lang={lang}"
    
    kb = [
        [KeyboardButton(text=s['main_menu_btn'], web_app=WebAppInfo(url=url))],
        [KeyboardButton(text=s['location_btn_menu']), KeyboardButton(text=s['about_btn_menu'])],
        [KeyboardButton(text=s['contact_btn_menu']), KeyboardButton(text=s['feedback_btn_menu'])]
    ]
    
    if is_admin:
        kb.append([KeyboardButton(text="🛠 Admin Panel")])
        
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def phone_keyboard(lang='uz'):
    s = STRINGS[lang]
    kb = [[KeyboardButton(text=s['phone_btn'], request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def delivery_method_kb(lang='uz'):
    s = STRINGS[lang]
    kb = [
        [KeyboardButton(text=s['method_delivery'])],
        [KeyboardButton(text=s['method_takeaway'])]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def location_keyboard(lang='uz'):
    s = STRINGS[lang]
    # No button, just text input needed, but we can provide a small back button or similar if needed
    # For now, just return None or a simple keyboard to clear previous one
    return ReplyKeyboardRemove()

def order_confirm_kb(lang='uz'):
    s = STRINGS[lang]
    kb = [
        [KeyboardButton(text=s['confirm_btn'])],
        [KeyboardButton(text=s['cancel_btn'])]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def promo_skip_kb(lang='uz'):
    s = STRINGS[lang]
    kb = [[KeyboardButton(text=s.get('skip_btn', 'Skip ➡️'))]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
