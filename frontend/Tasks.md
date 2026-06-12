# Ketentuan Frontend Fase 1

Pastikan selesaikan level secara berurutan, mulai dari level 1 hingga level 4. Setiap level memiliki ketentuan yang harus dipenuhi untuk dapat dinyatakan lulus. Buat folder baru didalam folder `frontend` dengan nama kalian yaitu:

- `frontend/aniqah`
- `frontend/syahla`

## Level 1 - Struktur Dashboard

Dashboard dibuat menggunakan HTML, CSS, dan JavaScript.

Dashboard wajib memiliki:

1. Judul Dashboard
2. Card Suhu
3. Card Kelembaban
4. Card Moisture
5. Data dapat diperbarui secara real-time/simulai interval
6. Struktur id dan class sesuai ketentuan

Elemen wajib:

```html
<div id="data-suhu" class="sensor-card"></div>
<div id="data-kelembaban" class="sensor-card"></div>
<div id="data-moisture" class="sensor-card"></div>
```

Jalankan perintah berikut untuk pengujian:

```bash
npx playwright test tests/level-1-structure.spec.js --grep <nama_kalian>
```

## Level 2 - Format Data

Data yang ditampilkan pada card harus dalam format:

- Suhu: "Suhu: 25°C"
- Kelembaban: "Kelembaban: 60%"
- Moisture: "Moisture: 40%"

File yang biasanya perlu diubah:

- `index.html`
- file JavaScript di folder kalian

Clue:

- Test membaca isi teks dari `#data-suhu`, `#data-kelembaban`, dan `#data-moisture`.
- Perhatikan huruf besar, titik dua, spasi, dan satuan.
- Suhu memakai simbol `°C`, bukan hanya `C`.
- Jangan ubah `id` elemen yang sudah ditentukan pada Level 1.

Jalankan perintah berikut untuk pengujian:

```bash
npx playwright test tests/level-2-format.spec.js --grep <nama_kalian>
```

## Level 3 - Simulasi Data

Data pada card harus diperbarui berdasarkan data yang diterima dari backend. Data diambil menggunakan method fetch() ke endpoint API yang disediakan oleh backend yaitu `/api/sensors`.

Data dari backend berbentuk JSON seperti ini:

```json
{
  "temperature": 25,
  "humidity": 60,
  "moisture": 40
}
```

File yang biasanya perlu diubah:

- file JavaScript di folder kalian

Clue:

- Gunakan `fetch("/api/sensors")` untuk mengambil data.
- Setelah response diterima, ubah response menjadi JSON.
- Ambil nilai dari property `temperature`, `humidity`, dan `moisture`.
- Tampilkan data ke elemen yang sama dengan Level 2.
- Buat fungsi kecil untuk menampilkan data agar bisa dipakai lagi di Level 4.

Kesalahan umum:

- Endpoint salah, misalnya `/api/sensor` tanpa huruf `s`.
- Nama property salah, misalnya `suhu` padahal data backend memakai `temperature`.
- Lupa menunggu proses `fetch` selesai.

Jalankan perintah berikut untuk pengujian:

```bash
npx playwright test tests/level-3-dummy-data.spec.js --grep <nama_kalian>
```

## Level 4 - Real-time Data

Data pada card harus diperbarui secara real-time/simulai interval. Data diambil menggunakan method fetch() ke endpoint API yang disediakan oleh backend yaitu `/api/sensors`.

File yang biasanya perlu diubah:

- file JavaScript di folder kalian

Clue:

- Panggil fungsi pengambilan data saat halaman pertama kali dibuka.
- Setelah itu, panggil fungsi yang sama secara berkala.
- `setInterval` bisa dipakai untuk menjalankan fungsi berulang.
- Interval 1000 ms sudah cukup untuk simulasi real-time pada test.
- Jangan membuat fungsi baru yang isinya sama persis; gunakan kembali fungsi dari Level 3.

Kesalahan umum:

- Hanya mengambil data sekali, sehingga tampilan tidak berubah.
- Memakai interval terlalu lama, sehingga test menunggu tetapi data belum berubah.
- Mengubah hanya data suhu, tetapi lupa menjaga format kelembaban dan moisture.

Jalankan perintah berikut untuk pengujian:

```bash
npx playwright test tests/level-4-real-time-data.spec.js --grep <nama_kalian>
```
