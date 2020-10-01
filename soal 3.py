print('Menghitung BMI (Body Mass Index), atau Index Masa Tubuh')
bb=float(input('masukkan berat badan tubuh anda (dalam satuan kg): '))
tb=float(input('masukkan tinggi badan tubuh anda (dalam satuan meter): '))
bmi=bb/(tb*tb)
hasil=print('BMI anda adalah', bmi)

if bmi > 30:
    print('obesitas')
elif bmi >= 23:
    print('berat badan anda berlebih (kecenderungan obesitas)')
elif bmi >= 18.5:
    print('berat badan anda normal')
elif bmi < 18.5:
    print('berat badan anda kurang')
else:
    print('error')

