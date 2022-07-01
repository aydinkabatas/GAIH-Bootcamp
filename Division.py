while True:
    try:
        a=int(input("Lütfen bölünecek olan tam sayı giriniz:"))
        b=int(input("Lütfen bölen tam sayıyı giriniz:"))
        break
    except ValueError:
        print("Girdiğiniz değer tam sayı değildir!")

print(a//b)
print(a/b)