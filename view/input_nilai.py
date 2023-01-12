from model.daftar_nilai import tambah_data, hapus_data, ubah_data

def masukan_data():
    print("------------------------:")
    print("|-silahkan masukan data-|")
    print("------------------------:")

    nama = input("masukan nama = ")
    nim = int(input("masukan nim = "))
    tugas = int(input("masukan nilai tugas = "))
    uts = int(input("masukan nilai uts = "))
    uas = int(input("masukan nilai uas = "))
    akhir = float((0.30*tugas)+(0.35*uts)+(0.35*uas))
    tambah_data(nama, nim, tugas, uts, uas, akhir)

def cari_hapus():
    hapus_data(input("masukan nama yang ingin di hapus = "))

def cari_ubah():
    ubah_data(input("masukan nama data yang ingin di ubah = "))
    print()
    print("|----------------------------|")
    print("|-silahkan masukan data baru-|")
    print("|----------------------------|")

    nama = input("masukan nama = ")
    nim = int(input("masukan nim = "))
    tugas = int(input("masukan nilai tugas = "))
    uts = int(input("masukan nilai uts = "))
    uas = int(input("masukan nilai uas = "))
    akhir = float((0.30 * tugas) + (0.35 * uts) + (0.35 * uas))
    tambah_data(nama, nim, tugas, uts, uas, akhir)
