from model.daftar_nilai import database
from tabulate import tabulate

def tampilkan():
    print(tabulate(database.values(), headers=["NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"], tablefmt="double_grid"))

def cari(nama):
    data_cari = {}
    for key, value in database.items():
        if nama in value:
            data_cari[key] = value
    print(tabulate(data_cari.values(), headers=["NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"], tablefmt="double_grid"))

