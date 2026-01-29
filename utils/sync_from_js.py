import re
import json
import sqlite3
import os

def import_menu_from_js():
    # Detect the current directory to find menu_data.js correctly
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'menu_data.js')
    
    if not os.path.exists(file_path):
        # Try current directory as fallback
        file_path = 'menu_data.js'
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Menu data file not found at {file_path}")

    print(f"Reading from: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Improved regex: catch everything inside the first { and last } before semicolon
    menu_match = re.search(r'window\.DYNAMIC_MENU_DATA\s*=\s*(\{.*?\});', content, re.DOTALL)
    cats_match = re.search(r'window\.DYNAMIC_CATS\s*=\s*(\{.*?\});', content, re.DOTALL)
    
    if not menu_match:
        raise ValueError("Could not find DYNAMIC_MENU_DATA in JS file")
    
    # Process Menu
    menu_str = menu_match.group(1)
    # Basic JSON fixes if needed
    try:
        menu_data = json.loads(menu_str)
    except:
        # Try cleaning trailing commas which JS allows but JSON doesn't
        menu_str_clean = re.sub(r',\s*([}\]])', r'\1', menu_str)
        menu_data = json.loads(menu_str_clean)

    # Process Cats
    if cats_match:
        cats_str = cats_match.group(1)
        try:
            cats_data = json.loads(cats_str)
        except:
            cats_data = json.loads(re.sub(r',\s*([}\]])', r'\1', cats_str))
    else:
        cats_data = {'uz': {}, 'ru': {}, 'en': {}}

    db_path = os.path.join(base_dir, 'yummy_bot.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    try:
        # Clear existing
        cur.execute("DELETE FROM products")
        cur.execute("DELETE FROM categories")
        cur.execute("DELETE FROM sqlite_sequence WHERE name='products' OR name='categories'")
        
        for cat_name, items in menu_data.items():
            u = cats_data.get('uz', {}).get(cat_name, cat_name)
            r = cats_data.get('ru', {}).get(cat_name, cat_name)
            e = cats_data.get('en', {}).get(cat_name, cat_name)
            
            cur.execute("INSERT INTO categories (name_uz, name_ru, name_en) VALUES (?, ?, ?)", (u, r, e))
            cat_id = cur.lastrowid
            
            for item in items:
                cur.execute("INSERT INTO products (category_id, name, price, image) VALUES (?, ?, ?, ?)",
                            (cat_id, item.get('n', 'Noma\'lum'), item.get('p', 0), item.get('i', '')))
        
        conn.commit()
        print(f"Import success: {len(menu_data)} categories imported.")
    finally:
        conn.close()

if __name__ == "__main__":
    import_menu_from_js()
