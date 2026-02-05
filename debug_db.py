import sqlite3
import sys

# Force UTF-8 for output
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('yummy_bot.db')
cur = conn.cursor()

print("CATEGORIES:")
cats = cur.execute("SELECT * FROM categories").fetchall()
for c in cats:
    print(c)

print("\nPRODUCTS:")
prods = cur.execute("SELECT * FROM products").fetchall()
for p in prods:
    print(p)

conn.close()
