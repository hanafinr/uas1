# uas1

## Projek UAS Bahasa Pemrograman

Nama    : Hanafi Nur Rosyid

NIM     : 312210429
 
Kelas   : TI.22.B2

## Link Youtube
https://youtu.be/_JbOQCTLkDE

## Ketentuan Program
Buatlah package dan modul dengan struktur seperti
berikut:
- daftar_nilai.py berisi modul untuk:
tambah_data, ubah_data, hapus_data,
dan cari_data
- view_nilai.py berisi modul untuk:
cetak_daftar_nilai, cetak_hasil_pencarian
- input_nilai.py berisi modul untuk:
input_data yang meminta pengguna
memasukkan data.
- main.py berisi program utama (menu
pilihan yang memanggil semua menu
yang ada)

# 1.DAFTAR NILAI

Langkah pertama adalah membuat file daftar_nilai.py. Sebelumnya kita harus membuat package yang berisi module seperti dalam ketentuan program di atas terlebih dahulu.

## A. Source Code

![Screenshot (60)](https://user-images.githubusercontent.com/115903342/212006979-2d01e294-754e-4d7f-89c7-0641daa2c754.png)

## B. Penjelasan

- data = {}. adalah Dictonary kosong. Fungsinya untuk menginput data dalam program tersebut dan memudahkan kita untuk memanggil data itu lagi.
- sedangkan def merupakan keyword yang digunakan untuk menyatakn suatu fungsi pada program. isi modul dengan beberapa fungsi yaitu tambah_data, ubah_data, hapus_data, dan cari_data.

# 2.INPUT NILAI

Selanjutnya membuat module input_nilai.py pada package view yang sudah di buat.

## A. Source Code

![Screenshot (61)](https://user-images.githubusercontent.com/115903342/212008058-36896d06-e1da-49e4-9cf5-ab92f59d8fc5.png)
![Screenshot (62)](https://user-images.githubusercontent.com/115903342/212008139-69879697-b926-46b8-bf36-49f2a620cbf1.png)

## B. Penjelasan

    from model.daftar_nilai import tambah_data, hapus_data, ubah_data
    from view.view_nilai import cari

Berfungsi ubntuk memanggil file lain di dalam satu module yang berbeda

# 3.VIEW NILAI

buatlah module view_nilai.py pada package view yang sudah di buat sebelumnya.

## A.Source Code

![Screenshot (63)](https://user-images.githubusercontent.com/115903342/212015759-48ba0329-1066-4037-a136-04421e74d02c.png)

## B. Penjelasan

    from model.daftar_nilai import data
Berfungsi untuk memanggil data(dictionary) pada modul daftar_nilai.py.
    from tabulate import tabulate
Berfungsi untuk mempermudah user dalam membuat table yang di inginkan. Sedangkan tablefmt="double_grid" berfungsi untuk membuat model atau jenis table sesuai yang diinginkan user.

# 4.MAIN
Terakhir membuat file main.py yang berisi code program untuk menyatukan semua fungsi yang ada di beberapa modul yang telah dibuat sebelumnya.

## A. Source Code

![Screenshot (58)](https://user-images.githubusercontent.com/115903342/212016564-f00c266f-e634-4c9d-ab2f-b0367cc2a93d.png)
![Screenshot (59)](https://user-images.githubusercontent.com/115903342/212016911-831dc927-ad0d-4a33-820b-95c11ddef809.png)

## B. Penjelas

- while True Merupakan kondisi perulangan atau looping, di mana kode program akan dijalankan berulang kali sampai mendapatkan kondisi berhenti untuk mengulangnya.
- untuk memembuat perulangan pada pilihan menu yang akan tampil sebagai pilihan user. saya menggunakan fungsi

if
elif
else

fungsi if-else untuk mengambil kondisi tertentu dan memeriksa apakah kondisinya benar atau salah. Jika kondisinya benar, maka pernyataan if mengeksekusi blok kode tertentu. Jika kondisinya salah, maka pernyataan else mengeksekusi blok kode yang berbeda.

# 5.HASIL OUTPUT

### Tambah Data
![Screenshot (1)](https://user-images.githubusercontent.com/115903342/212022803-eff96508-559e-46d5-9be2-e9d940bc70d2.png)

![Screenshot (2)](https://user-images.githubusercontent.com/115903342/212023104-22b31377-93d3-4b37-bad6-a248852c4a9c.png)

### Ubah Data
![Screenshot (3)](https://user-images.githubusercontent.com/115903342/212023204-310f5254-cf3d-45c8-9d2c-f895d9426354.png)

![Screenshot (4)](https://user-images.githubusercontent.com/115903342/212023509-da586942-07b1-42b7-8138-5d1d1e0e0141.png)

![Screenshot (5)](https://user-images.githubusercontent.com/115903342/212023708-becf1238-c561-4052-924e-76101b14bef3.png)

### Cari Data
![Screenshot (6)](https://user-images.githubusercontent.com/115903342/212023772-8831403b-b4e2-451b-b020-27775e5ed471.png)

### Menampilkan Semua Data
![Screenshot (7)](https://user-images.githubusercontent.com/115903342/212023990-29e0e187-5edf-4b3b-93c9-78f52e12e978.png)

### Hapus Data
![Screenshot (8)](https://user-images.githubusercontent.com/115903342/212024166-571cb098-d874-4db4-bf6b-d5279566aeef.png)

### Keluar Program
![Screenshot (9)](https://user-images.githubusercontent.com/115903342/212024241-5b4b4516-d97a-4892-907f-974bf4f3f8cb.png)








