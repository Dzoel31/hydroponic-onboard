# Mini Project Hydroponics

Dalam proyek mini ini, kalian akan membuat sistem hidroponik sederhana yang terdiri dari esp, backend, dan frontend. Proyek ini digunakan untuk belajar pengembangan sistem secara menyeluruh dari awal hingga deployment nanti.

## IoT dan ESP

Mikrokontroler yang digunakan adalah ESP32. Sedangkan untuk sensor dan aktuatornya berupa:

- Moisture Sensor
- DHT11 (suhu dan kelembaban)
- Relay (untuk pompa air)
- LCD (untuk menampilkan data sensor secara lokal)

## Backend

Backend akan dibangun menggunakan FastAPI dengan komponen sebagai berikut:

- Database: PostgreSQL dengan ekstensi TimescaleDB untuk data time-series.
- SQLAlchemy & Alembic: SQLAlchemy digunakan sebagai database toolkit (kita akan lebih banyak berlatih mengeksekusi raw SQL di sini), sedangkan Alembic untuk migrasi database.
- Pydantic: Untuk validasi data yang masuk dan keluar dari API.

## Frontend

Untuk pengembangan frontend difokuskan untuk pemahaman HTML, CSS, dan JavaScript dasar sebelum masuk ke framework seperti Vue.js dan TypeScript. Frontend akan menampilkan data sensor secara real-time dan memberikan kontrol untuk pompa air.

## DevOps (Fase Akhir)

Untuk deployment, kita akan menggunakan Docker untuk mengemas aplikasi backend dan frontend. Kita juga akan belajar menggunakan GitHub Actions untuk mengotomatisasi proses build dan deployment ke server.

## Metode Pembelajaran

Proyek ini akan mengadopsi TDL (Test-Driven Learning) dimana kita akan menulis tes terlebih dahulu sebelum mengembangkan fitur. Ini membantu memastikan bahwa setiap bagian kode yang kita tulis sudah teruji dan berfungsi dengan baik. Tugas kalian adalah membuat kode yang memenuhi tes yang sudah dibuat, sehingga kalian bisa belajar dengan cara yang lebih terstruktur dan efektif.

Setiap kalian mendapatkan tugas untuk mengembangkan sebuah fitur, kalian harus menguji fitur tersebut dengan tes yang sudah dibuat. Jika tes gagal, kalian harus memperbaiki kode kalian sampai tes tersebut berhasil. Tiap tasks dan test akan dijabarkan di setiap README.md pada folder `backend` dan `frontend`.

## Struktur Repository

Struktur repository yang akan menjadi final nanti adalah:

### Backend

Terdiri dari:

- `config/`: Berisi konfigurasi aplikasi, seperti pengaturan database dan environment variable.
- `models/`: Berisi definisi model database menggunakan SQLAlchemy.
- `schemas/`: Berisi definisi schema untuk validasi data menggunakan Pydantic.
- `services/`: Berisi logika bisnis untuk mengakses data dan melakukan operasi pada database.
- `routes/`: Berisi definisi endpoint HTTP untuk API.
- `main.py`: File utama untuk menjalankan aplikasi FastAPI.

### Frontend

Terdiri dari:

- `index.html`: File utama untuk halaman web.
- `styles/`: Berisi file CSS untuk styling halaman web.
- `scripts/`: Berisi file JavaScript untuk interaksi dan pengambilan data dari backend.

Lalu terdapat folder `tests/` untuk menyimpan tes otomatis yang akan kita jalankan. Folder ini tidak boleh diubah.

Goals akhir dari proyek dengan metode TDL ini adalah kalian bisa memahami alur pengembangan sistem hidroponik secara menyeluruh, mulai dari pengembangan backend, frontend, hingga deployment. Dengan metode ini, diharapkan kalian tidak terjebak pada `tutorial hell` dan bisa belajar dengan lebih efektif dikarenakan kalian memahami dan mempelajari apa yang dibutuhkan untuk membangun sebuah fitur (Just in Time Learning). Error? Wajar, itu bagian dari proses belajar. Jangan takut untuk membuat kesalahan, karena dengan membuat kesalahan, kalian akan belajar lebih banyak dan mendapatkan pengalaman yang berharga. Oiya, salah satu kemampuan yang bisa kalian asah pada proyek ini adalah kemampuan debugging, karena kalian akan sering menemui error dan harus mencari tahu penyebabnya untuk memperbaikinya. Apakah AI diperbolehkan? Tentu boleh, tapi kita sesuaikan promptnya:

prompt yang disarankan adalah mengajak AI tersebut untuk berdiskusi, menjelaskan dan mengarahkan kalian untuk menemukan solusi, bukan langsung memberikan solusi. Dengan cara ini, kalian bisa belajar lebih banyak dan mendapatkan pemahaman yang lebih baik tentang konsep yang sedang dipelajari. Happy coding!

Jika kalian merasa kesulitan, stuck, butuh bantuan atau butuh review, jangan ragu untuk berdiskusi dengan mentor dan maintainer utama sistem hidroponik kita:

- @Dzoel31 
- @Kahfii
- Sudarma Yudho (iot)

Selamat bersenang-senang dengan error!