import random
x = random.randint(1, 100)

can = int(input('Kaç hak ile sayıyı tahmin edersiniz ? : '))
hak = can
sayac=0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('1 ile 100 arasında sayı tahmini yapınız : '))
    
    if x==tahmin:
        print(f'Tebrikler tahmininiz doğru. {sayac} tahmininizde bildiniz.')
        print(f'Toplam puanınız : {100 - (100/can) * (sayac-1)}')
        break
    elif x<tahmin:
        print('Aşağı ininiz.')
    else:
        print('Yukarı çıkınız.')
    if hak == 0:
        print(f'Maalesef hakkınız dolmuştur.Doğru cevap : {x}')