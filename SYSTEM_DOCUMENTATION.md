# 🍔 YUMMY BOT - Tizim Hujjati (v2.1)

## 📋 Mundarija
1. [Tizim Tavsifi](#tizim-tavsifi)
2. [Arxitektura](#arxitektura)
3. [Ma'lumotlar Bazasi](#malumotlar-bazasi)
4. [Foydalanuvchi Buyurtma Jarayoni](#foydalanuvchi-buyurtma-jarayoni)
5. [Admin Paneli](#admin-paneli)
6. [Promo Kod Tizimi (Yangi)](#promo-kod-tizimi-yangi)
7. [Tillar Qo'llabi](#tillar-qollabi)
8. [Texnik Sozlamalar](#texnik-sozlamalar)
9. [Oxirgi O'zgarishlar](#oxirgi-ozgarishlar)

---

## 🎯 Tizim Tavsifi

**YUMMY BOT** — bu Telegram bot va integratsiya qilingan zamonaviy WebApp interfeysidan iborat mukammal fast-food buyurtma berish platformasi. Tizim mijozlarga premium dizayn va qulay interfeys orqali tezkor buyurtma berish imkonini beradi.

---

## 🏗️ Arxitektura

Tizim ikki qismdan iborat:

1.  **Frontend (WebApp):** HTML5, Vanilla JavaScript va CSS3 orqali yaratilgan. Premium dizayn (24px radius), shaffof elementlar va mikro-animatsiyalarga ega.
2.  **Backend (Bot):** Python (Aiogram 3.x) yordamida yozilgan. Ma'lumotlar bazasi sifatida **SQLite3** ishlatiladi.

---

## 💾 Ma'lumotlar Bazasi (SQLite)

*   `users`: Foydalanuvchilar ma'lumotlari (tel, til, id).
*   `orders`: Buyurtmalar tarixi va holatlari.
*   `promo_codes`: Chegirma beradigan kodlar bazasi.
*   `admins`: Turli darajadagi boshqaruvchilar (Super Admin, Worker).
*   `cart`: Savat ma'lumotlari.

---

## 👥 Foydalanuvchi Buyurtma Jarayoni

Hozirgi tizimda buyurtma berish flow quyidagicha barqarorlashtirilgan:

1️⃣  **Start:** Foydalanuvchi `/start` bosadi va tilni tanlaydi.
2️⃣  **WebApp:** "🚀 Yummy App" tugmasi orqali web-menu ochiladi.
3️⃣  **Tanlov:** Taomlar savatga qo'shiladi va **Promo kod** o'sha yerning o'zida (WebApp'da) tekshiriladi.
4️⃣  **Ma'lumotlar:** WebApp'dan qaytgandan so'ng bot telefon raqamini so'raydi.
5️⃣  **Usul:** "Kuryer" yoki "O'zi boraman" tanlanadi.
6️⃣  **Joylashuv (Location):** GPS tugmasi o'chirilgan. Foydalanuvchi manzilni faqat matn ko'rinishida qo'lda yozadi (bu barqarorlikni oshiradi).
7️⃣  **Yakunlash:** Bot buyurtma xulosasini ko'rsatadi. Tasdiqlangandan so'ng, tizim avtomatik "Main Menu"ga qaytadi.

---

## 👨‍💼 Admin Paneli

Adminlar uchun maxsus interfeys mavjud:
*   **Super Admin:** Barcha huquqlar (Adminga admin qo'shish, promolarni yaratish, to'liq statistika).
*   **Admin/Worker:** Buyurtmalarni boshqarish (qabul qilish, tayyorlash, yetkazib berish holatiga o'tkazish).

**Statistika:** Super adminga har kuni soat 00:00 da kunlik savdo hisoboti (Excel) bot orqali yuboriladi.

---

## 🎟️ Promo Kod Tizimi (WebApp orqali)

Bu tizimning eng katta yangilanishlaridan biridir:
*   **Mantiq:** Promo kodni bot (backend) so'ramaydi. Mijoz savat ichida kodni kiritadi.
*   **Tekshirish:** WebApp kodni darhol tekshiradi va chegirma foizini (masalan: 20%) hisoblaydi.
*   **Uzatish:** Tasdiqlangan promo-kod ma'lumotlari botga JSON formatida uzatiladi va yakuniy narxda hisobga olinadi.

---

## 🌐 Tillar Qo'llabi

Hozirda tizim 3 ta tilda mukammal ishlaydi:
*   🇺🇿 **O'zbekcha**
*   🇷🇺 **Ruscha**
*   🇺🇸 **Inglizcha**

---

## ⚠️ Joriy Kamchiliklar va Takomillashtirish Rejalari

Har qanday tizim kabi, YUMMY BOT ham o'zining rivojlanish bosqichida. Quyida joriy kamchiliklar va kelajakdagi takomillashtirishlar keltirilgan:

1.  **To'lov Tizimi (Online Payment):**
    *   *Holat:* Hozirda faqat naqd yoki terminal orqali to'lov mavjud.
    *   *Reja:* Click, Payme yoki Uzum integratsiyasini qo'shish.

2.  **Menu Ma'lumotlari Sinxronizatsiyasi:**
    *   *Holat:* Menu ma'lumotlari statik JS faylida. Admin paneldan baza yangilanganda, WebApp'ni qo'lda push qilish kerak bo'lishi mumkin.
    *   *Reja:* WebApp'ni bevosita API orqali ma'lumotlar bazasiga ulash.

3.  **Buyurtmani Jonli Kuzatish (Order Tracking):**
    *   *Holat:* Mijoz buyurtma holatini faqat bot yuborgan xabarlardan biladi.
    *   *Reja:* Kuryerni xaritada jonli ko'rish funksiyasini qo'shish.

4.  **Ombor Zahirasi (Stock Management):**
    *   *Holat:* Taom tugab qolgan bo'lsa, WebApp'da "tarkibda yo'q" (sold out) deb avtomatik chiqmaydi.
    *   *Reja:* Mahsulot qoldig'ini real vaqtda bazadan tekshirish.

5.  **Filiallar Bilan Ishlash:**
    *   *Holat:* Hozir tizim bitta asosiy nuqta uchun sozlangan.
    *   *Reja:* Ko'p filialli tizimga o'tkazish va eng yaqin filialni tanlash funksiyasini qo'shish.

6.  **Push Notificationlar:**
    *   *Holat:* Faqat Telegram ichidagi xabarlar.
    *   *Reja:* Maxsus takliflar uchun browser push-xabarnomalarini o'rnatish.

---

## ⚙️ Texnik Sozlamalar

*   **WebApp Versiyalash:** Kesh muammosini hal qilish uchun URL versiyasi: `v=20260128_1034`.
*   **Server Restart:** Har qanday `git push` dan so'ng serverda `git pull` va skriptni `restart` qilish shart.
*   **Webhook/Polling:** Tizim ham `Polling` (lokal), ham `Webhook` (Cloud/Render) rejimini qo'llab-quvvatlaydi.

---

## ✨ Oxirgi O'zgarishlar (28.01.2026)

1.  ✅ **Promo-kod so'rovi botdan olib tashlandi:** Endi bot jarayon o'rtasida promo-kod haqida xabarlar yubormaydi.
2.  ✅ **Joylashuv (GPS) tugmasi o'chirildi:** Foydalanuvchilar faqat yozma ko'rinishda manzil kiritadi.
3.  ✅ **Menyu Restart:** Buyurtma yakunlangandan so'ng bot "Asosiy menyu"ni majburiy ko'rsatadi (qotib qolmasligi uchun).
4.  ✅ **Xavfsiz Location Logikasi:** Bot ham GPS koordinatani, ham matnni birdek qabul qiladigan darajada barqarorlashtirildi.
5.  ✅ **Savat interfeysi yangilandi:** Promo-kod tekshirish funksiyasi savat ichiga joylashtirildi.

---
**Hujjat Oxirgi Yangilashi:** 28-Yanvar 2026
**Holat:** ✅ To'liq aktiv va barqaror
