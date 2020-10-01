loop=0
while loop<3:
    username=str(input('masukkan username anda: '))
    password=str(input('masukkan password anda: '))
    if username=='imamgalih' and password=='sidorejo':
        print('anda berhasil masuk')
        break
    else:
        print('maaf username dan password yang anda masukkan gagal')
    loop+=1
