import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50008))
s.listen(5)
print "Server siap"
perintah =' '
a=0
t=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan:",perintah
        if len(item)==2:
            if perintah == 'Luas alas':
                a=int(item[1])
                komm,send('Luas alas disimpan')
            elif perintah =='Luas sisi tegak':
                t=int(item[1])
                komm.send('Luas sisi tegak disimpan')
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung':
            L=float(a+4*t)
            response = 'Luas Piramid dengan Luas alas {} Luas sisi tegak {} adalah {}'.format(a,t,)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
        
