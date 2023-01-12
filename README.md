# uas1

## Projek UAS Bahasa Pemrograman

Nama    : Hanafi Nur Rosyid 
NIM     : 312210429 
Kelas   : TI.22.B2

## Link Youtube

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

## 1.DAFTAR NILAI

Langkah pertama adalah membuat file daftar_nilai.py. Sebelumnya kita harus membuat package yang berisi module seperti dalam ketentuan program di atas terlebih dahulu.

# A. Source Code

![Screenshot (60)](https://user-images.githubusercontent.com/115903342/212006979-2d01e294-754e-4d7f-89c7-0641daa2c754.png)

# B. Penjelasan

- data = {}. adalah Dictonary kosong. Fungsinya untuk menginput data dalam program tersebut dan memudahkan kita untuk memanggil data itu lagi.
- sedangkan def merupakan keyword yang digunakan untuk menyatakn suatu fungsi pada program. isi modul dengan beberapa fungsi yaitu tambah_data, ubah_data, hapus_data, dan cari_data.

## 2.INPUT NILAI

Selanjutnya membuat module input_nilai.py pada package view yang sudah di buat.

# A. Source Code

![Screenshot (61)](https://user-images.githubusercontent.com/115903342/212008058-36896d06-e1da-49e4-9cf5-ab92f59d8fc5.png)
![Screenshot (62)](https://user-images.githubusercontent.com/115903342/212008139-69879697-b926-46b8-bf36-49f2a620cbf1.png)

# B. Penjelasan

    from model.daftar_nilai import tambah_data, hapus_data, ubah_data
    from view.view_nilai import cari

Berfungsi ubntuk memanggil file lain di dalam satu module yang berbeda

## 3.VIEW NILAI

buatlah module view_nilai.py pada package view yang sudah di buat sebelumnya.

# A.Source Code

![Screenshot (63)](https://user-images.githubusercontent.com/115903342/212015759-48ba0329-1066-4037-a136-04421e74d02c.png)

# B. Penjelasan

    from model.daftar_nilai import data
Berfungsi untuk memanggil data(dictionary) pada modul daftar_nilai.py.
    from tabulate import tabulate
Berfungsi untuk mempermudah user dalam membuat table yang di inginkan. Sedangkan tablefmt="double_grid" berfungsi untuk membuat model atau jenis table sesuai yang diinginkan user.

## 4.MAIN
Terakhir membuat file main.py yang berisi code program untuk menyatukan semua fungsi yang ada di beberapa modul yang telah dibuat sebelumnya.

# A. Source Code

![Screenshot (58)](https://user-images.githubusercontent.com/115903342/212016564-f00c266f-e634-4c9d-ab2f-b0367cc2a93d.png)
![Screenshot (59)](https://user-images.githubusercontent.com/115903342/212016911-831dc927-ad0d-4a33-820b-95c11ddef809.png)

# B. Penjelas

- while True Merupakan kondisi perulangan atau looping, di mana kode program akan dijalankan berulang kali sampai mendapatkan kondisi berhenti untuk mengulangnya.
- untuk memembuat perulangan pada pilihan menu yang akan tampil sebagai pilihan user. saya menggunakan fungsi

if
elif
else

fungsi if-else untuk mengambil kondisi tertentu dan memeriksa apakah kondisinya benar atau salah. Jika kondisinya benar, maka pernyataan if mengeksekusi blok kode tertentu. Jika kondisinya salah, maka pernyataan else mengeksekusi blok kode yang berbeda.

## 5.HASIL OUTPUT







