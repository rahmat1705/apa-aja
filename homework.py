# DATA PRIBADI
print("1. DATA PRIBADI")
nama = (input('Masukan nama : '))
nik = int(input('Masukan NIK Anda : '))
tempat = str(input('Masukan Tempat Tinggal : '))
email = str(input('email : '))
print()

# Kelengkapan Syarat
print('2. KELENGKAPAN SYARAT')
wni = (input("input Kewargakenegaraan Anda : "))
pekerjaan = (input('Masukan Pekerjaan : '))
bpjs = (input('Keaktifan BPJS : '))
gaji = float(input('Masukan Gaji Anda : '))

# Syarat
daftar = ['asn','tni','polri']
js = ('aktif')
wei = ('indonesia')

if (wni in wei) and (pekerjaan not in daftar) and (bpjs in js) and (gaji <= 3500000):
    hasil = ('BERHAK MENDAPATKAN Bantuan Subsidi Upah (BSU)')
else:
    hasil = ('TIDAK BERHAK MENDAPATKAN Bantuan Subsidi Upah (BSU)')

print('-'*20)
print('Nama : ', nama)
print('NIK : ', nik)
print('Pekerjaan : ', pekerjaan)
print('Tempat Tinggal : ', tempat)
print('Email ')
print(hasil)