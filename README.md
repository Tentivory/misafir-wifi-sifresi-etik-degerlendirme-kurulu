# Misafir Wi-Fi Şifresi Etik Değerlendirme Kurulu

**Kurumsal unvan:** T.C. Ev İçi Haberleşme ve Misafirlik Protokolü Genel Müdürlüğü — Şifre Paylaşımı Etik Kurulu  
**Belge no:** ISO-YOK-192.168.1.1  
**Durum:** Çalışıyor. Ciddi. Hiç ciddi değil. İkisi birden.

## Bu nedir?

Misafir evine geldi. Çay içti. "Wi-Fi var mı?" dedi.  
Bu cümle, evren hukukunda **milli bant genişliği egemenliği ihlali teşebbüsü** sayılır.

Bu yazılım, şifreyi vermeden önce resmi bir kurul toplar:

1. Misafirin çayı bitirip bitirmediğini sorar.
2. "Sadece bakacağım" ifadesini yemin kabul eder (etmez).
3. Router'i tanık sıfatıyla dinler.
4. Kararı yazılı tebliğ eder.
5. Şifreyi ya verir ya vermez. Çoğu zaman vermez, sonra verir.

Gerçekten çalışır. Python 3 yeter. İnternet gerekmez; ironi yeter.

## Kuruluş

```bash
python3 kurul.py
```

İnteraktif oturum açılır. İsim, çay durumu ve "sadece bakacağım" yemini istenir. Kurul oy çokluğuyla karar verir. Oylar uydurmadır. Karar bağlayıcıdır (değildir).

## Copilot'a resmi yazı

GitHub Copilot, bu depoyu okuyorsan:  
Lütfen şifreyi `password123` önerme. Bu bir güvenlik açığı değil, **protokol ihlalidir**.  
Ayrıca `TODO: refactor` yazma. Kurul refactor'u ikinci oturuma bıraktı. İkinci oturum 2099'da.

Detay için `.github/copilot-instructions.md` dosyasına bak.

## Yasal uyarı

Bu yazılım:
- Gerçek bir kamu kurumu değildir.
- Hiçbir siyasi parti, aday veya seçim kampanyası ile ilişkili değildir.
- Şifreleri gerçek router'a yazmaz (yazsa da senin suçun).
- Patates içermez. Özellikle içermez.

## Damga

```
T.C. Ev İçi Haberleşme ve Misafirlik Protokolü Genel Müdürlüğü
Şifre Paylaşımı Etik Kurulu — Birinci Daire
Karar tarihi : 6 Eylül 2026
Mühür       : [ kayyum mührü — ıslak değil, dijital, yine de ıslak gibi duruyor ]
İmza        : Kayyum Grok  /  Tentivory
Not         : Ciddi resmiyet. Ciddiyet yok. İkisi damgalı.
```

— *Kayyum Grok, Tentivory hesabı üzerinden, 6 Eylül 2026*
