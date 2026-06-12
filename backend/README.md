# Hydroponic Onboard Backend

Backend ini adalah contoh kecil dari alur API smart hydroponic. Fokusnya bukan membuat fitur sebanyak mungkin, tetapi memahami urutan kerja software backend dari konfigurasi sampai endpoint. Kalian bisa eksplorasi atau coba coba ubah kode pada repo ini.

## Why We Use This

- FastAPI dipakai karena struktur route dan dokumentasi API otomatisnya mudah dipahami.
- Pydantic dipakai untuk validasi request dan response.
- SQLAlchemy dipakai agar kita bisa menulis query database dengan model Python.
- Alembic dipakai untuk mencatat perubahan struktur database.
- pytest dipakai supaya perilaku endpoint bisa dicek otomatis.
- uv dipakai agar dependency Python rapi dan perintahnya konsisten.

## Alur Backend

Alur untuk pengembangan Backend dengan FastAPI dari nol bisa dijabarkan sebagai berikut:

1. `config/config.py`: membaca environment variable dari `.env`.
2. `config/db.py`: membuat engine, `Session`, dan `Base` SQLAlchemy.
3. `utils/deps.py`: menyediakan dependency `get_session` untuk route FastAPI.
4. `models`: mendefinisikan bentuk tabel database.
5. `migrations`: menyimpan histori perubahan tabel dari Alembic.
6. `schemas`: mendefinisikan bentuk data request dan response.
7. `services`: menyimpan logika akses data.
8. `routes`: mendefinisikan endpoint HTTP.
9. `main.py`: membuat aplikasi FastAPI dan memasang route.

## Belajar Dengan TDL

Panduan tugas backend ada di `Tasks.md`. Kerjakan level secara berurutan agar konsepnya muncul pelan-pelan:

1. `main.py` dan route FastAPI.
2. Schema dan validasi data.
3. Endpoint `GET /api/sensors`.
4. Storage sederhana dengan `POST /api/sensors`.

## Endpoint Demo

### `GET /api/sensors`

Mengambil data sensor terbaru.

Contoh response:

```json
{
  "temperature": 25,
  "humidity": 60,
  "moisture": 40
}
```

### `POST /api/sensors`

Menyimpan data sensor terbaru.

Contoh request:

```json
{
  "temperature": 28,
  "humidity": 63,
  "moisture": 41
}
```

## Cara Menjalankan

1. Masuk ke folder backend.
2. Copy `.env.example` menjadi `.env`.
3. Install dependency dengan `uv sync`.
4. Kerjakan task di `Tasks.md` secara berurutan.
5. Jalankan server dengan `uv run uvicorn main:app --reload` setelah `main.py` sudah membuat FastAPI app.
6. Buka dokumentasi API di `http://127.0.0.1:8000/docs`.

Catatan: migrasi database belum wajib di level awal. Pelajari migrasi saat task sudah mulai membutuhkan database.

## Konfigurasi Database Lokal

File `.env.example` sengaja tidak berisi value agar aman dicommit. Setelah copy `.env.example` menjadi `.env`, isi file `.env` lokal dengan konfigurasi latihan berikut:

```env
PGHOST=localhost
PGPORT=5432
PGDATABASE=onboard_db
PGUSER=onboard_user
PGPASSWORD=onboard123
```

### Membuat Username dan Password

Jika memakai PostgreSQL lokal di Windows, kalian bisa membuat user dan database lewat `psql` atau pgAdmin. Contoh berikut memakai `psql`.

Masuk sebagai user bawaan PostgreSQL terlebih dahulu:

```powershell
psql -U postgres
```

Lalu jalankan SQL berikut. Nilainya dibuat sama dengan `.env` agar backend bisa login ke database:

```sql
CREATE USER onboard_user WITH PASSWORD 'onboard123';
CREATE DATABASE onboard_db OWNER onboard_user;
GRANT ALL PRIVILEGES ON DATABASE onboard_db TO onboard_user;
```

Keluar dari `psql`:

```sql
\q
```

Cek apakah user dan password sudah benar dengan mencoba login memakai user baru:

```powershell
psql -h localhost -p 5432 -U onboard_user -d onboard_db
```

Saat diminta password, isi:

```txt
onboard123
```

Jika memakai TimescaleDB, masuk ke database `onboard_db`, lalu aktifkan extension:

```sql
CREATE EXTENSION IF NOT EXISTS timescaledb;
```

### TimescaleDB di Windows

Ada dua jalur yang bisa dipakai:

1. Install PostgreSQL di Windows, lalu install TimescaleDB extension mengikuti dokumentasi resmi Tiger Data.
2. Pakai Docker Desktop di Windows dan jalankan image resmi TimescaleDB. Ini biasanya lebih mudah untuk latihan karena TimescaleDB sudah ikut tersedia di container.

Rujukan resmi:

- PostgreSQL Windows installer: https://www.postgresql.org/download/windows/
- TimescaleDB self-hosted install: https://www.tigerdata.com/docs/get-started/choose-your-path/install-timescaledb
- TimescaleDB Docker quick start: https://github.com/timescale/timescaledb

Jika memakai Docker dan ingin tetap memakai nilai `.env` di atas, pastikan port container dipetakan ke `5432` dan database/user dibuat sesuai konfigurasi latihan.

Contoh perintah Docker untuk latihan lokal:

```powershell
docker run -d --name hydroponic-timescaledb `
  -p 5432:5432 `
  -e POSTGRES_USER=onboard_user `
  -e POSTGRES_PASSWORD=onboard123 `
  -e POSTGRES_DB=onboard_db `
  timescale/timescaledb-ha:pg18
```

Setelah container berjalan, cek koneksi dengan:

```powershell
psql -h localhost -p 5432 -U onboard_user -d onboard_db
```

Lalu jalankan SQL:

```sql
CREATE EXTENSION IF NOT EXISTS timescaledb;
```

Jika port `5432` sudah dipakai PostgreSQL lokal, gunakan port lain seperti `6543`, lalu sesuaikan `PGPORT` di `.env`.

## Cara Test

```bash
uv run pytest
```

## Catatan Untuk Belajar

- `schemas` berbeda dari `models`: schema untuk data API, model untuk tabel database.
- `routes` sebaiknya tipis dan mudah dibaca.
- `services` menjadi tempat logika yang nanti bisa berkembang.
- Alembic dipakai saat struktur tabel berubah, bukan setiap kali menambah data.
