# LAPORAN PRAKTIKUM: SISTEM PAKAR DIAGNOSA PENYAKIT THT


* **Nama:** FARIZ RAHMAN SYAHIDA
* **NIM:** H1D024008
* **Shift KRS:** C
* **Shift Baru:** G 

---

### 1. PENJELASAN APLIKASI
Aplikasi ini adalah **Sistem Pakar (Expert System)** berbasis desktop yang berfungsi sebagai alat konsultasi kesehatan khusus bidang THT (Telinga, Hidung, Tenggorokan). Aplikasi ini mengadopsi pengetahuan dari pakar/dokter ke dalam sistem komputer untuk memberikan diagnosa awal secara otomatis.

### 2. TUJUAN DAN FUNGSI
* **Tujuan:** Memberikan kemudahan bagi pengguna dalam mengenali jenis gangguan THT tanpa harus membuka buku medis secara manual.
* **Fungsi:** Mengolah 37 jenis gejala (G1-G37) untuk mengidentifikasi 23 jenis penyakit THT seperti Tonsilitis, Sinusitis, hingga Kanker Laring dengan tingkat akurasi berdasarkan kemiripan pola gejala.

### 3. LOGIKA DAN ALGORITMA (INFERENCE ENGINE)
Aplikasi ini bekerja menggunakan metode **Forward Chaining** (Penalaran Maju) dengan pendekatan **Pattern Matching**:

1.  **Knowledge Base:** Data disimpan dalam bentuk aturan (Rules). Penyakit "A" akan terdeteksi jika user memiliki gejala "G1, G5, dan G10".
2.  **Working Memory:** Sistem mencatat setiap jawaban "YA" dari user ke dalam sebuah list (memori sementara).
3.  **Inference:** Setelah semua pertanyaan selesai, sistem melakukan "Scanning" ke seluruh database penyakit.
4.  **Skoring (Weighting):** Sistem menghitung persentase kecocokan dengan membagi jumlah gejala yang ditemukan dengan total gejala yang seharusnya ada pada penyakit tersebut.
    * *Contoh:* Jika penyakit X punya 4 gejala dan user mengalami 2, maka skor kecocokannya adalah 50%.

### 4. STRUKTUR ANTARMUKA (UI/UX)
Antarmuka dibangun menggunakan library **Tkinter** dengan konsep modern:
* **State-Driven UI:** Layar berubah secara dinamis (Halaman Sambutan -> Pertanyaan -> Hasil) tanpa membuka jendela baru (SPA - Single Page Application).
* **Progress Tracking:** Terdapat Progress Bar untuk menjaga psikologi pengguna agar tahu durasi konsultasi.
* **Visual Feedback:** Tombol memiliki warna yang tegas (Hijau/Merah) untuk meminimalisir kesalahan input.

### 5. TEKNIS PENGEMBANGAN
* **Bahasa:** Python 
* **Library Utama:** `tkinter`, `ttk` (untuk komponen UI modern).
* **Struktur Data:** Menggunakan `Dictionary` untuk database penyakit dan `List of Tuples` untuk daftar gejala agar akses data cepat dan efisien.

---
