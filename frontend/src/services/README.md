# services

Folder ini dipakai untuk fungsi yang berkomunikasi dengan backend atau sistem luar.

Di project ini, `hydroponicApi.ts` menjadi pembungkus kecil untuk generated API client.

Kenapa tetap dibungkus:

- `App.vue` tidak perlu tahu detail nama method hasil generate
- kalau base URL atau cara request berubah, perubahan cukup di service
- kode komponen tetap mudah dibaca pemula

Opsi lain adalah langsung pakai API client hasil generate di `App.vue` atau komponen lain yang memerlukan data dari backend.
