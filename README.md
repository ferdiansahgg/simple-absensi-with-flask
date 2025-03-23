# simple-absensi-with-flask
Proyek ini adalah web aplikasi berbasis Flask yang memungkinkan pengguna untuk:
✅ Mencatat absensi harian dalam format file .txt.
✅ Mencatat lembur dalam format file .txt.
✅ Menampilkan hasil absensi & lembur langsung di halaman web sebelum diunduh.
✅ Memungkinkan akses dari HP atau perangkat lain dalam jaringan lokal.

Aplikasi ini cocok untuk individu, tim kecil, atau organisasi yang membutuhkan pencatatan absensi sederhana tanpa perlu menggunakan sistem besar seperti HRIS.

Fitur yang Ada :

✅ Form Absensi

- Pengguna mengisi nama, tanggal mulai absensi, jam masuk, jam keluar, dan keterangan (opsional).

- Data absensi otomatis dibuat untuk 5 hari kerja (Senin-Jumat).

- Data bisa langsung dilihat di halaman web sebelum diunduh dalam format .txt.

✅ Form Lembur

- Pengguna mengisi nama, tanggal lembur, jam masuk lembur, jam keluar lembur, dan keterangan (opsional).

- Data lembur bisa langsung ditampilkan dan diunduh dalam format .txt.

✅ Tampilan Hasil

- Hasil absensi dan lembur langsung ditampilkan di browser sebelum diunduh.

- Tersedia link download untuk mengunduh file .txt.

✅ Akses Jaringan Lokal

- Bisa diakses dari HP atau perangkat lain di jaringan yang sama dengan menggunakan IP lokal server Flask.


Teknologi yang Digunakan :

✅ Python 3.13

Bahasa utama dalam pengembangan aplikasi.

✅ Flask

Framework backend yang digunakan untuk menangani request HTTP dan merender template HTML.

✅ HTML + Jinja2

Template engine yang digunakan untuk menampilkan data di halaman web.

✅ CSS (Minimal)

Styling sederhana pada halaman web.

✅ JavaScript (Optional - Tidak Banyak Digunakan)

Bisa ditambahkan jika ada fitur interaktif di masa depan.

✅ Hosting di Localhost

Aplikasi berjalan di komputer lokal, tetapi bisa diakses dari HP melalui IP lokal.

