"""
Hardcoded category and product initializer.
This script directly inserts default menu data into the database,
bypassing the need to parse menu_data.js.
"""
import sqlite3
import os

MENU_DATA = {
    "🔥 Specials": [
        {"n": "Kfc BURGER (+0.25 Cola)", "p": 33000, "i": "images/image2/kfc_burger.png"},
        {"n": "Kfc HAGGI (+0.25 Cola)", "p": 38000, "i": "images/image2/kfc_haggi_cola.png"}
    ],
    "🍔 MAZZA": [
        {"n": "MAZZA (Kichik)", "p": 15000, "i": "images/mazza.png"},
        {"n": "MAZZA (Katta)", "p": 30000, "i": "images/mazza.png"}
    ],
    "🌯 Lavash": [
        {"n": "Standart", "p": 30000, "i": "images/lavash.png"},
        {"n": "Pishloqli", "p": 35000, "i": "images/image2/images3/lavash_cheese.png"},
        {"n": "Big", "p": 40000, "i": "images/image2/images3/lavash_big.png"},
        {"n": "Big pishloq", "p": 45000, "i": "images/image2/images3/lavash_cheese.png"}
    ],
    "🍔 Burger": [
        {"n": "Gamburger", "p": 28000, "i": "images/burger.png"},
        {"n": "Chizburger", "p": 33000, "i": "images/image2/images3/cheeseburger.png"},
        {"n": "Double", "p": 35000, "i": "images/image2/images3/double_burger.png"},
        {"n": "Double chiz", "p": 40000, "i": "images/image2/images3/double_cheese.png"}
    ],
    "🥙 Doner": [
        {"n": "Standart Doner", "p": 25000, "i": "images/image2/donar.png"},
        {"n": "Katta Doner", "p": 30000, "i": "images/image2/images3/donerbig.png"},
        {"n": "Pishloqli Doner", "p": 35000, "i": "images/image2/images3/donercheese.png"}
    ],
    "🍗 KFC": [
        {"n": "File strips", "p": 90000, "i": "images/image2/images3/Fillet_strips.png"},
        {"n": "Qanot", "p": 85000, "i": "images/image2/images3/wings.png"},
        {"n": "Lunch box", "p": 30000, "i": "images/image2/images3/lunch_box.png"},
        {"n": "Kfc xaggi", "p": 30000, "i": "images/image2/images3/KFC_xaggi.png"}
    ],
    "🌭 Xot-dog": [
        {"n": "Mini", "p": 10000, "i": "images/image2/images3/hot_dog.png"},
        {"n": "Twins", "p": 17000, "i": "images/image2/images3/twins.png"},
        {"n": "Big (45sm)", "p": 22000, "i": "images/image2/images3/hotdogbig.png"},
        {"n": "Super (45sm)", "p": 25000, "i": "images/image2/hot_dog.png"},
        {"n": "Canada (45sm)", "p": 25000, "i": "images/hotdog_canada.png"}
    ],
    "🥪 Xaggi": [
        {"n": "Standart", "p": 35000, "i": "images/image2/xaggi.png"},
        {"n": "Big", "p": 45000, "i": "images/image2/images3/xaggi_big.png"},
        {"n": "Xot let", "p": 28000, "i": "images/image2/xaggi.png"}
    ],
    "🍗 Naggets": [
        {"n": "Naggets", "p": 22000, "i": "images/naggets.png"},
        {"n": "Naggets mini", "p": 11000, "i": "images/naggets.png"}
    ],
    "🧀 Pishloqli yostiqchalar": [
        {"n": "Yostiqchalar", "p": 28000, "i": "images/pishloqli.png"},
        {"n": "Yostiqchalar mini", "p": 14000, "i": "images/pishloqli.png"}
    ],
    "🥪 Klab sandwich": [
        {"n": "Standart", "p": 35000, "i": "images/sandwich.png"}
    ],
    "🍟 Fri": [
        {"n": "Standart", "p": 15000, "i": "images/fri.png"},
        {"n": "Big", "p": 17000, "i": "images/image2/images3/fribig.png"}
    ],
    "🥟 Somsa": [
        {"n": "Go'shtli", "p": 10000, "i": "images/somsa.png"},
        {"n": "Pishloqli tovuq", "p": 7000, "i": "images/image2/images3/chickensomsa.png"},
        {"n": "Ko'k", "p": 5000, "i": "images/image2/images3/koksomsa.png"},
        {"n": "Kartoshka", "p": 5000, "i": "images/image2/images3/kartoshkasomsa.png"}
    ],
    "☕️ Ichimliklar": [
        {"n": "Choy", "p": 3000, "i": "images/image2/tea.png"},
        {"n": "Kofe", "p": 5000, "i": "images/image2/coffee.png"},
        {"n": "Kofe (Big)", "p": 7000, "i": "images/image2/coffee.png"},
        {"n": "Choy mevali", "p": 10000, "i": "images/image2/tea_via_fruits.png"}
    ],
    "🍹 Cocktails": [
        {"n": "Tropic", "p": 15000, "i": "images/image2/tropic.png"},
        {"n": "Moxito", "p": 15000, "i": "images/image2/moxito.png"},
        {"n": "O'rmon mevalari", "p": 15000, "i": "images/image2/forest_fruits.png"}
    ],
    "🥫 Souslar": [
        {"n": "Sous", "p": 4000, "i": "images/image2/sous.png"}
    ]
}

def init_menu():
    db_path = "yummy_bot.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Clear existing
    cur.execute("DELETE FROM products")
    cur.execute("DELETE FROM categories")
    try:
        cur.execute("DELETE FROM sqlite_sequence WHERE name='products' OR name='categories'")
    except:
        pass
    
    for cat_name, items in MENU_DATA.items():
        cur.execute("INSERT INTO categories (name_uz, name_ru, name_en) VALUES (?, ?, ?)", 
                    (cat_name, cat_name, cat_name))
        cat_id = cur.lastrowid
        
        for item in items:
            cur.execute("INSERT INTO products (category_id, name, price, image) VALUES (?, ?, ?, ?)",
                        (cat_id, item['n'], item['p'], item['i']))
    
    conn.commit()
    conn.close()
    print(f"✅ Menu initialized: {len(MENU_DATA)} categories added.")

if __name__ == "__main__":
    init_menu()
