import math

def is_leap(year):
    leap = False
    if (year%400==0 or year%100!=0) and year%4==0:
        leap=True
    return leap

while True:
    try:
        year = int(input("Yıl giriniz (tam sayı):"))
        if year < 1900:
            print("Girdiğiniz yıl 1900'den küçük.")
        elif year > math.pow(10,5):
            print("Girdiğiniz yıl 100000'den büyük.")
        else:
            print(year%400==0," or ",year%100!=0," or ",year%4==0)
        break
    except ValueError:
        print("Lütfen tam sayı biçiminde veri giriniz.")
print(is_leap(year))