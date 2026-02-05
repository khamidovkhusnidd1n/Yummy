import sqlite3

conn = sqlite3.connect('yummy_bot.db')
cur = conn.cursor()

# Update all products to use .jpg if they were mistakenly set to .png
# but only for paths starting with images/
cur.execute("UPDATE products SET image = REPLACE(image, '.png', '.jpg') WHERE image LIKE 'images/%.png'")

conn.commit()
conn.close()
print("✅ Database image extensions fixed to .jpg")
