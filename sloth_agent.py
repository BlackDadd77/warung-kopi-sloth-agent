import os, time
from datetime import datetime

# Hacktoberfest Slow & Steady - Warung Kopi Agent
# Guna Ollama Llama 3.2 local

PROMPT_KEDAH = """
Kau adalah Pak Din, penjaga Warung Kopi Titi Gajah.
Ringkaskan chat WhatsApp di bawah dalam 1 pantun Kedah + 3 point penting.
Guna loghat Kedah pekat: pi, mai, satgi, hang, cek, bendang, pusaran.
Jangan lupa sebut Quran Sunnah kalau ada gaduh.

CHAT:
{chat_text}

OUTPUT FORMAT:
PANTUN: [pantun 4 kerat]
RINGKASAN: [3 point]
NASIHAT GAJAH PUTIH: [1 ayat hikmah]
"""

def summarize_chat(chat_file):
with open(chat_file, 'r', encoding = 'utf-8') as f:
text = f.read()[-4000:] # ambik 4000 char terakhir ja, slow & steady

# Call Ollama local - 100% open-weight
# os.system(f'ollama run llama3.2:3b "{PROMPT_KEDAH.format(chat_text=text)}" > output.txt')

# Mock output untuk demo
output = f"""
PANTUN:
Pi bendang pagi-pagi buta,
Nampak gajah berendam dalam paya,
Mat gaduh Minah dok kata-kata,
Pusaran mai kita semua berjaya.

RINGKASAN 18 OKT:
1. Mat risau cawan kopi beputaq - tanda pusaran 100%
2. Minah ingatkan dua pusaka: Quran Sunnah
3. Pak Din kata LEPASKAN PUSARAN malam ni!

NASIHAT GAJAH PUTIH: Slow and steady, jangan gelabah.
"""
return output

if __name__ == "__main__":
print("🦥 Warung Kopi Sloth Agent berjaga... 3 AM")
result = summarize_chat("./inbox/chat.txt")
filename = f"ringkasan- {
    datetime.now().strftime('%d-%m-%Y')}.md"
with open(filename, 'w') as out:
out.write(result)
print(f"Siap! File: {
    filename
} - pi tidoq balik tuan ooo...")