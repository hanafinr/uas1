database = {}

def tambah_data(nama, nim, tugas, uts, uas, akhir):
    database[nama] = nama, nim, tugas, uts, uas, akhir

def hapus_data(nama):
    if nama in database.keys():
        del database[nama]
        print(f'data dengan nama {nama} berhasil dihapus')
        return True
    else:
        print(f'data dengan nama {nama} tidak ditemuykan!!')
        return False

def ubah_data(nama):
    if nama in database.keys():
        del database[nama]

def cari_data():
    from view.view_nilai import cari
    cari(input("masukan nama yang ingin dicari = "))