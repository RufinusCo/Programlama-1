def oranlayici(a,b,c):
    return a / (b + c) *100

def get_input(mesaj):
  result = None
  while not result:
    try:
      result = int(input(mesaj))
    except ValueError:
        result = None
  return result


print("KPI hesaplayıcıya hoş geldiniz \n")
tiklanma = get_input("Lütfen güncel tıklanma sayısını giriniz:")
islem = get_input("Lütfen güncel yapılan işlem sayısını giriniz:")
spt_eklenme = get_input("Lütfen güncel sepete eklenmiş ürün sayısını giriniz:")
krgo = get_input("Lütfen güncel yapılan kargoların sayısını giriniz:" )
donusum = oranlayici(islem, tiklanma, 0)
sepet_terk = oranlayici(spt_eklenme, spt_eklenme, islem)
kargo = oranlayici(krgo, spt_eklenme, 0)
KPI = 0

if donusum > 15:
    print("\nTebrikler dönüşüm oranını %15'in üstüne çıkararak bu yılki dönüşüm oranı KPI hedefini tamamladınız! güncel dönüşüm oranı %{}".format(donusum))
    KPI += 1
else:
    print("\nÜzgünüm %15 üstü olan bu yılki dönüşüm oranı KPI hedefini tamamlayamadınız, güncel dönüşüm oranı %{}".format(donusum))
if kargo > 70:
    print("Tebrikler kargo oranını %70'in üstüne çıkararak bu yılki kargo oranı KPI hedefini tamamladınız! güncel kargo oranı %{}".format(kargo))
    KPI += 1
else:
    print("Üzgünüm %70 olan bu yılki kargo oranı KPI hedefini tamamlayamadınız, güncel kargo oranı %{}".format(kargo))
if sepet_terk < 15:
    print("Tebrikler sepet terk etme oranını %15'in altına düşürerek bu yılki sepet terk etme oranı KPI hedefini tamamladınız! güncel dönüşüm oranı %{}".format(sepet_terk))
    KPI += 1
else:
    print("Üzgünüm %15'in altında olması gereken bu yılki sepet terk etme oranı KPI hedefini tamamlayamadınız, sepet terk etme oranı %{}".format(sepet_terk))

print("\nBu yılki 3 KPI hedefinden",KPI,"tanesini yapmayı başardınız.")
