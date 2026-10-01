# Knight Online KOXP için ödeme öncesi uyumluluk kaydı

Bu belge NexusForgeKO’nun resmî kullanıcı dokümantasyonunun bir parçasıdır. Bir bağımsız inceleme, test sonucu veya ücretsiz deneme lisansı değildir.

## 1. İhtiyacı tek senaryoya indirin

- Sunucu ve istemci: kullandığınız tam adı yazın.
- Güncelleme: oyun istemcisinin görünen sürümünü veya son güncelleme tarihini yazın.
- Ortam: Windows sürümü, tek ya da birden fazla oyun istemcisi.
- Hedef: örneğin maden rotası, hedef seçimi veya tedarik akışı. Birden fazla ihtiyacı ayrı satırlara ayırın.

## 2. Gösterilen özellik ile beklenen sonucu ayırın

[KOXP ürün sayfasındaki videoları](https://nexusforgeko.com/urun/knight-online-farm-bot) izlerken ayar ekranının mı, oyun içindeki işlemin mi gösterildiğini not edin. Tarih ve istemci uyuşmuyorsa destekten teyit isteyin. Başka bir özel sunucuda destek olduğunu varsaymayın.

| Kontrol | Kaydedilecek bilgi | Sonuç |
|---|---|---|
| Sunucu | Ürün sayfasında açıklanan kapsam | Teyit edildi / belirsiz |
| Özellik | Videonun adı ve gözlenen işlem | Gösterildi / açıklama gerekli |
| Ortam | Windows ve istemci türü | Uygun / soru var |
| Deneme | Varsa destekçe teyit edilen süre ve kapsam | Teyit edildi / sunulmadı / sorulacak |
| Lisans | Süre ve CR bedeli | Seçildi / karar verilmedi |
| İlk ödeme | Yükleme tutarı ve lisans sonrası kalan kredi | Hesaplandı / soru var |

Doldurulabilir başlangıç şablonu: [uyumluluk-kontrolu.csv](templates/uyumluluk-kontrolu.csv). CSV’yi bir hesap tablosunda açabilir veya düz metin olarak kullanabilirsiniz. Form, bilgileri kendi cihazınızda düzenlemek içindir.

## 3. Bakiye ile lisansı ayrı kontrol edin

Güncel tutarlar [kredi sayfasında](https://nexusforgeko.com/kredi) görünür. Ürün seçimiyle bakiye sayfasına geçtiğinizde lisans süresi, gereken yükleme ve kalan kredi açıklanır. Banka bildirimi ödeme yapmaz; kredi onayı da lisansı otomatik başlatmaz. Onay sonrası ürüne dönüp süreyi seçin.

Krediye yeterli bakiyeniz varsa yeniden yükleme gerekmeyebilir. OTP hesap siparişi, KOXP yazılım lisansından ayrı üründür. Ayrıntılı örnek: [süre ve toplam bütçe rehberi](https://nexusforgeko.com/haberler/koxp-lisans-suresi-ve-butce-secimi).

## 4. Destek talebini netleştirin

> Sunucum: … / İstemcim: … / Windows: … / İstediğim özellik: … / Videoda netleştiremediğim nokta: … . Bu senaryonun kapsamını ve varsa deneme seçeneğini ödeme öncesi teyit edebilir misiniz?

Hesaba özel cevabı [özel destek kaydından](https://nexusforgeko.com/destek) isteyin. Bu formu herkese açık bir GitHub issue’suna parola, OTP kodu, hesap erişimi veya ödeme belgesi ekleyerek göndermeyin.

Kontrol kaydı, yazılım uyumluluğunu değerlendirmeye yardım eder. Gelecek oyun güncellemeleri veya hesabın yaptırım durumu için garanti oluşturmaz.
