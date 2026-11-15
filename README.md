# M10 Surftablet

Ein altes BQ Aquaris M10 wird zu einem schlanken Surftablet für das Heimnetz. Der Schwerpunkt liegt auf Tempo und Sicherheit, mit möglichst wenigen Apps.

**Stand (15.11.2026):** Recherche abgeschlossen, Bestandsaufnahme am Gerät steht noch aus. Am Tablet wurde noch nichts verändert. Die nächsten Schritte und offenen Fragen stehen in der [Übergabe](CLAUDE.md).

## Zielgerät

| | |
|---|---|
| Gerät | BQ Aquaris M10 (10 Zoll), Variante HD oder FHD, noch zu bestimmen |
| Chip | MediaTek MT8163, 64-Bit ARM, 2 GB RAM, 16 GB Speicher |

### Bestandsaufnahme am Gerät

Noch offen. Das Tablet war bisher nicht per USB angeschlossen.

| Frage | Ergebnis |
|---|---|
| Startet das Tablet, Akkuzustand | offen |
| Variante | offen |
| System, Android-Version, Sicherheitspatch | offen |
| Bildschirmauflösung, RAM, freier Speicher | offen |
| Google-Konto eingerichtet | offen |
| Schalter „OEM-Entsperrung“ vorhanden | offen |

### Die Varianten und ihre Namen

Die Namen `cooler` und `frieza` gelten nur für die Ubuntu Edition. Unter Android, bei TWRP und bei LineageOS heißen die Geräte anders. Ein Build für die falsche Variante macht das Tablet unbrauchbar, bis die Originalfirmware wieder eingespielt ist.

| Variante | Auflösung | Name unter Android | Name unter Ubuntu | Letzte Originalfirmware |
|---|---|---|---|---|
| M10 HD | 1280 × 800 | `freezerhd` | `cooler` | Android 8.1.0 (3.0.4) |
| M10 FHD | 1920 × 1200 | `freezerfhd` | `frieza` | Android 6.0.1 (2.6.2) |
| M10 4G | 1280 × 800 | `freezerlte` (anderer Chip) | – | Android 6.0.1 (1.10.0) |

Am Gerät entscheiden `adb shell getprop ro.product.device` und `adb shell wm size`.

## Entscheidung: LineageOS statt klassischem Linux

| Weg | Aufwand | Sicherheit | Tempo |
|---|---|---|---|
| Ubuntu Touch 16.04 | Gering | Schlecht: der Browser ist jahrelang veraltet | Ordentlich |
| **LineageOS (inoffiziell) mit aktuellem Browser** | Mittel | Am besten, weil der Browser aktuell bleibt | Am besten, die Grafikbeschleunigung funktioniert |
| Eigene postmarketOS-Portierung | Sehr hoch, Ausgang offen | Aktuelle Programme, aber alter Kernel | Vermutlich langsam, Grafiktreiber fehlen |

Beim Surfen ist der Browser das größte Einfallstor. Deshalb fällt die Wahl auf ein Android mit Linux-Kernel und einen Browser, der noch Updates bekommt. Die Recherche unten schränkt diese Entscheidung ein: siehe [Empfehlung](#empfehlung).

## Recherche: Welche Builds gibt es?

Es gibt für beide Varianten genau eine LineageOS-Version: **15.1 (Android 8.1)**. Alle Builds stammen von einer einzelnen Person (GitHub-Konto `jmpfbmx`) im Projekt [bq-mtk](https://github.com/bq-mtk). Sie liegen als Release-Dateien bei GitHub, der Quellcode von Gerätebaum und Kernel liegt daneben.

| Variante | Datei | Datum | Downloads |
|---|---|---|---|
| FHD (`freezerfhd`) | `lineage-15.1-20210906-UNOFFICIAL-freezerfhd.zip` | 06.09.2021 | etwa 1500 |
| HD (`freezerhd`) | `lineage-15.1-20220113-UNOFFICIAL-freezerhd.zip` | 13.01.2022 | etwa 260 |

Was das für die Sicherheit bedeutet:

- **Die Builds sind vier bis fünf Jahre alt.** Seit Januar 2022 ist keiner mehr erschienen, die letzte Änderung am Kernel-Quellcode ist vom März 2023. Mit Updates ist nicht zu rechnen.
- **SELinux läuft nur im Modus „permissive“.** Beide Gerätebäume starten den Kernel mit `androidboot.selinux=permissive`. Damit protokolliert Android Regelverstöße nur, statt sie zu verhindern. Das ist eine wichtige Schutzschicht weniger als bei der Originalfirmware. Ein Zweig mit eingeschaltetem SELinux existiert im Quellcode, wurde aber nie als Build veröffentlicht.
- **Keine Prüfsummen und keine Fehlerlisten.** Die Releases nennen weder SHA-Summen noch bekannte Fehler. Ob Verschlüsselung funktioniert, ist nicht dokumentiert; das Wiederherstellungssystem OrangeFox desselben Autors kann verschlüsselte Daten nicht lesen.
- **Die eingebaute Web-Ansicht (WebView) ist auf dem Stand von 2021** und bekommt ohne Play Store keine Updates. Alles, was Webseiten anzeigt, muss deshalb über den separaten Browser laufen.
- Einen älteren LineageOS-15.1-Build für das FHD (Juli/August 2020, Forum HTCMania) gibt es ebenfalls; spätere Beiträge dort fragen nach der Datei, der Link ist vermutlich tot. Zweige für LineageOS 16 bis 18.1 liegen im Quellcode, daraus ist nie ein Build entstanden.

Die Originalfirmware aller Varianten ist entgegen der früheren Annahme wieder verfügbar: Das Projekt bq-mtk hat sie nach dem Ende der BQ-Webseite neu hochgeladen ([firmware_collection](https://github.com/bq-mtk/firmware_collection)), im Format für das SP Flash Tool. Für TWRP gibt es offizielle Seiten für alle drei Varianten.

Zum Entsperren nennen die Anleitungen: Schalter „OEM-Entsperrung“ in den Entwickleroptionen einschalten, dann `fastboot oem-unlock` und am Gerät mit „Lauter“ bestätigen. Dabei werden alle Daten gelöscht. Am eigenen Gerät ist das noch nicht geprüft.

## Recherche: Welcher Browser?

| Browser | Mindestversion Android | Auf Android 8.1 |
|---|---|---|
| **Firefox** | 8.0 (seit Firefox 144, Herbst 2025) | **bekommt Updates** |
| Chrome und die meisten Chromium-Ableger | 10 (seit Chrome 139, August 2025) | bleibt auf Chrome 138 stehen |
| Firefox auf Android 6.0.1 | – | bleibt auf Firefox 143 stehen |

Auf Android 8.1 ist **Firefox** der einzige große Browser mit laufenden Updates. Er bringt seine eigene Technik zum Darstellen von Webseiten mit und hängt nicht von der veralteten WebView ab. Der Werbeblocker uBlock Origin lässt sich als Erweiterung installieren. Firefox kommt ohne Play Store aufs Tablet, entweder als APK von Mozilla oder als Ableger (Fennec, IronFox) über F-Droid.

Das Risiko: Android 8 ist jetzt die unterste Stufe, die Mozilla unterstützt. Bei der nächsten Anhebung ist Schluss. Mozilla hat dafür noch kein Datum genannt.

Auf Android 6.0.1, der letzten Originalfirmware des FHD, läuft kein aktueller Browser mehr.

## Empfehlung

Der weitere Weg hängt von der Variante ab.

**Wenn es ein M10 HD ist:** Zuerst die Originalfirmware Android 8.1 (3.0.4) behalten oder einspielen, statt LineageOS zu installieren. Firefox läuft darauf genauso, SELinux bleibt eingeschaltet, die Verschlüsselung ist vom Hersteller getestet, und der Bootloader kann gesperrt bleiben. Die Google-Apps und der übrige Ballast lassen sich per `adb` deaktivieren, ohne das System zu verändern. LineageOS brächte hier keine neuere Android-Version, sondern nur ein schlankeres System, und kostet dafür SELinux und den gesperrten Bootloader.

**Wenn es ein M10 FHD ist:** LineageOS 15.1 ist der einzige Weg zu einem aktuellen Browser, weil die Originalfirmware bei Android 6.0.1 endet. Der Preis ist ein System von 2021 mit ausgeschaltetem SELinux und entsperrtem Bootloader. Für ein Tablet, das nur im Heimnetz surft und keine Konten, Passwörter oder Bankdaten enthält, ist das vertretbar, aber schlechter als erhofft. Diese Abwägung trifft der Besitzer, bevor irgendetwas geflasht wird.

In beiden Fällen gilt: nur Firefox mit uBlock Origin, keine Google-Konten, keine gespeicherten Passwörter für wichtige Dienste.

## Sicherungsplan

Vor jedem Schreibzugriff wird der komplette Speicher (16 GB) auf den PC ausgelesen. Die Originalfirmware gibt es zwar wieder im Netz, aber einige Bereiche gibt es nur auf diesem einen Gerät: `nvram`, `proinfo` und `protect1`/`protect2` enthalten WLAN- und Bluetooth-Adresse, Seriennummer und Kalibrierdaten. Gehen sie verloren, hilft keine Firmware aus dem Netz.

Ohne Root lässt sich über `adb` kein Speicherabbild ziehen. Es bleibt der USB-Notfallmodus des MediaTek-Chips, für den es zwei Werkzeuge gibt:

| | mtkclient (empfohlen) | SP Flash Tool |
|---|---|---|
| Herkunft | Quelloffen, [GitHub](https://github.com/bkerler/mtkclient) | Geschlossenes MediaTek-Programm, nur über inoffizielle Download-Seiten |
| Braucht | Python 3 (python.org), Treiber UsbDk, MediaTek-USB-Treiber | MediaTek-VCOM-Treiber, dafür unter Windows 11 die Treibersignaturprüfung abschalten; dazu die Scatter-Datei aus der Originalfirmware (etwa 1 GB Download) |
| Komplettabbild | Ein Befehl (`mtk rf flash.bin`), dazu `mtk rl` für einzelne Partitionen | „Readback“ mit von Hand eingetragenen Adressbereichen |
| MT8163 | Im Quellcode eingetragen (Konfiguration und Payload vorhanden) | Vom bq-mtk-Projekt als Standardweg beschrieben |

Empfohlen ist mtkclient: Alle Bestandteile kommen aus nachvollziehbaren Quellen, die Windows-Sicherheitsfunktionen bleiben eingeschaltet, und das Auslesen ist ein einziger Befehl. Das SP Flash Tool bleibt die Rückfallebene, falls mtkclient das Tablet nicht anspricht.

Ablauf, sobald der Besitzer den Installationen zugestimmt hat:

1. Python 3 von python.org, UsbDk und den MediaTek-USB-Treiber installieren, mtkclient in einen Ordner außerhalb des Repositorys laden.
2. Tablet ausschalten, `mtk rf` starten, Tablet mit gedrückter Lautstärketaste per USB anschließen. Das Auslesen von 16 GB dauert etwa eine halbe bis ganze Stunde.
3. Zusätzlich die Partitionen einzeln auslesen (`mtk rl`), damit `nvram`, `proinfo`, `protect1`, `protect2`, `preloader` und `lk` als eigene Dateien vorliegen.
4. Prüfsummen notieren und die Sicherung auf einen zweiten Datenträger kopieren. Sie enthält Seriennummer und eventuell persönliche Daten und gehört nicht ins Repository.

Auslesen verändert das Tablet nicht. Geschrieben wird erst nach ausdrücklicher Zustimmung.

## Etappen

1. **Bestandsaufnahme:** Variante und System per `adb` bestimmen. Verändert nichts.
2. **Sichern:** Den kompletten Speicher nach dem Sicherungsplan auslesen.
3. **Entscheiden:** Je nach Variante Originalfirmware 8.1 oder LineageOS 15.1, siehe Empfehlung.
4. **Installieren und abspecken:** Nur Firefox und Werbeblocker, alles andere entfernen oder deaktivieren.
5. **Absichern:** Bildschirmsperre, Verschlüsselung (falls sie funktioniert), keine Google-Dienste, automatische Browser-Updates.

## Offene Punkte

- Die Bestandsaufnahme am Gerät fehlt noch vollständig.
- Welchen Stand der Sicherheitspatches die LineageOS-Builds haben und ob die Verschlüsselung darin funktioniert, zeigt sich erst am installierten System.
- Die Forenbeiträge bei XDA und HTCMania ließen sich nicht automatisch abrufen; die Angaben daraus stammen aus Suchergebnissen.
- Der Kernel des Tablets (3.18) bekommt keine Sicherheitsupdates mehr. Das Tablet sollte deshalb nur im Heimnetz und nicht für Bankgeschäfte benutzt werden.

## Quellen

Abgerufen am 15.11.2026.

- LineageOS-Builds: [bq-mtk/ota_releases](https://github.com/bq-mtk/ota_releases/releases)
- Gerätebäume mit der SELinux-Einstellung: [mt8163-common](https://github.com/bq-mtk/android_device_bq_mt8163-common/blob/lineage-15.1/BoardConfigCommon.mk), [freezerhd](https://github.com/bq-mtk/android_device_bq_freezerhd/blob/lineage-15.1/BoardConfig.mk), [freezerfhd](https://github.com/bq-mtk/android_device_bq_freezerfhd)
- Originalfirmware: [bq-mtk/firmware_collection](https://github.com/bq-mtk/firmware_collection)
- Älterer FHD-Build: [HTCMania](https://www.htcmania.com/showthread.php?t=1560183), [XDA](https://xdaforums.com/t/cyanogenmod-for-bq-aquaris-m10-fhd-freezerfhd.3977457/)
- TWRP: [M10 HD](https://twrp.me/bq/bqaquarism10.html), [M10 FHD](https://twrp.me/bq/bqaquarism10fhd.html); Entsperren: [XDA-Anleitung](https://xdaforums.com/t/guide-bq-aquaris-m10-freezerhd-twrp-root.3523833/)
- Firefox ab Android 8.0: [Mozilla-Blog](https://blog.mozilla.org/futurereleases/2025/09/15/raising-the-minimum-android-version-for-firefox/), [Mozilla-Hilfe](https://support.mozilla.org/en-US/kb/will-firefox-work-my-mobile-device)
- Chrome ab Android 10: [heise online](https://heise.de/-10457380)
- mtkclient: [bkerler/mtkclient](https://github.com/bkerler/mtkclient), MT8163 in [`brom_config.py`](https://github.com/bkerler/mtkclient/blob/main/mtkclient/config/brom_config.py)

## Inhalt dieses Repositorys

Anleitung, Skripte und Konfiguration. Kaum Programmcode.

## Was nicht ins Repository gehört

- Speicherabbilder des Tablets: Sie enthalten gerätespezifische Schlüssel, Seriennummern und eventuell persönliche Daten
- WLAN-Passwörter, PINs und Seriennummern
- Firmware-Dateien von BQ oder MediaTek (Urheberrecht)
