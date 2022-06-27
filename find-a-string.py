basestr = input("Bir yazı dizisi giriniz: ").strip()
vstr = input("Örüntü aranacak diziyi giriniz: ").strip()

baselen=len(basestr)
vlen=len(vstr)

x=0
for i in range(baselen):
    if basestr[i:i+vlen]==vstr:
        x+=1

print(x,"örüntü gözlemlendi.")