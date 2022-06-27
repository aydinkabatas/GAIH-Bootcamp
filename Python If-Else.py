try:
    baseint = int(input("Bir tam sayı giriniz: "))
    if baseint%2==1:
        print("Weird")
    elif baseint%2==0 and baseint >=2 and baseint <=5:
        print("Not Weird")
    elif baseint%2==0 and baseint >=6 and baseint <=20:
        print("Weird")
    elif baseint%2==0 and baseint >20:
        print("Not Weird")

except ValueError:
    print("Woawww, thats a OMEGA-WEIRD!\nGirdiğiniz değer bir tam sayı değildir.")