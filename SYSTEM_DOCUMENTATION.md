# 🍔 YUMMY BOT - Tizim Hujjati

## 📋 Mundarija
1. [Tizim Tavsifi](#tizim-tavsifi)
2. [Arxitektura](#arxitektura)
3. [Ma'lumotlar Bazasi](#malumotlar-bazasi)
4. [Foydalanuvchi Buyurtma Jarayoni](#foydalanuvchi-buyurtma-jarayoni)
5. [Admin Paneli](#admin-paneli)
6. [Promo Kodlar](#promo-kodlar)
7. [Tillar Qo'llabi](#tillar-qollabi)
8. [API Integratsiyasi](#api-integratsiyasi)
9. [Fayllar Strukturi](#fayllar-strukturi)
10. [O'rnatish va Ishga Tushirish](#ornatish-va-ishga-tushirish)

---

## 🎯 Tizim Tavsifi

**YUMMY BOT** - Telegram bot orqali fast-food buyurtma beradigan web-ilovasi. Tizim quyidagi xususiyatlarga ega:

- ✅ **Multilingual qo'llabi** (O'zbekcha, Ruscha, Inglizcha)
- ✅ **WebApp integratsiyasi** - Maxsus web interfeysi bilan buyurtma qilish
- ✅ **Promo kod tizimi** - Chegirma beradigan promo kodlar
- ✅ **Admin paneli** - Buyurtmalarni boshqarish, statistika, mailing
- ✅ **Avtomatik SMS xabarlari** - Buyurtma holatini yangilash
- ✅ **SQLite ma'lumotlar bazasi** - Mahalliy saqlash
- ✅ **Webhook/Polling modlari** - Cloud va lokal ishga tushirish

---

## 🏗️ Arxitektura

### Texnologiyalar
```
┌─────────────────────────────────────────┐
│          TELEGRAM BOT (aiogram)         │
│  - User Handlers                        │
│  - Admin Handlers                       │
│  - WebApp Data Handler                  │
└────────────────┬────────────────────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
    ▼            ▼            ▼
┌──────┐  ┌──────────┐  ┌──────────┐
│ User │  │ WebApp   │  │ Admin    │
│Routes│  │ Handler  │  │ Routes   │
└──────┘  └──────────┘  └──────────┘
    │            │            │
    └────────────┼────────────┘
                 │
    ┌────────────▼────────────┐
    │   KEYBOARD BUTTONS      │
    │  (user_keyboards.py)    │
    │  (admin_keyboards.py)   │
    └────────────┬────────────┘
                 │
    ┌────────────▼────────────┐
    │   DATABASE (SQLite)     │
    │  - Users                │
    │  - Orders               │
    │  - Products             │
    │  - Promo Codes          │
    │  - Admins               │
    └─────────────────────────┘
```

### Fayllar Tasnifi

**Backend:**
- `main.py` - Bot ishga tushirish, webhook/polling config
- `config.py` - Environment variablelari
- `database.py` - SQLite ma'lumotlar bazasi
- `translations.py` - Tillar (UZ, RU, EN)

**Handlerlari:**
- `handlers/user_handlers.py` - Foydalanuvchi buyurtma jarayoni
- `handlers/admin_handlers.py` - Admin panel

**Keyboard Markup:**
- `keyboards/user_keyboards.py` - Foydalanuvchi tugmalari
- `keyboards/admin_keyboards.py` - Admin tugmalari

**Frontend:**
- `index.html` - Web ilovasi UI
- `menu_data.js` - Menu ma'lumotlari

---

## 💾 Ma'lumotlar Bazasi

### Jadvallar

#### 1. **users**
```sql
user_id (PRIMARY KEY) - Telegram user ID
full_name - Foydalanuvchi ismi
username - Telegram username
phone - Telefon raqami
lang - Tanlangan til (uz, ru, en)
```

#### 2. **orders**
```sql
order_id (PRIMARY KEY) - Buyurtma ID
user_id (FOREIGN KEY) - Foydalanuvchi
items - JSON taom ro'yxati
total_price - Jami narx
promo_code - Ishlatilgan promo kod
discount_amount - Chegirma miqdori
method - Yetkazish usuli (delivery/takeaway)
location - Joylashuv/manzil
status - Holatı (pending/preparing/delivering/completed)
created_at - Yaratilgan vaqti
```

#### 3. **products**
```sql
id (PRIMARY KEY)
category_id (FOREIGN KEY)
name - Taom nomi
price - Narx
image - Rasm URL
is_available - Mavjudligi (1/0)
```

#### 4. **categories**
```sql
id (PRIMARY KEY)
name_uz - Kategoriya nomi o'zbekchada
name_ru - Ruscha
name_en - Inglizcha
```

#### 5. **promo_codes**
```sql
id (PRIMARY KEY)
code - Promo kod (UNIQUE)
discount_percent - Chegirma foizi
is_active - Faol (1/0)
expiry_date - Tugash sanasi
```

#### 6. **admins**
```sql
user_id (PRIMARY KEY)
role - Admin turi (super_admin/admin)
permissions - Ruxsatnomalar (JSON)
is_active - Faol (1/0)
added_at - Qo'shilgan vaqti
```

#### 7. **cart**
```sql
user_id (PRIMARY KEY)
items - JSON savatdagi taomlar
updated_at - Yangilangan vaqti
```

---

## 👥 Foydalanuvchi Buyurtma Jarayoni

### FSM (Finite State Machine) Holatlari
```
OrderState:
├── phone       → Telefon raqami
├── method      → Yetkazish usuli
├── location    → Joyashuv (agar kuryer)
├── promo       → Promo kod (ixtiyoriy)
└── confirm     → Tasdiqlash
```

### Buyurtma Qilish Algor itsmi

```
1️⃣ /start
   ↓
2️⃣ Tilni tanlang (UZ/RU/EN)
   ↓
3️⃣ Asosiy menyu → "🚀 Yummy App" (WebApp)
   ↓
4️⃣ [WebApp'da] Taomlarni tanlash + location
   ↓
5️⃣ [Bot'da] Telefon raqamini yuboring
   → OrderState.phone
   ↓
6️⃣ Yetkazish usuliga tanlang:
   ├─ 🛵 Kuryer orqali → OrderState.location so'rash
   └─ 🏃 O'zim boraman → OrderState.confirm'ga o'tish
   ↓
7️⃣ [Kuryer uchun] Manzilingizni kiriting (QOLDA MATN)
   → Faqat text input, share location button RED ETILDI
   ↓
8️⃣ Promo kod so'rashi:
   ├─ Kod kiritish → Validatsiya (inline)
   │  ├─ ✅ Haqiqiy → Muvaffaqiyat xabari + davom
   │  └─ ❌ Noto'g'ri → Xato xabari + qayta so'rash
   └─ skip/bo'sh → Chegirmasiz davom
   ↓
9️⃣ Buyurtma xulosasi ko'rish:
   📊 Taomlar
   🛒 Usul
   📍 Manzil
   💰 Jami narx
   🎟 Promo (agar bor)
   ↓
🔟 ✅ TASDIQLASH / ❌ BEKOR QILISH
   ↓
1️⃣1️⃣ ✅ Buyurtma qabul qilindi! (#ID)
   + 🏠 MAIN MENU TUGMASI
   ↓
1️⃣2️⃣ Admin'ga xabartirish (Worker)
```

### Kodni Tushuntirish

#### location_keyboard()
```python
def location_keyboard(lang='uz'):
    """Users enter location manually - no location button"""
    return ReplyKeyboardRemove()
```
**Asosiy o'zgarish:** Location share button o'chirilgan, faqat qo'lda text input qabul qiladi.

#### get_location() Handler
```python
@router.message(OrderState.location)
async def get_location(message: types.Message, state: FSMContext):
    # Location share qabul qilmaydi
    if message.location:
        await message.answer(s['location_req'], reply_markup=kb.location_keyboard(lang))
        return
    
    # Faqat text input qabul qiladi
    location_str = message.text
    await state.update_data(location=location_str, maps_url=message.text)
    await ask_for_promo(message, state)  # Promo so'rashi
```

#### ask_for_promo() - Yangi Funksiya
```python
async def ask_for_promo(message: types.Message, state: FSMContext):
    """Promo kod so'rashi - agar WebApp'dan bo'lsa, validatsiya qiladi"""
    data = await state.get_data()
    promo_code = data.get('promo_code_from_app')
    
    if promo_code:
        # WebApp'dan kelgan kod - validate qil
        promo = db.get_promo_code(promo_code.upper())
        if promo:
            await state.update_data(
                promo_code=promo_code.upper(), 
                discount_percent=promo[2]
            )
        await show_order_summary(message, state)
    else:
        # Foydalanuvchidan so'rash
        await state.set_state(OrderState.promo)
        await message.answer(s['promo_req'], reply_markup=types.ReplyKeyboardRemove())
```

#### get_promo() - Inline Validatsiya
```python
@router.message(OrderState.promo)
async def get_promo(message: types.Message, state: FSMContext):
    """Promo kod validatsiyasi"""
    promo_input = message.text.strip().upper()
    
    # Skip bo'lsa, chegirmasiz davom
    if promo_input in ['SKIP', 'BEKOR', 'БЕЗ', '']:
        await state.update_data(promo_code=None, discount_percent=0)
        await show_order_summary(message, state)
        return
    
    # Promo tekshirish
    promo = db.get_promo_code(promo_input)
    if promo and promo[3] == 1:  # Active promo
        await state.update_data(
            promo_code=promo_input, 
            discount_percent=promo[2]
        )
        await message.answer(s['promo_applied'].format(percent=promo[2]))
        await show_order_summary(message, state)
    else:
        # Noto'g'ri - xato xabari va qayta so'rash
        await message.answer(s['promo_invalid'])
        # Handler yana ishlaydi, user qayta text yuborishi mumkin
```

#### process_confirm() - Main Menu Tugmasi
```python
@router.message(OrderState.confirm)
async def process_confirm(message: types.Message, state: FSMContext):
    if message.text == s['confirm_btn']:
        # Buyurtmani yaratish
        order_id = db.create_order(...)
        
        # ✅ Main Menu bilan qaytish (o'zgarish!)
        await message.answer(
            s['order_received'].format(id=order_id),
            reply_markup=kb.main_menu(lang, is_admin)
        )
        
        # Admin'ga xabartirish
        await notify_admin(...)
```

---

## 👨‍💼 Admin Paneli

### Admin Turlar

#### 1. **Super Admin** (Barcha ruxsatnomalar)
- ✅ Buyurtmalarni boshqarish
- ✅ Menyu boshqarish (taom qo'shish/o'chirish)
- ✅ Promo kodlar
- ✅ Mailing (massiv xabar)
- ✅ Statistika
- ✅ Adminlari boshqarish

#### 2. **Admin/Worker** (Cheklangan ruxsatnomalar)
- ✅ Buyurtmalarni boshqarish
- ✅ Buyurtma holatini yangilash

### Admin Komandalar

```
/admin - Admin panelini ochish
/stats - Statistika ko'rish
/promo - Promo kodlar boshqarish
/mailing - Foydalanuvchilarga xabar yuborish
/menu - Menyu tahrirlash
```

---

## 🎟️ Promo Kodlar

### Promo Kod Tizimi

**Xususiyatlari:**
- Foydalanuvchi promo kodi kiritse → **inline validatsiya**
- Noto'g'ri kod → xato xabari + qayta so'rash
- To'g'ri kod → muvaffaqiyat xabari + davom
- Promo faqat bir marta so'ralinadi (order summary'da qayta so'ranmaydi)
- Promo kod tingdan keyin avtomatik qo'llaniladi

### Promo Kod Ma'lumotlari

```
code          - Kod (UNIQUE) - "SAVE50"
discount_percent - Chegirma foizi - 50
is_active     - Faol - 1 (true)
expiry_date   - Tugash sanasi - "2025-12-31"
```

### Foydalanish Misoli

```
User: "SAVE50"
Bot: "✅ Promo kod qabul qilindi! 50% chegirma berildi."
Discount: (subtotal) * 0.50 = final_price
```

---

## 🌐 Tillar Qo'llabi

### Qo'llangan Tillar
- 🇺🇿 **O'zbekcha** (uz)
- 🇷🇺 **Ruscha** (ru)
- 🇺🇸 **Inglizcha** (en)

### Tarjimalar Saqlash

Barcha tarjimalar `translations.py` faylida:

```python
STRINGS = {
    'uz': {
        'welcome': "Xush kelibsiz...",
        'phone_req': "Telefon raqamingizni yuboring:",
        'location_req': "Iltimos, manzilingizni yozma ravishda kiriting:",
        'promo_req': "📝 Agar promo kodingiz bo'lsa, uni kiriting...",
        'promo_applied': "✅ Promo kod qabul qilindi! {percent}% chegirma...",
        'promo_invalid': "❌ Promo kod noto'g'ri yoki tugagan...",
        # ... boshqa tarjimalar
    },
    'ru': { ... },
    'en': { ... }
}
```

### Tilni O'zgartirish

```python
# /start buyurtmasining javobida
@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery):
    lang = callback.data.split("_")[1]  # uz, ru, yoki en
    db.set_user_lang(callback.from_user.id, lang)
```

---

## 🔌 API Integratsiyasi

### WebApp Integratsiyasi

**WebApp URL:**
```
https://khamidovkhusnidd1n.github.io/Yummy/?lang={lang}&v=20260128_1034
```

**WebApp'dan kelgan ma'lumotlar:**

```python
@router.message(F.content_type == types.ContentType.WEB_APP_DATA)
async def web_app_data_handler(message: types.Message, state: FSMContext):
    data = json.loads(message.web_app_data.data)
    
    # data strukturi:
    {
        "type": "order",
        "items": [
            {"name": "Burger", "price": 25000, "quantity": 2},
            {"name": "Coca-Cola", "price": 5000, "quantity": 1}
        ],
        "location": {
            "lat": 41.2995,
            "lon": 69.2401,
            "address": "Yangiyo'l"
        },
        "promo_code": "SAVE50"  # Ixtiyoriy
    }
```

### Webhook Mode (Production)

```python
# RENDER_EXTERNAL_URL o'rnatilgan bo'lsa
WEBHOOK_URL = f"{WEBHOOK_HOST}/webhook/{BOT_TOKEN}"

# Bot webhook'ga o'tadi
await bot.set_webhook(WEBHOOK_URL)
```

### Polling Mode (Local)

```python
# RENDER_EXTERNAL_URL bo'lmasa
await dp.start_polling(bot)
```

---

## 📁 Fayllar Strukturi

```
for yummy - Copy (2)/
├── main.py                          # Bot entry point
├── config.py                        # Config va environment
├── database.py                      # SQLite DB class
├── translations.py                  # Tillar
├── menu_data.js                     # Menu JSON
├── index.html                       # WebApp UI
├── Dockerfile                       # Docker image
├── Procfile                         # Heroku deploy
├── requirements.txt                 # Python dependencies
│
├── handlers/
│   ├── user_handlers.py             # Foydalanuvchi routes
│   └── admin_handlers.py            # Admin routes
│
├── keyboards/
│   ├── user_keyboards.py            # Foydalanuvchi tugmalari
│   └── admin_keyboards.py           # Admin tugmalari
│
├── images/                          # Taom rasmlari
├── utils/
│   └── publisher.py                 # Publisher utils
│
└── SYSTEM_DOCUMENTATION.md          # Bu fayl!
```

---

## 🚀 O'rnatish va Ishga Tushirish

### 1. Muhim Paketlar

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
aiogram==3.x
aiohttp
python-dotenv
sqlite3
openpyxl
```

### 2. Environment Variables (.env)

```env
BOT_TOKEN=7612345678:ABCDEFGHIJKLMNOPQRSTUVWXYZabc...
SUPER_ADMINS=123456789,987654321
WORKERS=111111111,222222222
RENDER_EXTERNAL_URL=https://yummy-bot.onrender.com
PORT=8080
```

### 3. Local Ishga Tushirish

```bash
python main.py
# Polling mode ishga tushadı
```

### 4. Production'da (Render/Heroku)

**Procfile:**
```
web: python main.py
```

**Deploy:**
```bash
git push heroku main
```

---

## 🔑 Muhim Xususiyatlar

### ✅ Taqdim Etilgan O'zgarishlar

| Xususiyat | Oldiy | Yangi | Status |
|-----------|-------|-------|--------|
| Location Button | Share button | Only manual text | ✅ O'chirildi |
| Promo Entry Point | Skip button va prompt | Promo.State | ✅ Inline validatsiya |
| Promo Validation | WebApp'da | Telegram'da inline | ✅ Barokahor |
| Order Summary | Promo qayta so'ranadi | Qayta so'ranmaydi | ✅ Tayyor |
| Order Confirmation | Plain message | Main Menu button | ✅ Qulayroq |

### 🎯 Asosiy Qo'llanma

```
🛍️ Buyurtma Qilish:
   1. /start → Tilni tanlang
   2. 🚀 Yummy App → WebApp'da taomlarni tanlash
   3. 📞 Telefon (button orqali)
   4. 🛒 Usul (Kuryer/O'zim)
   5. 📍 Joyashuv (MATN) - agar kuryer
   6. 🎟️ Promo kod (ixtiyoriy) - inline validatsiya
   7. ✅ Tasdiqlash
   8. 📲 Main Menu tugmasi - yana buyurtma qilish uchun

💼 Admin Paneli:
   1. /start → 🛠 Admin Panel
   2. Buyurtmalarni boshqarish
   3. Holatni yangilash
   4. Statistika ko'rish
```

---

## 📞 Muhim Kontaktlar

- **Asosiy Manzil:** Yangiyo'l, Toshkent
- **Telefon:** +998900666506
- **Admin:** @khusniddinkhamidov

---

## 📊 Statistika va Hisobotlar

### Kunlik Hisobot

Haftasiga har kuni soat 00:00'da super admin'ga Excel fayl yuboriladi:
- Kunni buyurtmalari soni
- Jami daromad
- Taomlar sotuvi

```python
# daily_report_scheduler() - main.py'da
# Avtomatik ishga tushadı deployment vaqtida
```

---

## 🐛 Debugging va Problem Solving

### Umumiy Muammolar

| Muammo | Sabab | Yechimi |
|--------|-------|--------|
| Bot javob bermaydi | BOT_TOKEN noto'g'ri | .env'da BOT_TOKEN tekshirish |
| WebApp ma'lumoti kelmasdi | URL noto'g'ri | keyboards/user_keyboards.py dagi URL |
| Promo kod qo'llanilmaydi | Kod noto'g'ri yoki o'chirilgan | Promo kod faol ekanligini tekshirish |
| Location error | Share button bosish | Text input kiritish (button qayta tanlash) |
| Admin xabari kelmasdi | Admin ID noto'g'ri | config.py dagi SUPER_ADMINS/WORKERS |

### Log Tekshirish

```bash
# Render/Heroku
heroku logs --tail

# Local
# main.py console outputida
```

---

## 📝 Litsenziya va Huquqlar

**Yangi o'zgarishlar (2025-01-28):**
- ✅ Location button o'chirildi - faqat qo'lda text kiritish
- ✅ Promo kodlar inline validatsiyasi
- ✅ Main Menu tugmasi order confirmation'da
- ✅ Promo kod qayta so'ranmaydi

---

**Hujjat Yaratilgan:** 28-Yanvar 2025
**Oxirgi Yangilash:** 28-Yanvar 2025 (v2.0)
**Versiya:** 2.0
**Status:** ✅ Aktiv

---

