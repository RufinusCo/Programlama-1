talep = []
cevap = []

def oran_hesap():
    return cevap.count(1) / talep.count(1) * 100

while True:
    print("Talebiniz alındı lütfen bekleyiniz.")
    talep += [1]
    soru = input("Talebinize cevap verildi mi?")
    if soru == "evet" or soru == "Evet":
        cevap.append(1)
        oran = oran_hesap()
        print("Güncel Talep, cevap oranı: ½{}".format(oran))
    elif soru == "hayır" or soru == "Hayır":
        cevap += [0]
        oran = oran_hesap()
        print("Güncel Talep, cevap oranı: ½{}".format(oran))
    else:
        print("Lütfen cevabınızı ""Evet"" veya ""Hayır"" olarak veriniz")
        continue

    if oran < 80:
        print("Günlük taleplere verilen cevap oranı ½80'in altına düştü lütfen departman yöneticisine haber veriniz. Güncel oran: ½{}".format(oran))
        print("Bugün alınan talep sayısı:",talep.count(1),"Bugün taleplere verilen cevap sayısı:",cevap.count(1),"Bugün taleplere verilmeyen cevap sayısı:",cevap.count(0))
        break
