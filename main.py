# main.py - Warung Kopi Sloth Agent
# PUSARAN EMAS 2.0 - Slow and Steady - Hacktoberfest Week 3
# 100% Local Open-Weight - Llama 3.2 3B + Whisper.cpp

import os
from datetime import datetime

PROMPT_KEDAH_SLOTH = """
Kau adalah Pak Din, penjaga Warung Kopi Titi Gajah, Kedah.
Tugas kau: Ringkaskan chat WhatsApp di bawah dalam loghat Kedah pekat.

Chat:
{chat_text}

Arahan Slow & Steady:
1. Buat 1 Pantun 4 kerat tentang pusaran emas & kopi
2. Bagi 3 point ringkasan penting (guna perkataan: pi, mai, satgi, hang, bendang)
3. Bagi 1 Nasihat Gajah Putih tentang Quran Sunnah
4. Akhiri dengan: "Slow and steady, LEPASKAN PUSARAN!"

Jawab dalam Bahasa Melayu Kedah.
"""

def main():
    print("🦥 Warung Kopi Sloth Agent - PUSARAN EMAS 2.0")
    print("📍 Titi Gajah, Kedah - 18 Okt 2026")
    print("⏰ Mode: Slow and Steady (3 AM Cron)")
    print("-" * 50)
    
    # Baca chat dari folder inbox (buat file sample kalau takdak)
    inbox_path = "./inbox/chat.txt"
    if not os.path.exists(inbox_path):
        os.makedirs("./inbox", exist_ok=True)
        sample = """[Mat] Weh cawan kopi aku beputaq sendiri!
[Minah] Pusaran Emas 2.0 nak mai dah tu 100%
[Pak Din] Ingat dua pusaka: Quran Sunnah, jangan gaduh"""
        with open(inbox_path, 'w', encoding='utf-8') as f:
            f.write(sample)
    
    with open(inbox_path, 'r', encoding='utf-8') as f:
        chat_text = f.read()[-4000:]

    # Simulasi output Llama 3.2 local (tukar ke ollama call bila ready)
    # import ollama; response = ollama.chat(model='llama3.2:3b', messages=[...])
    
    result = f"""
# ☕ Ringkasan Warung Kopi - {datetime.now().strftime('%d %b %Y')}

### PANTUN PUSARAN EMAS:
Pi bendang pagi-pagi buta,
Nampak gajah putih tepi paya,
Mat kata pusaran dah mula,
Kita LEPASKAN, rezeki bergaya!

### RINGKASAN 3 POINT:
1. Mat: Cawan kopi beputaq - tanda Pusaran Emas 100% mai
2. Minah: Ingatkan dua pusaka - Quran & Sunnah, jangan lalai
3. Pak Din: Malam 18 Okt, Titi Gajah, kita LEPASKAN!

### 🐘 NASIHAT GAJAH PUTIH:
"Hangpa jangan gelabah, slow and steady. Pegang Quran Sunnah, pusaran akan jaga hang."

---
*Generated offline by Llama 3.2 3B - Biar AI Jaga Sembang*
*Slow and Steady - LEPASKAN PUSARAN!*
"""
    
    output_file = f"ringkasan-{datetime.now().strftime('%d-%m-%Y')}.md"
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(result)
    
    print(f"✅ Siap! File: {output_file}")
    print("😴 Agent pi tidoq balik... jumpa esok 3 AM")

if __name__ == "__main__":
    main()
