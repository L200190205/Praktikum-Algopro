Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Program Akun
>>> ## Dibuat oleh Buhtiar L200190205
>>> import random
>>> angka = random.randint(0,1000)
>>> 
>>> Nama = 'Buhtiar Aimar Khadafi'
>>> TanggalLahir = '10 Agustus 2001'
>>> NamaSingkat = Nama[0] + '.' + Nama[8] + '.' + Nama[14:21]
>>> Password = Nama[14:21] + str(angka)
>>> 
>>> print(Nama)
Buhtiar Aimar Khadafi
>>> print(TanggalLahir)
10 Agustus 2001
>>> print(NamaSingkat)
B.A.Khadafi
>>> print(Password)
Khadafi250
>>> 
