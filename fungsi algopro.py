def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")
anggota = ["icha", "mutiara", "nita"]

say_hi(anggota)
