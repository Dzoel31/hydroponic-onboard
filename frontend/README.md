# Hydroponic Onboard Frontend

Frontend ini adalah contoh kecil untuk belajar alur aplikasi web modern dengan TypeScript, Vue, dan Vite.

## Why We Use This

- TypeScript membantu kita menangkap kesalahan tipe data lebih awal.
- Vue membuat UI mudah dipecah menjadi komponen kecil.
- Vite membuat proses development cepat dan sederhana.
- CSS murni dipakai agar anggota baru memahami dasar styling sebelum memakai framework CSS.
- OpenAPI client generation membantu frontend mengikuti kontrak API backend.

## Alur Folder

- `src/main.ts`: titik masuk aplikasi Vue.
- `src/App.vue`: halaman utama dashboard hidroponik.
- `src/api`: hasil generate dari OpenAPI backend.
- `src/assets`: aset yang di-import dari kode frontend.
- `src/components`: komponen Vue yang bisa dipakai ulang.
- `src/reference`: catatan pembanding dengan repo utama.
- `src/router`: tempat routing jika aplikasi sudah punya banyak halaman.
- `src/services`: tempat fungsi komunikasi ke backend.
- `src/utils`: helper kecil yang bisa dipakai ulang.
- `src/views`: halaman utama jika Vue Router sudah digunakan.

Tidak semua folder langsung dipakai di tahap awal. Folder tetap dibuat agar struktur onboarding terasa dekat dengan repo utama.

## Cara Menjalankan

1. Masuk ke folder frontend.
2. Install dependency dengan `npm install`.
3. Jalankan backend di `http://127.0.0.1:8000`.
4. Jalankan frontend dengan `npm run dev`.
5. Buka URL yang ditampilkan Vite.

## Generate API

Pastikan backend sedang berjalan, lalu jalankan:

```bash
npm run generate-api
```

Command ini membaca OpenAPI schema dari backend:

```text
http://127.0.0.1:8000/openapi.json
```

Lalu menghasilkan client TypeScript di:

```text
src/api
```

Di Windows, generator lebih stabil jika schema diunduh dulu ke file lokal. Karena itu script `generate-api` menjalankan `scripts/download-openapi.mjs`, lalu memanggil `npx openapi-typescript-codegen`.

`src/services/hydroponicApi.ts` memakai client hasil generate, tetapi tetap dibungkus dalam fungsi kecil supaya `App.vue` mudah dibaca.
