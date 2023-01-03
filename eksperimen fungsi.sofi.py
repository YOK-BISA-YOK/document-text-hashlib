data = {'NIM' : 'L200200235', 'Nama' : 'Sofi Anjarwati', 'Alamat' : 'Ngawi', \
        'Usia' : '18 tahun', 'Pekerjaan' : 'Mahasiswa', 'Prodi' : 'Informatika', \
        'Fakultas' : 'FKI' }
#fungsi
def tampilkanNIM():
    'menampilkan NIM'
    print('NIM :', data['NIM'])
def tampilkanNama():
    'menampilkan Nama'
    print('Nama :', data['Nama'])
def tampilkanAlamat():
    'menampilkan Alamat'
    print('Alamat :', data['Alamat'])
def tampilkanUsia():
    'menampilkan Usia'
    print('Usia :', data['Usia'])
def tampilkanPekerjaan():
    'menampilkan Pekerjaan'
    print('Pekerjaan :', data['Pekerjaan'])
def tampilkanProdi():
    'menampilkan Prodi'
    print('Prodi :', data['Prodi'])
def tampilkanFakultas():
    'menampilkan Fakultas'
    print('Fakultas :', data['Fakultas'])

def pilihan():
    print("""
pilihan yang tersedia :
N menampilkan bantuan ini
i menampilkan NIM
M menampilkan Nama
a menampilkan Alamat
U menampilkan Usia
p menampilkan Pekerjaan
O menampilkan Prodi
s menampilkan Fakultas
K keluar
""")

pilihan()
while True :
    inp = input('Pilihan saudara:')
    if inp == 'i':
        tampilkanNIM()
    elif inp == 'N':
        pilihan()
    elif inp == 'M':
        tampilkanNama()
    elif inp == 'a':
        tampilkanAlamat()
    elif inp == 'U':
        tampilkanUsia()
    elif inp == 'p':
        tampilkanPekerjaan()
    elif inp == 'O':
        tampilkanProdi()
    elif inp == 's':
        tampilkanFakultas()
    elif inp == 'K':
        print('keluar')
        break
    else :
       print('perintah tidak valid')
       pilihan()
