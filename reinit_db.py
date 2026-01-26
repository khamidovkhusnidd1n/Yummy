import sqlite3

def reinit():
    conn = sqlite3.connect("yummy_bot.db")
    cursor = conn.cursor()

    # Clear old data
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM categories")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('products', 'categories')")

    # Categories
    cats = [
        ("🌯 Lavash", "🌯 Лаваш", "🌯 Lavash"),
        ("🍔 Burger", "🍔 Бургер", "🍔 Burger"),
        ("🥙 Doner", "🥙 Донер", "🥙 Doner"),
        ("🍗 KFC", "🍗 KFC", "🍗 KFC"),
        ("🌭 Xot-dog", "🌭 Хот-дог", "🌭 Hot-dog"),
        ("🥪 Xaggi", "🥪 Хагги", "🥪 Haggi"),
        ("🍗 Naggets", "🍗 Наггетсы", "🍗 Nuggets"),
        ("🧀 Pishloqli yostiqchalar", "🧀 Сырные", "🧀 Cheese pods"),
        ("🥪 Klab sandwich", "🥪 Клаб", "🥪 Club"),
        ("🍟 Fri", "🍟 Фри", "🍟 Fries"),
        ("🥟 Somsa", "🥟 Сомса", "🥟 Somsa"),
        ("☕️ Ichimliklar", "☕️ Напитки", "☕️ Drinks"),
        ("🍹 Cocktails", "🍹 Коктейли", "🍹 Cocktails"),
        ("🔥 Specials", "🔥 Акции", "🔥 Specials"),
        ("🥫 Souslar", "🥫 Соусы", "🥫 Sauces")
    ]

    for uz, ru, en in cats:
        cursor.execute("INSERT INTO categories (name_uz, name_ru, name_en) VALUES (?, ?, ?)", (uz, ru, en))
    
    conn.commit()

    # Get category IDs
    cursor.execute("SELECT id, name_uz FROM categories")
    cat_ids = {name: id for id, name in cursor.fetchall()}

    # Products
    products = [
        # Lavash
        (cat_ids["🌯 Lavash"], "Standart", 30000, "images/lavash.png"),
        (cat_ids["🌯 Lavash"], "Pishloqli", 35000, "images/lavash.png"),
        (cat_ids["🌯 Lavash"], "Big", 40000, "images/lavash.png"),
        (cat_ids["🌯 Lavash"], "Big pishloq", 45000, "images/lavash.png"),
        
        # Burger
        (cat_ids["🍔 Burger"], "Gamburger", 28000, "images/burger.png"),
        (cat_ids["🍔 Burger"], "Chizburger", 33000, "images/burger.png"),
        (cat_ids["🍔 Burger"], "Double", 35000, "images/double_burger.png"),
        (cat_ids["🍔 Burger"], "Double chiz", 40000, "images/double_burger.png"),

        # Doner
        (cat_ids["🥙 Doner"], "Standart", 25000, "images/lavash.png"),
        (cat_ids["🥙 Doner"], "Big", 30000, "images/lavash.png"),
        (cat_ids["🥙 Doner"], "Chiz", 35000, "images/lavash.png"),

        # KFC
        (cat_ids["🍗 KFC"], "File strips", 90000, "images/kfc_strips.png"),
        (cat_ids["🍗 KFC"], "Qanot", 85000, "images/kfc_wings.png"),
        (cat_ids["🍗 KFC"], "Lunch box", 30000, "images/kfc_lunch.png"),
        (cat_ids["🍗 KFC"], "Kfc xaggi", 30000, "images/sandwich.png"),

        # Xot-dog
        (cat_ids["🌭 Xot-dog"], "Mini", 10000, "images/hotdog.png"),
        (cat_ids["🌭 Xot-dog"], "Twins", 17000, "images/hotdog.png"),
        (cat_ids["🌭 Xot-dog"], "Big (45sm)", 22000, "images/hotdog.png"),
        (cat_ids["🌭 Xot-dog"], "Super (45sm)", 25000, "images/hotdog.png"),
        (cat_ids["🌭 Xot-dog"], "Canada (45sm)", 25000, "images/hotdog_canada.png"),

        # Xaggi
        (cat_ids["🥪 Xaggi"], "Standart", 35000, "images/sandwich.png"),
        (cat_ids["🥪 Xaggi"], "Big", 45000, "images/sandwich.png"),
        (cat_ids["🥪 Xaggi"], "Xot let", 28000, "images/sandwich.png"),

        # Naggets
        (cat_ids["🍗 Naggets"], "Naggets", 22000, "images/naggets.png"),
        (cat_ids["🍗 Naggets"], "Naggets mini", 11000, "images/naggets.png"),

        # Pishloqli yostiqchalar
        (cat_ids["🧀 Pishloqli yostiqchalar"], "Yostiqchalar", 28000, "images/pishloqli.png"),
        (cat_ids["🧀 Pishloqli yostiqchalar"], "Yostiqchalar mini", 14000, "images/pishloqli.png"),

        # Klab sandwich
        (cat_ids["🥪 Klab sandwich"], "Standart", 35000, "images/sandwich.png"),

        # Fri
        (cat_ids["🍟 Fri"], "Standart", 15000, "images/fri.png"),
        (cat_ids["🍟 Fri"], "Big", 17000, "images/fri.png"),

        # Somsa
        (cat_ids["🥟 Somsa"], "Go'shtli", 10000, "images/somsa.png"),
        (cat_ids["🥟 Somsa"], "Pishloqli tovuq", 7000, "images/somsa.png"),
        (cat_ids["🥟 Somsa"], "Ko'k", 5000, "images/somsa.png"),
        (cat_ids["🥟 Somsa"], "Kartoshka", 5000, "images/somsa.png"),

        # Ichimliklar
        (cat_ids["☕️ Ichimliklar"], "Choy", 3000, "images/hot_drinks.png"),
        (cat_ids["☕️ Ichimliklar"], "Kofe", 5000, "images/hot_drinks.png"),
        (cat_ids["☕️ Ichimliklar"], "Kofe (Big)", 7000, "images/hot_drinks.png"),
        (cat_ids["☕️ Ichimliklar"], "Choy mevali", 10000, "images/hot_drinks.png"),

        # Cocktails
        (cat_ids["🍹 Cocktails"], "Tropic", 15000, "images/drinks.png"),
        (cat_ids["🍹 Cocktails"], "Moxito", 15000, "images/drinks.png"),
        (cat_ids["🍹 Cocktails"], "O'rmon mevalari", 15000, "images/drinks.png"),

        # Specials
        (cat_ids["🔥 Specials"], "Kfc BURGER (+0.25 Cola)", 33000, "images/burger.png"),
        (cat_ids["🔥 Specials"], "Kfc HAGGI (+0.25 Cola)", 38000, "images/sandwich.png"),

        # Souslar
        (cat_ids["🥫 Souslar"], "Sous", 4000, "images/mazza.png")
    ]

    for cat_id, name, price, img in products:
        cursor.execute("INSERT INTO products (category_id, name, price, image) VALUES (?, ?, ?, ?)", (cat_id, name, price, img))

    conn.commit()
    conn.close()
    print("Database re-initialized with local image paths!")

if __name__ == "__main__":
    reinit()
