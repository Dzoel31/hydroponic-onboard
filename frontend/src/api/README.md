# api

Folder ini berisi kode hasil generate dari OpenAPI backend.

Cara membuat ulang folder ini:

```bash
npm run generate-api
```

Kenapa folder ini penting:

- frontend tidak menebak bentuk request dan response
- tipe data mengikuti kontrak backend
- perubahan endpoint bisa terlihat lebih cepat

Catatan: file di folder ini sebaiknya tidak diedit manual. Kalau kontrak backend berubah, jalankan ulang `npm run generate-api`.
