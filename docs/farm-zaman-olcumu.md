# Knight Online farm zamanı: çevrimdışı ölçüm aracı

Bu araç NexusForgeKO tarafından, kullanıcıların kendi tuttuğu süre kayıtlarını karşılaştırması için hazırlanmıştır. Oyuna bağlanmaz, karakter yönetmez, oyun dosyalarını okumaz ve ağ isteği göndermez. Python 3 standart kütüphanesiyle çalışır. Bot lisansı veya uyumluluk testi değildir.

## Hangi soruyu yanıtlar?

“Bir saatlik oturumun ne kadarı yolda, NPC'de, bankada ve bakımda geçti?” sorusunu sayısal hale getirir. Satış/depo akışının kurulumu [NPC satışı, banka ve slota dönüş rehberinde](https://nexusforgeko.com/haberler/knight-online-npc-satis-banka-slota-donus) açıklanır. Buradaki araç o işlemler için elle kaydettiğiniz dakikaları toplar.

## Kullanım

Depoyu indirin ve kök klasöründe çalıştırın:

```bash
python3 tools/route_efficiency.py docs/templates/farm-zaman-ornek.csv
```

Windows'ta Python başlatıcısı kuruluysa `python3` yerine `py -3` kullanabilirsiniz. Ek paket veya hesap girişi gerekmez. [Örnek CSV](templates/farm-zaman-ornek.csv) iki **temsili** oturum içerir; bunlar gerçek sunucu veya ürün performans ölçümleri değildir.

```json
{
  "sessions": 2,
  "total_minutes": 120.0,
  "recorded_other_minutes": 35.0,
  "remaining_minutes": 85.0,
  "remaining_percent": 70.83
}
```

Kendi kayıtlarınız için örnek satırları değiştirin. Başlangıç/bitiş noktalarını iki oturumda aynı tutun. Farklı rotaları ayrı dosyalarda özetleyin; farklı koşullardaki kayıtları tek bir karşılaştırma sonucu gibi yorumlamayın.

| CSV sütunu | Dakika olarak kaydedilecek süre |
|---|---|
| `session` | İsteğe bağlı kısa oturum etiketi |
| `total_minutes` | Başlangıçtan bitişe toplam süre; sıfırdan büyük |
| `travel_minutes` | Gidiş ve dönüş yolları |
| `npc_minutes` | NPC satış ve tedarik işlemleri |
| `bank_minutes` | Banka/depo işlemleri |
| `repair_minutes` | Diğer kategorilerde sayılmamış bakım süresi |
| `other_minutes` | Diğer bekleme ve kesintiler |

Dosya virgülle ayrılır; ondalık için nokta kullanılır (`2.5`). Boş veya geçersiz süreler sıfır kabul edilmez. Negatif ve sonlu olmayan sayılar, eksik başlıklar, fazladan sütunlar ve toplam oturum süresini aşan aralıklar hata verir. UTF-8 BOM içeren CSV de okunabilir.

## Sonucu doğru yorumlayın

Formül: `kalan dakika = toplam dakika − kayıtlı diğer süreler`.

`remaining_percent`, kalan dakikanın toplam dakikaya oranıdır. Birden fazla satırda süre ağırlığı kullanılır: toplam kalan dakika / toplam oturum dakikası. Ayrı yüzdelerin basit ortalaması alınmaz.

**Kalan süre, otomatik olarak doğrulanmış aktif farm süresi değildir.** Kayda girmemiş bekleme varsa kalan bölümde görünür. O aralıklarda karakterin gerçekten çalıştığını siz gözlemlemelisiniz. Araç drop değeri, net gelir, sunucu uyumluluğu veya hesap yaptırım durumunu ölçmez.

Ölçüm tasarımı ve tek değişiklikle rota karşılaştırması için [OtomasyonTR süre ölçüm rehberini](https://otomasyontr.tech/makale/knight-online-farm-rotasi-zaman-olcumu) okuyabilirsiniz. Güncel modüller ve videolar [NexusForgeKO ürün dokümantasyonundadır](https://nexusforgeko.com/urun/knight-online-farm-bot).

## Hesaplama kontrolü

```bash
python3 -m unittest discover -s tools -p 'test_route_efficiency.py'
```

Kontroller süre ağırlıklı sonucu, kesirli dakikaları ve geçersiz kayıtların reddini sınar. Bunlar oyun istemcisi testi değildir. CSV'ye parola, OTP, ödeme belgesi veya kişisel bilgi yazmanız gerekmez.
