# Hydroponic Onboard Backend

Backend ini adalah contoh kecil dari alur API smart hydroponic. Fokusnya bukan membuat fitur sebanyak mungkin, tetapi memahami urutan kerja software backend dari konfigurasi sampai endpoint.

## Why We Use This

- FastAPI dipakai karena struktur route dan dokumentasi API otomatisnya mudah dipahami.
- Pydantic dipakai untuk validasi request dan response.
- SQLAlchemy dipakai agar kita bisa menulis query database dengan model Python.
- Alembic dipakai untuk mencatat perubahan struktur database.
- pytest dipakai supaya perilaku endpoint bisa dicek otomatis.
- uv dipakai agar dependency Python rapi dan perintahnya konsisten.

## Alur Backend

Urutan yang kamu ingat sudah benar. Versi yang sedikit dirapikan:

1. `config/config.py`: membaca environment variable dari `.env`.
2. `config/db.py`: membuat engine, `Session`, dan `Base` SQLAlchemy.
3. `utils/deps.py`: menyediakan dependency `get_session` untuk route FastAPI.
4. `models`: mendefinisikan bentuk tabel database.
5. `migrations`: menyimpan histori perubahan tabel dari Alembic.
6. `schemas`: mendefinisikan bentuk data request dan response.
7. `services`: menyimpan logika akses data.
8. `routes`: mendefinisikan endpoint HTTP.
9. `main.py`: membuat aplikasi FastAPI dan memasang route.

## Endpoint Demo

### `GET /hydroponics`

Mengambil daftar data hidroponik yang tersimpan.

### `POST /hydroponics`

Menambahkan data hidroponik baru.

Contoh request:

```json
{
  "moisture": 80,
  "temperature": 27.1,
  "humidity": 67.5,
  "ph": 6.1,
  "ec": 1.45
}
```

## Cara Menjalankan

1. Masuk ke folder backend.
2. Copy `.env.example` menjadi `.env`, lalu isi konfigurasi PostgreSQL.
3. Install dependency dengan `uv sync`.
4. Jalankan migrasi database dengan `uv run alembic upgrade head`.
5. Jalankan server dengan `uv run uvicorn main:app --reload`.
6. Buka dokumentasi API di `http://127.0.0.1:8000/docs`.

## Cara Test

```bash
uv run pytest
```

Test route memakai dependency override, jadi pytest tidak wajib terhubung ke database asli. Ini sengaja dibuat begitu agar anggota baru bisa belajar testing endpoint dulu sebelum masuk ke integration test database.

## Catatan Untuk Belajar

- `schemas` berbeda dari `models`: schema untuk data API, model untuk tabel database.
- `routes` sebaiknya tipis dan mudah dibaca.
- `services` menjadi tempat logika yang nanti bisa berkembang.
- Alembic dipakai saat struktur tabel berubah, bukan setiap kali menambah data.
