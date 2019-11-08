Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Buhtiar Aimar K'
>>> NIM = 205
>>> Tinggi = 1.76
>>> Berat = 69
>>> TahunLahir = 2001
>>> Aku =(TahunLahir,Berat,Tinggi,NIM,Nama)
>>> Data =[TahunLahir,Berat,Tinggi,NIM,Nama]
>>> type(Aku)
<class 'tuple'>
>>> #Karena data "Aku" tertulis dalam tanda kurung yang bertype data tuple menghimpun sembarang data dan bersifat tidak bisa berubah
>>> Aku[0]
2001
>>> #Karena objek pertama dari "Aku" adalah data "TahunLahir",Nilai dari data "TahunLAHIR adalah 2001
>>> a = NIM % 4; Aku[a]
69
>>> #Karena nilai dari 205 dibagi 4 adalah 1,jadi nilai Aku[1] adalah berat yaitu 69
>>> type(Aku[a])
<class 'int'>
>>> #Karena nilai dari "Berat' adalah 1,1 adalah type data integer
>>> Aku[a:4]
(69, 1.76, 205)
>>> #Karena 4 objek utama dari "Aku" adalah data "Berat","Tinggi","NIM"
>>> type(Aku[4])
<class 'str'>
>>> #Karena urutan ke 4 dalam data "Aku" adalah "Nama",Nilai dari "Nama" adalah 'Buhtiar Aimar K' yang bertype data integer
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #ERORR Karena data Aku pada urutan objek ke o adalah "TahunLahir" yang mempunyai data tidak bisa dirubah atau tupple
>>> type(Data)
<class 'list'>
>>> #Karena nilai dari "Data" adalah mutable bisa bertambah,berkurang, dan berubah serta menghimpun sembarang data yang lain yang bertype data list
>>> type(Data[4])
<class 'str'>
>>> #Karena urutan objek ke 4 dari "Data" adalah "Nama" yang mempunyai nilai 'Buhtiar Aimar K' yang bertype data string
>>> Data [4][5]
'a'
>>> #Karena urutan objek ke 4 dari "Data" adalah "Nama",Serta urutan objek ke 5 dari data "Nama" adalah a,maka hasilnya a
>>> Data [4][a:6]
'uhtia'
>>> #Karena urutan objek  ke 4 dari "Data" adalah "Nama",Serta variabel "a" berisi objek nomor urutan 0,sehingga isi dari data "Nama[0:6]" adalah uhtia
>>> Data [0] = 'ok' ; Data
['ok', 69, 1.76, 205, 'Buhtiar Aimar K']
>>> #Karena urutan data ke 0 dalam "Data" adalah "TahunLahir" yang bertype data integer,kemudian diubah menjadi "ok".Kemudian isi dari data "Data" adalah "TahunLahir","Berat","Tinggi","NIM","Nama"
>>> Data [-a]
'Buhtiar Aimar K'
>>> #Karena menampilkan urutan pertama dari kanan oleh "Data" adalah "Buhtiar Aimar K"
>>> range(a)
range(0, 1)
>>> #Karena variabel a adalah 1,jadi "range(a) adalah "range(0,1) yang memiliki objek/indeks 1
