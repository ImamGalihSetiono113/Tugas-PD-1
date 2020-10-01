print("menghitung keliling dan luas bangun datar")
print('pilih keliling bangun apa yang ingin anda cari:')
print('a. Persegi')
print('b. Persegi Panjang')
print('c. Segitiga')
print('d. Lingkaran')
pilih = input('pilih: ')

if pilih=='a':
    s=int(input('masukkan sisi persegi: '))
    kelp=4*s
    lp=s*s
    print('hasil keliling persegi adalah ',kelp)
    print('hasil luas persegi adalah ',lp)
elif pilih=='b':
    p=int(input('masukkan panjang persegi panjang: '))
    l=int(input('masukkan lebar persegi panjang: '))
    kelpp=2*(p+l)
    lpp=p*l
    print('hasil keliling persegi panjang adalah ',kelpp)
    print('hasil luas persegi panjang adalah ',lpp)
elif pilih=='c':
    a=int(input('masukkan sisi a segitiga: '))
    b=int(input('masukkan sisi b segitiga: '))
    c=int(input('masukkan sisi c segitiga: '))
    t=int(input('masukkan tinggi segitiga: '))
    kels=a+b+c
    ls=1/2+a*t
    print('hasil keliling segitiga adalah ',kels)
    print('hasil luas segitiga adalah ',ls)
elif pilih=='d':
    r=int(input('masukkan jari-jari lingkaran: '))
    kelr=2*3.14*r
    lr=3.14*r**2
    print('hasil keliling lingkaran adalah ',kelr)
    print('hasil luas lingkaran adalah ',lr)
else:
    print('menu yang anda inputkan salah, harap coba kembali')


