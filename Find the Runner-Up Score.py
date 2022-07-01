while True:
    try:
        n=int(input("Kaç yarışçının skorunu gireceksiniz? (2 ile 10 arası):"))
        if n>=2 and n<=10:
            break
        else:
            print("Girdiğiniz değer 2 ile 10 arasında değil! Lütfen tekrar değer girin.")
    except ValueError:
        print("Girdiğiniz değer bir tam sayı değildir!")

kume=[]
x=0

while True:
    try:
        data=float(input("Lütfen skoru giriniz (-100 ile +100 arası):"))
        if data >=-100 and data <= 100:
            kume.append(data)
            x+=1
            if x==n:
                break
        else:
            print("Girdiğiniz değer -100 ile 100 arasında değil! Lütfen tekrar değer girin.")
    except ValueError:
        print("Girdiğiniz değer bir sayı değildir!")

ix=0
scndmax=0.0
kume.sort()
while True:
    if kume[ix]==max(kume):
        scndmax=kume[ix-1]
        break
    ix+=1
print("İkinci'nin puanı:",scndmax)
