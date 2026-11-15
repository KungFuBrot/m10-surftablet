# M10 Surftablet

Ein altes BQ Aquaris M10 wird zu einem schlanken Surftablet für das Heimnetz. Der Schwerpunkt liegt auf Tempo und Sicherheit, mit möglichst wenigen Apps.

**Stand:** Planung. Am Tablet wurde noch nichts verändert. Die nächsten Schritte und offenen Fragen stehen in der [Übergabe](CLAUDE.md).

## Zielgerät

| | |
|---|---|
| Gerät | BQ Aquaris M10 (10 Zoll), Variante HD (`cooler`) oder FHD (`frieza`), noch zu bestimmen |
| Chip | MediaTek MT8163, 64-Bit ARM |

## Entscheidung: LineageOS statt klassischem Linux

| Weg | Aufwand | Sicherheit | Tempo |
|---|---|---|---|
| Ubuntu Touch 16.04 | Gering | Schlecht: der Browser ist jahrelang veraltet | Ordentlich |
| **LineageOS (inoffiziell) mit aktuellem Browser** | Mittel | Am besten, weil der Browser aktuell bleibt | Am besten, die Grafikbeschleunigung funktioniert |
| Eigene postmarketOS-Portierung | Sehr hoch, Ausgang offen | Aktuelle Programme, aber alter Kernel | Vermutlich langsam, Grafiktreiber fehlen |

Beim Surfen ist der Browser das größte Einfallstor. Deshalb fällt die Wahl auf LineageOS (Android mit Linux-Kernel) und einen Browser, der noch Updates bekommt.

## Etappen

1. **Sichern:** Den kompletten Speicher mit mtkclient auslesen und die Variante (HD oder FHD) bestimmen. Dabei wird nichts verändert.
2. **Prüfen:** Welche LineageOS-Versionen gibt es für diese Variante wirklich, und welcher aktuelle Browser läuft darauf noch? Danach endgültig entscheiden.
3. **Installieren und abspecken:** Nur Browser und Werbeblocker, alles andere entfernen oder deaktivieren.
4. **Absichern:** Bildschirmsperre, Verschlüsselung, keine Google-Dienste, automatische Browser-Updates.

## Offene Punkte

- Die Firmware-Downloads von BQ sind vermutlich nicht mehr online. Die eigene Sicherung aus Etappe 1 ist deshalb die einzige Rückfallebene.
- Der Kernel des Tablets bekommt keine Sicherheitsupdates mehr. Das Tablet sollte deshalb nur im Heimnetz und nicht für Bankgeschäfte benutzt werden.
- Ob ein aktueller Browser die vorhandene Android-Version noch unterstützt, klärt Etappe 2.

## Inhalt dieses Repositorys

Anleitung, Skripte und Konfiguration. Kaum Programmcode.

## Was nicht ins Repository gehört

- Speicherabbilder des Tablets: Sie enthalten gerätespezifische Schlüssel, Seriennummern und eventuell persönliche Daten
- WLAN-Passwörter, PINs und Seriennummern
- Firmware-Dateien von BQ oder MediaTek (Urheberrecht)
