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

1. Baca `backend/Tasks.md`.
2. Jalankan test level 1 terlebih dahulu.
3. Baca pesan error dari test.
4. Buat folder atau file yang diminta oleh task.
5. Jalankan test lagi sampai berhasil.
6. Lanjut ke level berikutnya.

Beberapa folder backend seperti `routes`, `schemas`, dan `services` sengaja belum disediakan. Tujuannya agar kalian membuat struktur itu saat benar-benar membutuhkannya.

Jalankan backend:

```bash
cd backend
uv sync
uv run uvicorn main:app --reload
```

Jalankan test backend:

```bash
cd backend
uv run pytest
```

### Frontend

Urutan belajar yang disarankan:

1. Baca `frontend/Tasks.md`.
2. Buat folder sesuai nama kalian, misalnya `frontend/aniqah` atau `frontend/syahla`.
3. Kerjakan level 1 sampai level 4 secara berurutan.
4. Jalankan test sesuai level yang sedang dikerjakan.
5. Gunakan error dari test sebagai petunjuk bagian mana yang perlu diperbaiki.

Jalankan frontend:

```bash
cd frontend
npm install
npm run dev
```

Jalankan test frontend:

```bash
cd frontend
npx playwright test tests/level-1-structure.spec.js --grep <nama_kalian>
```

Ganti nama test sesuai level yang sedang kalian kerjakan.

## Alur Git Untuk Pemula

Setiap mengerjakan task, buat branch baru agar perubahan kalian tidak langsung bercampur dengan branch utama.

1. Pastikan berada di branch utama dan ambil update terbaru:

```bash
git switch main
git pull
```

2. Buat branch baru dengan nama yang jelas:

```bash
git switch -c feat/nama-level-yang-dikerjakan
```

Contoh:

```bash
git switch -c feat/aniqah-frontend-level-1
git switch -c feat/syahla-backend-level-2
```

3. Kerjakan task dan jalankan test.

4. Cek file yang berubah:

```bash
git status
```

5. Masukkan file yang ingin dicommit:

```bash
git add <nama-file>
```

Jika yakin semua perubahan memang mau dicommit:

```bash
git add .
```

6. Commit dengan format Conventional Commit:

```bash
git commit -m "type(scope): pesan singkat"
```

Format yang dipakai:

```txt
type(scope): pesan singkat
```

Jenis `type` yang umum dipakai:

- `feat`: menambah fitur atau task baru.
- `fix`: memperbaiki bug.
- `test`: menambah atau memperbaiki test.
- `docs`: mengubah dokumentasi.
- `refactor`: merapikan kode tanpa mengubah perilaku.
- `chore`: perubahan pendukung seperti konfigurasi.

Contoh commit message:

```bash
git commit -m "feat(frontend): add dashboard structure"
git commit -m "feat(backend): add sensor schema"
git commit -m "test(frontend): add realtime sensor check"
git commit -m "docs: add backend learning guide"
```

7. Push branch kalian:

```bash
git push -u origin <nama-branch>
```

8. Buka Pull Request di GitHub, lalu minta review.

Tips kecil:

- Commit sebaiknya kecil dan fokus pada satu level atau satu perbaikan.
- Jangan commit file `.env` karena berisi konfigurasi lokal.
- Jika ragu, jalankan `git status` dulu sebelum `git add`.
- Jika test masih gagal, tulis di Pull Request bagian mana yang masih membingungkan.

## Why We Use This

Kita memakai stack ini karena cukup dekat dengan repo smart-hydroponic, tetapi masih ramah untuk latihan:

- FastAPI memberi dokumentasi API otomatis lewat `/docs` dan `/openapi.json`.
- SQLAlchemy dan Alembic mengenalkan pola database yang umum dipakai di proyek nyata.
- pytest membiasakan anggota mengecek fitur dengan test otomatis.
- Vue, TypeScript, dan Vite memberi frontend yang cepat dibuat, tetapi tetap punya struktur profesional.
- CSS murni membantu anggota baru memahami dasar layout dan styling sebelum memakai framework CSS.
