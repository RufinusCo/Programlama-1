#Malzeme, işçilik, değişken genel üretim, sabit gdirekt genel üretim ve sabit ortak genel üretim giderleri
def get_input(message): 
  result = None
  while not result:
    try:
      result = int(input(message))
    except ValueError:
        result = None
  return result


print("Durum karşılaştırıcıya hoş geldiniz \n")
adet = get_input("Lütfen üründen kaç tane üretmek istediğinizi giriniz:")
mal_gider = get_input("Lütfen ürün için malzeme giderlerini giriniz:")
is_gider = get_input("Lütfen ürün için işçilik giderlerini giriniz:")
degisken_genel_uretim = get_input("Lütfen ürün için değişken genel üretim giderlerini giriniz:")
sabit_direkt_uretim = get_input("Lütfen ürün için sabit direkt genel üretim giderlerini giriniz:")
sabit_ortak_uretim = get_input("Lütfen ürün için sabit ortak genel üretim giderlerini giriniz:")
satin_alma = adet * get_input("Lütfen ürünün dışarıdaki fiyatını giriniz:")
uretmek = adet * mal_gider + adet * is_gider + adet * degisken_genel_uretim + adet * sabit_direkt_uretim + adet * sabit_ortak_uretim
fark = uretmek - satin_alma

if fark < 0:
    print("Bu ürünü kendiniz üretmeniz sizin için {}$ Dolar farkla daha karlı olacaktır.".format(fark * -1))
elif fark > 0:
    print("Bu ürünü dışarıdan almanız sizin için {}$ Dolar farkla daha karlı olacaktır.".format(fark))
else:
    print("Bu ürünü dışarıdan almanız ile kendiniz üretmeniz arasında herhangi bir finansal fark bulunmamaktadır.")