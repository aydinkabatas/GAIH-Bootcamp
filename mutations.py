basestr=input("Bir yazı giriniz: ").strip()
vstr=input("Hangi harfi değiştirmek istiyorsunuz?: ").strip()

baselen=len(basestr)

while True:
    vlen=len(vstr)
    if vlen>1:
        print("Hece ya da kelime değil, harf giriniz.")
        vstr=input("Hangi harfi değiştirmek istiyorsunuz?: ").strip()
    else:
        z=0
        for i in range(baselen):
            if basestr[i]==vstr:
                z+=1
        if z>0:
            break
        else:
            print("Girdiğiniz yazıda böyle bir harf yok")
            vstr=input("Hangi harfi değiştirmek istiyorsunuz?: ").strip()

x=0
y=[]
for i in range(baselen):
    if basestr[i]==vstr:
        y.append(i)
        x+=1

vloc=0
if x>1:
    print("Girdiğiniz yazı içerisinde ",x,"tane aranan harf bulunmaktadır.")
    while True:
        try:
            vloc=input("Kaçıncı harfi değiştirmek istiyorsunuz? (ilk index 1 olmak üzere): ")
            vloc=int(vloc)
            if vloc > x or vloc < 0:
                print("Girdiğiniz index değeri 0'dan küçük ya da ",x,"'ten büyük.")
            else:
                break
        except ValueError:
            print("Girdiğiniz değer hataya sebebiyet vermektedir (Sebebi neydi ki?).\nNeyse, sana bir şans daha...")

nstr=input("Yerine hangi harfi yazmak istiyorsunuz?: ").strip()
while True:
    nlen=len(nstr)
    if nlen>1:
        print("Hece ya da kelime değil, harf giriniz.")
        nstr=input("Yerine hangi harfi yazmak istiyorsunuz?: ").strip()
    else:
        break

baselist = list(basestr)
if vloc > 0:
    baselist[y[vloc-1]]=nstr
else:
    baselist[y[0]]=nstr

baselist = ''.join(baselist)

print(baselist)