def kabisat():
    tahun=int(input('Input Tahun : '))
    if tahun%4==0:
        if tahun%100==0:
            if tahun%400==0:
                print('Hasil : Tahun Kabisat')
            else:
                print('Hasil : Bukan Tahun Kabisat')
        else:
            print('Hasil : Bukan Tahun Kabisat')
    else:
        print('Hasil : Bukan Tahun Kabisat')

kabisat()