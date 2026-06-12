# Ketentuan Backend Fase 1

Backend fase 1 dibuat dengan metode TDL (Test-Driven Learning). Artinya, kalian akan menjalankan test terlebih dahulu, melihat error yang muncul, lalu memperbaiki kode sedikit demi sedikit sampai test berhasil.

Kalian tidak perlu memahami semua folder sejak awal. Pelajari bagian yang sedang dibutuhkan oleh level yang sedang dikerjakan. Ini disebut Just In Time Learning.

Beberapa folder backend memang sengaja belum disediakan. Jika test atau task meminta folder seperti `routes`, `schemas`, atau `services`, berarti kalian perlu membuat folder itu sendiri.

Kontrak API yang dipakai pada fase ini:

```txt
/api/sensors
```

Response utama yang harus dikembalikan backend:

```json
{
  "temperature": 25,
  "humidity": 60,
  "moisture": 40
}
```

## Level 1 - Struktur Aplikasi FastAPI

Goal level ini adalah mengenal `main.py`, FastAPI app, router, dan endpoint.

Backend wajib memiliki:

1. Variable `app` di `main.py`.
2. `app` harus dibuat dari `FastAPI`.
3. Route `GET /api/sensors` harus terpasang ke aplikasi.

Folder yang perlu dilihat:

- `main.py`
- `routes/`

Clue:

- `main.py` adalah pintu masuk aplikasi backend.
- Router bisa dibuat di folder `routes` agar `main.py` tetap rapi.
- Setelah router dibuat, router masih harus dipasang ke `app`.

Jalankan perintah berikut untuk pengujian:

```bash
uv run pytest test/test_level_1_app_structure.py
```

## Level 2 - Schema Data Sensor

Goal level ini adalah mengenal validasi data menggunakan Pydantic.

Buat schema untuk data sensor dengan field:

1. `temperature`
2. `humidity`
3. `moisture`

Ketentuan validasi:

- `humidity` harus berada di rentang 0 sampai 100.
- `moisture` harus berada di rentang 0 sampai 100.
- Ketiga field utama wajib ada.

Folder yang perlu dilihat:

- `schemas/`

Clue:

- Schema dipakai untuk menjelaskan bentuk data API.
- Gunakan Pydantic agar data yang salah bisa ditolak otomatis.
- Test mencari schema bernama `SensorData` dari file `schemas/sensor.py`.

Jalankan perintah berikut untuk pengujian:

```bash
uv run pytest test/test_level_2_sensor_schema.py
```

## Level 3 - Endpoint Mengembalikan Data Sensor

Goal level ini adalah menghubungkan route dengan data yang akan dibaca frontend.

`GET /api/sensors` harus mengembalikan JSON berisi:

```json
{
  "temperature": 25,
  "humidity": 60,
  "moisture": 40
}
```

Nilainya boleh dummy dulu. Yang penting bentuk datanya benar dan bisa dibaca frontend.

Folder yang perlu dilihat:

- `routes/`
- `schemas/`
- `services/`

Clue:

- Route menerima request HTTP.
- Service menyimpan logika pengambilan data.
- Untuk level ini, data dummy lebih baik daripada langsung memakai database.
- Jangan ubah kontrak field karena frontend akan membaca `temperature`, `humidity`, dan `moisture`.

Jalankan perintah berikut untuk pengujian:

```bash
uv run pytest test/test_level_3_sensor_api.py
```

## Level 4 - Simpan Data Sensor Terbaru

Goal level ini adalah mengenal konsep storage sederhana.

Backend harus mendukung:

1. `POST /api/sensors` untuk menerima data sensor baru.
2. `GET /api/sensors` untuk mengambil data sensor terbaru.

Untuk fase ini, storage boleh dibuat sederhana dulu. Kalian boleh mulai dari penyimpanan sementara di memory sebelum belajar database.

Folder yang perlu dilihat:

- `routes/`
- `schemas/`
- `services/`

Clue:

- POST biasanya dipakai untuk mengirim data baru ke backend.
- GET dipakai untuk membaca data.
- Jika data terbaru disimpan di service, route GET bisa mengambil data dari tempat yang sama.
- Database belum wajib di level ini. Yang penting alurnya paham dulu.

Jalankan perintah berikut untuk pengujian:

```bash
uv run pytest test/test_level_4_sensor_storage.py
```

## Cara Mengerjakan

Kerjakan level secara berurutan:

```bash
uv run pytest test/test_level_1_app_structure.py
uv run pytest test/test_level_2_sensor_schema.py
uv run pytest test/test_level_3_sensor_api.py
uv run pytest test/test_level_4_sensor_storage.py
```

Jika sudah selesai semua:

```bash
uv run pytest
```

## Catatan Belajar

- Jangan langsung mengejar semua test hijau sekaligus.
- Baca pesan error perlahan, karena error biasanya memberi tahu file atau konsep yang perlu dipelajari.
- Boleh diskusi dengan AI, tetapi minta clue dan penjelasan, bukan langsung solusi penuh.
- Jika bingung folder mana yang perlu dibuka, kembali ke bagian "Folder yang perlu dilihat" pada level yang sedang dikerjakan.
