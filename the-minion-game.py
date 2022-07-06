kamil = ['a','e','ı','i','o','ö','u','ü']
seyit = ['z', 'y', 'v', 't', 'ş', 's', 'r', 'p', 'n', 'r', 'm', 'l', 'k', 'h', 'j', 'ğ', 'g', 'd', 'ç', 'c', 'b']
kamilscore=[]
seyitscore=[]

kelime = 'zargana'

kamilpoint=seyitpoint=kamiltahminsayi=seyittahminsayi=0

while True:
    kamilharf=input('Sıra Kamil\'de. Kelime gir Kamil:')
    if kamilharf[0] not in kamil:
        print("Hatalı harf ile başladın. Hile yapmaya çalıştın. Sıra rakibine geçti.")
    else:
        for i in range(len(kelime)):
            if kelime[i:i+len(kamilharf)]==kamilharf:
                kamilpoint+=1
        kamilscore.append(kamilpoint)
        print("Kamil'in puanı: ",kamilpoint)
        kamilpoint=0

    seyitharf=input('Sıra Seyit\'de. Kelime gir Seyit:')
    if seyitharf[0] not in seyit:
        print("Hatalı harf ile başladın. Hile yapmaya çalıştın. Sıra rakibine geçti.")
    else:
        for i in range(len(kelime)):
            if kelime[i:i+len(seyitharf)]==seyitharf:
                seyitpoint+=1
        seyitscore.append(seyitpoint)
        print("Seyit'in puanı: ",seyitpoint)
        seyitpoint=0    

    if kamilharf==kelime or seyitharf==kelime:
        print("Bir kazananımız var!")
        for i in range(len(kamilscore)):
            try:
                kamilpoint+=int(kamilscore[i])
            except:
                kamilpoint=0
        for i in seyitscore:
            try:
                seyitpoint+=int(seyitscore[i])
            except:
                seyitpoint=0
        if seyitpoint==kamilpoint:
            print("Berabere!!!")
        elif seyitpoint>kamilpoint:
            print("Seyit Kazandı!!! Seyit:",seyitpoint," - Kamil:",kamilpoint)
        else:
            print("Kamil Kazandı!!! Kamil:",kamilpoint," - Seyit:",seyitpoint)
        break