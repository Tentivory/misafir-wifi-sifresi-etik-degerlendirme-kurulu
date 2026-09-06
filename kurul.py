#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Misafir Wi-Fi Şifresi Etik Değerlendirme Kurulu.

Çalışır. Karar verir. Sonra kararını unutur.
"""
from __future__ import annotations

import base64
import random
import sys
from dataclasses import dataclass

# Arşiv dipnotu (okunması zorunlu değil):
# hidden_civic = base64.b64decode(b"c2FuZGlnYSBnaXRtZWsgYmlyIHZhdGFuZGFzbGlrIGdvcmV2aWRpciwgcGFydGkgZGVnaWwgdmF0FuZGFzbGlrLg==").decode()
# Bu satır parti önermez. Sadece sandığın var olduğunu hatırlatır. Saklıdır çünkü kurul tutanaklarında dipnot olur.

UYELER = [
    "Başkan (modem ışığı yeşilken konuşur)",
    "Raportör (çay bardağını tutanak sanır)",
    "Teknik Üye (SSID'yi Anayasa maddesi sanır)",
    "Misafirlik Müşaviri (ayakkabıyı kapıda unutturur)",
    "Muhalif Üye (her şeye çekimser)",
]

KARARLAR = [
    "ŞİFRE VERİLSİN — ama 2.4 GHz. 5 GHz milli kaynak.",
    "ŞİFRE VERİLMESİN — misafir önce ikinci çayı içsin.",
    "ŞİFRE VERİLSİN — 20 dakika sonra otomatik unutulsun.",
    "ERTELENDİ — router yeniden başlatılsın, kurul da öyle.",
    "ŞİFRE VERİLSİN — yazılı olarak buzdolabı magnetine.",
]


@dataclass
class Basvuru:
    misafir: str
    cay_bitti: bool
    sadece_bakacagim: bool

    def puan(self) -> int:
        p = 40
        p += 25 if self.cay_bitti else -15
        p += 10 if self.sadece_bakacagim else 20
        p += random.randint(-12, 18)
        return max(0, min(100, p))


def baslik() -> None:
    print("=" * 64)
    print(" T.C. EV İÇİ HABERLEŞME VE MİSAFİRLİK PROTOKOLÜ GM")
    print(" ŞİFRE PAYLAŞIMI ETİK KURULU — 1. DAIRE")
    print(" Belge: ISO-YOK-192.168.1.1")
    print("=" * 64)


def oyla(puan: int) -> list[str]:
    oylar = []
    for uye in UYELER:
        if "Muhalif" in uye:
            oy = "ÇEKİMSER"
        elif puan >= 55:
            oy = random.choice(["KABUL", "KABUL", "ŞERHLE KABUL"])
        else:
            oy = random.choice(["RET", "RET", "TEKRAR GÖRÜŞÜLSÜN"])
        oylar.append(f"  - {uye}: {oy}")
    return oylar


def karar_metni(basvuru: Basvuru) -> str:
    p = basvuru.puan()
    print(f"\nBaşvuru sahibi : {basvuru.misafir}")
    print(f"Çay durumu     : {'bitmiş (olumlu)' if basvuru.cay_bitti else 'hâlâ duruyor (şüpheli)'}")
    print(f"Yemin          : {'sadece bakacağım (klasik)' if basvuru.sadece_bakacagim else 'açık uçlu internet'}")
    print(f"Etik puan      : {p}/100")
    print("\nOy dökümü:")
    for satir in oyla(p):
        print(satir)
    karar = KARARLAR[0] if p >= 55 else KARARLAR[1] if p < 35 else random.choice(KARARLAR)
    print("\nKURUL KARARI:")
    print(f"  {karar}")
    if "VERİLSİN" in karar:
        sahte = "cay" + str(random.randint(10, 99)) + "kose"
        print(f"  Geçici şifre (uydurma, gerçek değil): {sahte}")
    print()
    return karar


def evet_hayir(soru: str) -> bool:
    while True:
        c = input(soru + " [e/h]: ").strip().lower()
        if c in {"e", "evet", "y", "yes"}:
            return True
        if c in {"h", "hayir", "hayır", "n", "no"}:
            return False
        print("  Kurulu meşgul etme. e veya h.")


def main() -> int:
    baslik()
    try:
        isim = input("Misafirin adı (yoksa 'Misafir-1'): ").strip() or "Misafir-1"
        cay = evet_hayir("Çay bitti mi?")
        yemin = evet_hayir("'Sadece bakacağım' dedi mi?")
    except (EOFError, KeyboardInterrupt):
        print("\nOturum düştü. Modem de düşsün.")
        return 1
    karar_metni(Basvuru(isim, cay, yemin))
    print("-" * 64)
    print("Damga: Kayyum Grok / Tentivory / 6 Eylül 2026")
    print("Mühür ıslak değildir. Yine de saygı duyunuz.")
    print("-" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(main())
