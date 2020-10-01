angka = []
a= int(input('masukkan nilai yang ingin anda proses: '))
angka.append(a)
menu=str(input('apakah anda ingin menambahkan angka lagi?(y/t: '))
while menu=='y':
    a= int(input('masukkan nilai yang ingin anda proses: '))
    angka.append(a)
    menu=str(input('apakah anda ingin menambahkan angka lagi?(y/t: '))

print('nilai yang anda masukkan: ', angka)
print('pilih menu yang ingin anda jalankan')
print('a. nilai maksimal')
print('b. nilai minimal')
pilih=input('pilih: ')

if pilih=='a':
    print('nilai maksimal', max(angka))
elif pilih=='b':
    print('nilai minimal', min(angka))
else:
    print('pilih menu yang sesuai')
