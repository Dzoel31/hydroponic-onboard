# Hydroponic Onboard

Repository ini dibuat untuk pembelajaran sistem hidroponik sebelum terjun langsung ke repo aslinya. Struktur dan isi dari repo ini akan dibuat sangat mirip dengan repo aslinya, sehingga memudahkan untuk memahami dan mengimplementasikan sistem hidroponik yang sebenarnya. Di repo ini kalian bebas eksplorasi untuk mempelajari dan meningkatkan pengetahuan serta pengalaman kalian dalam pengembangan software untuk sistem hidroponik. Jangan ragu untuk mencoba berbagai pendekatan dan solusi, karena tujuan utama dari repo ini adalah untuk belajar dan berkembang dalam bidang ini. Selamat belajar dan semoga sukses!

Anggap aja repo ini sebagai tempat latihan dan eksperimen untuk memahami konsep-konsep dasar dalam pengembangan sistem hidroponik. Kalian tidak usah takut untuk membuat kesalahan. Justru dengan membuat kesalahan, kalian akan belajar lebih banyak dan mendapatkan pengalaman yang berharga. Kalian tetap akan dipandu dengan baik melalui dokumentasi dan contoh-contoh yang ada di repo ini, sehingga kalian bisa memahami setiap langkah dengan jelas.

## Tools dan Framework yang Digunakan

Dalam repo ini, kita akan menggunakan beberapa tools dan framework yang umum digunakan dalam pengembangan sistem hidroponik. Beberapa di antaranya termasuk:

### Backend

- **Python**: Bahasa pemrograman utama yang digunakan untuk mengembangkan backend sistem hidroponik.
- **FastAPI**: Framework web yang ringan dan mudah digunakan untuk membangun API backend.
- **SQLAlchemy**: Library untuk mengelola database dengan mudah dan efisien.
- **Alembic**: Tool untuk melakukan migrasi database dengan SQLAlchemy.
- **Pydantic**: Library untuk validasi data dan pembuatan model data yang digunakan dalam FastAPI.
- **PostgreSQL**: Database yang digunakan untuk menyimpan data sistem hidroponik.
- **TimescaleDB**: Ekstensi untuk PostgreSQL yang digunakan untuk menyimpan data time-series, seperti data sensor.
- **pytest**: Framework testing untuk menulis dan menjalankan tes otomatis untuk backend.

Tools untuk dependensi dan manajemen proyek: `uv` untuk backend dan `npm` untuk frontend.

### Frontend

- **Node.js**: Platform untuk menjalankan JavaScript/TypeScript di server.
- **TypeScript**: Bahasa pemrograman yang digunakan untuk mengembangkan frontend dengan tipe data yang kuat.
- **Vue.js**: Framework JavaScript untuk membangun antarmuka pengguna yang interaktif dan responsif.
- **Vite**: Build tool yang digunakan untuk mengembangkan frontend dengan cepat dan efisien.

### DevOps

- **Docker**: Platform untuk mengembangkan, mengirim, dan menjalankan aplikasi dalam container.
- **Docker Compose**: Tool untuk mendefinisikan dan menjalankan aplikasi multi-container dengan Docker.
- **Git**: Sistem kontrol versi yang digunakan untuk mengelola kode sumber proyek ini.
- **GitHub**: Platform untuk hosting kode sumber dan kolaborasi dalam proyek ini.
- **GitHub Actions**: Tool untuk mengotomatisasi workflow pengembangan, seperti testing dan deployment.
- **CI/CD**: Praktik untuk mengotomatisasi proses integrasi dan pengiriman kode, memastikan bahwa setiap perubahan yang dilakukan diuji dan siap untuk diproduksi.
- **Testing Frameworks**: Tools seperti pytest untuk backend dan Jest untuk frontend, digunakan untuk menulis dan menjalankan tes otomatis untuk memastikan kualitas kode. (Untuk saat ini hanya backend yang menggunakan pytest).
- **Monitoring Tools**: Tools seperti Prometheus dan Grafana untuk memantau performa dan kesehatan sistem hidroponik secara real-time. (Sebenarnya sudah ada di repo smart-hydroponic, namun kondisi server FIK yang suka nyala-mati membuat monitoring jadi sulit, jadi untuk saat ini kita skip dulu).

## Alur Pengembangan

Repo ini sengaja dibuat kecil agar anggota baru bisa memahami alur dari backend ke frontend tanpa terlalu banyak distraksi.

### Backend

Urutan belajar yang disarankan:

1. Baca `.env.example`, lalu pahami environment variable yang dibutuhkan.
2. Buka `backend/config/config.py` untuk melihat cara `.env` dibaca.
3. Buka `backend/config/db.py` untuk melihat koneksi database dan session.
4. Buka `backend/utils/deps.py` untuk melihat dependency session di FastAPI.
5. Buka `backend/models` untuk melihat bentuk tabel.
6. Buka `backend/migrations` untuk melihat histori pembuatan tabel.
7. Buka `backend/schemas` untuk melihat validasi request dan response.
8. Buka `backend/services` untuk melihat logika akses data.
9. Buka `backend/routes` untuk melihat endpoint HTTP.
10. Buka `backend/main.py` untuk melihat aplikasi FastAPI dirangkai.

Jalankan backend:

```bash
cd backend
uv sync
uv run alembic upgrade head
uv run uvicorn main:app --reload
```

Jalankan test backend:

```bash
cd backend
uv run pytest
```

### Frontend

Urutan belajar yang disarankan:

1. Buka `frontend/src/main.ts` untuk melihat aplikasi Vue dipasang.
2. Buka `frontend/src/App.vue` untuk melihat state, form, dan tampilan.
3. Buka `frontend/src/types` untuk melihat tipe data TypeScript.
4. Buka `frontend/src/services` untuk melihat request ke backend.
5. Jalankan `npm run generate-api` untuk membuat client API dari OpenAPI backend.

Jalankan frontend:

```bash
cd frontend
npm install
npm run dev
```

Generate API frontend:

```bash
cd frontend
npm run generate-api
```

Pastikan backend sedang berjalan di `http://127.0.0.1:8000` sebelum generate API.

## Why We Use This

Kita memakai stack ini karena cukup dekat dengan repo smart-hydroponic, tetapi masih ramah untuk latihan:

- FastAPI memberi dokumentasi API otomatis lewat `/docs` dan `/openapi.json`.
- SQLAlchemy dan Alembic mengenalkan pola database yang umum dipakai di proyek nyata.
- pytest membiasakan anggota mengecek fitur dengan test otomatis.
- Vue, TypeScript, dan Vite memberi frontend yang cepat dibuat, tetapi tetap punya struktur profesional.
- CSS murni membantu anggota baru memahami dasar layout dan styling sebelum memakai framework CSS.
