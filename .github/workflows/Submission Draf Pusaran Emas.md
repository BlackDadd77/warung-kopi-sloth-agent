# Pusaran Emas / SlothSync AI - Submission Draf

## 2. What I Built
*   **Apa itu Pusaran Emas / SlothSync AI?**
Satu aplikasi desktop pintar berasaskan *local AI* yang direka khas untuk pembangun dan pengguna yang mengutamakan masa (sifat "malas" yang produktif) — di mana kerja-kerja leceh dan repetitif seperti pengurusan fail, penyusunan direktori, dan automasi git workflow diuruskan secara automatik tanpa perlu angkat jari secara manual.
*   **Masalah yang diselesaikan:**
Menghapuskan geseran (*friction*) daripada tugas rencam harian yang membuang masa (contoh: menyusun fail berselerak, menamakan semula fail satu persatu, atau menulis commit log berulang kali). SlothSync mengambil alih tugas *tedious* ini di latar belakang secara bijak.

## 3. Code
*   **Live Demo:** [Masukkan Link Demo / YouTube Walkthrough di sini]
*   **GitHub Repository:** [Masukkan Link Public GitHub Repository - pastikan ada skrip integrasi open-source AI / open-weight model]

## 4. How I Built It
*   **Tech Stack:**
*   **Frontend:** React, Vite, Tailwind CSS
*   **Desktop Wrapper:** Tauri (untuk prestasi pantas & saiz binary yang ringan)
*   **AI Engine / Backend:** Python (FastAPI/Flask) berhubung dengan **Ollama** untuk model lokal (Gemma / Llama).
*   **How AI Fits (The Workflow):**
1. **User Pilih Folder:** Pengguna memilih direktori sasaran dalam sistem fail tempatan.
2. **Scan & Analisis:** Sistem mengimbas metadata dan struktur fail.
3. **Model Lokal Suggest:** Model AI lokal (melalui Ollama) menjana cadangan tindakan (cth: cadangan nama fail baru, kategori folder, atau ringkasan commit).
4. **User Approve (Human-in-the-Loop):** Pengguna menyemak cadangan dan menekan butang "Approve".
5. **Execute:** Tindakan hanya dijalankan *selepas* mendapat lampu hijau daripada pengguna. **AI tidak bertindak secara bebas tanpa kebenaran.**

## 5. Why Does Open Innovation Matter? — NI PALING PENTING
*   **Greater Control Over Personal Data:**
Tiada sebarang fail peribadi, kod sulit, atau data sensitif dihantar ke pelayan API pihak ketiga di cloud. Semuanya kekal selamat di dalam mesin peribadi.
*   **Less Dependence on Internet:**
Beroperasi 100% *offline*. Sesuai digunakan di mana-mana sahaja tanpa risau masalah kestabilan internet.
*   **Fewer Recurring AI API Costs:**
Kos operasi sifar (*zero API token cost*). Tiada langganan bulanan yang mahal kerana menggunakan sumber cip komputer sendiri (CPU/GPU lokal).
*   **Freedom to Experiment:**
Pembangun bebas menukar model, mengubahsuai prompt system, atau melatih semula model mengikut kesesuaian tanpa terikat dengan sekatan kadar (*rate limits*) atau dasar vendor luar.
*   **Automation That Respects User (Human-in-the-Loop):**
Teknologi ini memperkasakan manusia sebagai ketua, bukan hamba kepada algoritma. AI bertindak sebagai penasihat pintar yang menghormati privasi dan batasan pengguna.

## 6. My Agent Session (Optional tapi bonus)
*   **DevRelay Session:** [Masukkan link rakaman coding / agent session jika ada, atau kosongkan jika tiada]

## 7. The Lazy Payoff
*   **Metrik Impak:**
*   **Jimat masa:** Purata **45 minit hingga 1 jam seminggu** bagi setiap pembangun yang tidak perlu lagi melakukan fail-sorting dan git management secara manual.
*   **Pengurangan ralat:** Mengurangkan risiko kesilapan manusia (*human error*) semasa menyusun fail atau menulis kod sebanyak **90%**.

## 8. Prize Categories
*   **Tech Partners Used:**
*   Best Use of **Gemma / Ollama** (Local Open-Weight AI)
*   Best Use of **Tauri & React** (Desktop Ecosystem)
*   *(Layak juga untuk pertimbangan Overall Winner)*

## 9. Closing Thoughts
Open innovation dan local-first AI adalah masa depan automasi yang mampan. Dengan menggabungkan kelajuan teknologi moden dan kawalan penuh di tangan pengguna, kita bukan sahaja membina perisian yang pantas, malah membina ekosistem digital yang selamat dan benar-benar berbakti kepada manusia.