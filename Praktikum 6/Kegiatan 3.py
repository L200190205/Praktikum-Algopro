Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Buhtiar Aimar Khadafi'
>>> NIM = 'L200190205'
>>> X = '1'+ NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> 
>>> type(a)
<class 'int'>
>>> #Karena nilai dari data a adalah 1205,1205 adalah type data integer
>>> type(b)
<class 'int'>
>>> #Karena data b memiliki type data len dari data Nama yang berarti jumlah karakter dari data Nama yaitu berjumlah 21,21 adalah type data integer
>>> a / b
57.38095238095238
>>> #Karena hasil dari 1205 di bagi 21 adalah 57.38095238095238
>>> a // b
57
>>> #Karena hasil pembagian dengan pembulatan dari 1205 dibagi 21 adalah 57
>>> 10 *(a-999)
2060
>>> #Karena nilai dari a di kurangi 999 adalah 206,sesudah itu di kalikan dengan 10 adalah 2060
>>> b ** 2
441
>>> #Karena arti dari "**" adalah kuadrat,maka kuadrat dari 21 adalah 441
>>> a % b
8
>>> #Karena arti dari "%" adalah sisa hasil bagi,maka sisa hasil bagi dari 1205 di bagi 21 adalah 8
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #Karena nilai dari data c adalh 12.5,yang bertype data float
>>> a / c
96.4
>>> #Karena hasil dari 1205 di bagi dengan 12.5 adalah 96.4
>>> a // c
96.0
>>> #Karena hasil pembagian dengan pembulatan dari 1205 di bagi 12.5 adalah 96.0
>>> a % c
5.0
>>> #Karena arti dari "%" adalah sisa hasil bagi,maka sisa hasil bagi dari 1205 di bagi 12.5 adalah 5.0
>>> c > b
False
>>> #Karena nilai dari 12.5 tidak lebih besar dari 21,maka hasil false
>>> type(c > b)
<class 'bool'>
>>> #Karena ">" merupakan type data bool atau perbandingan
>>> a > b and b > c
True
>>> #Karena nilai perbandingan dari 1205 benar lebih besar dari 21 dan nilai perbandingan dari 21 lebih besar dari 12.5
>>> a > 1100 or b < 10
True
>>> #Karena nilai perbandingan dari 1205 benar lebih besar dari 1100 atau nilai dari 21 lebih besar dari 10 juga benar,maka hasil true
>>> 
