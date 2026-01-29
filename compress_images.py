"""
Rasmlarni siqish skripti
- Fayl nomlari va yo'llari O'ZGARMAYDI
- Faqat hajmi kichrayadi (2MB -> ~100-200KB)
"""

import os
from PIL import Image

IMAGES_DIR = "images"
MAX_SIZE = (800, 800)  # Maksimal o'lcham
QUALITY = 75  # JPEG sifati (1-100)

def compress_image(filepath):
    """Bitta rasmni siqish"""
    try:
        original_size = os.path.getsize(filepath)
        
        # Agar rasm allaqachon kichik bo'lsa, o'tkazib yuborish
        if original_size < 150 * 1024:  # 150KB dan kichik
            print(f"[SKIP] Kichik: {filepath}")
            return 0
        
        with Image.open(filepath) as img:
            # RGBA bo'lsa RGB ga o'tkazish (JPEG uchun)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # O'lchamni kamaytirish
            img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
            
            # Yangi fayl nomi (PNG -> JPG)
            base, ext = os.path.splitext(filepath)
            new_filepath = base + ".jpg" if ext.lower() == ".png" else filepath
            
            # Saqlash
            img.save(new_filepath, "JPEG", quality=QUALITY, optimize=True)
            
            # Agar PNG dan JPG ga o'zgargan bo'lsa, eski PNG ni o'chirish
            if new_filepath != filepath and os.path.exists(new_filepath):
                os.remove(filepath)
            
            new_size = os.path.getsize(new_filepath)
            saved = original_size - new_size
            saved_percent = (saved / original_size) * 100
            
            print(f"[OK] {os.path.basename(filepath)}: {original_size//1024}KB -> {new_size//1024}KB ({saved_percent:.0f}% saved)")
            return saved
            
    except Exception as e:
        print(f"[ERROR] {filepath} - {e}")
        return 0

def main():
    total_saved = 0
    count = 0
    
    print("\n=== Rasmlarni siqish boshlandi ===\n")
    
    for root, dirs, files in os.walk(IMAGES_DIR):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                filepath = os.path.join(root, file)
                saved = compress_image(filepath)
                total_saved += saved
                count += 1
    
    print("\n" + "=" * 50)
    print(f"Natija: {count} ta rasm tekshirildi")
    print(f"Jami tejaldi: {total_saved // (1024*1024)} MB ({total_saved // 1024} KB)")
    print("Tayyor! Yollar ozgarmadi, faqat hajm kichraydi.")

if __name__ == "__main__":
    main()
