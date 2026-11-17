# Übergabe für die nächste Session

Stand 17.11.2026: LineageOS 15.1 ist als Versuch installiert (Bootloader entsperrt, alte Daten gelöscht), dazu F-Droid, Fennec mit uBlock Origin und vier Lesezeichen sowie KeePassDX. Am 17.11. wurden der Video-Chip (fehlende Herstellerbibliothek, Rechte auf `/dev/Vcodec`) und zram repariert; drei eigene Dateien liegen dafür in `/system`, siehe README unter „Tempo“. Ebenfalls am 17.11.: uBlock Origin neu installiert (war am 16.11. abends entfernt worden) und `/system/etc/hosts` durch die StevenBlack-Sperrliste ersetzt, siehe README unter „Werbung“. Einzelheiten stehen im [README](README.md) unter „Installation“. Die Fragen unter „Was noch niemand weiß“ sind beantwortet.

Nächste Schritte: Der Besitzer legt in KeePassDX seine Datenbank an; dann Bildschirmsperre setzen, Root-Zugriff und Android-Debugging abschalten. Nach jedem Neustart läuft `adb` wieder ohne Root; `adb root` geht nur, solange in den Entwickleroptionen „Root-Zugriff: Nur ADB“ eingestellt ist. Solange das Debugging an ist, funktioniert `adb` ohne Bestätigung am Gerät (`ro.adb.secure=0`); Fennec lässt sich so per `input tap` und `screencap` fernsteuern. Taugt LineageOS dem Besitzer nicht, kauft er ein Neugerät.

Sicherung und Werkzeug liegen außerhalb des Repositorys:

- `C:\Education\m10-sicherung`: Komplettabbild, Einzelpartitionen, `SHA256SUMS.txt`
- `C:\Education\m10-werkzeug`: mtkclient mit den Anpassungen aus `werkzeug/mtkclient-m10.patch`, eigene Python-Umgebung `venv`

mtkclient immer mit `--serialport` aufrufen, ab dem zweiten Befehl einer Sitzung mit `M10_RESUME=2`. Einzelheiten und Stolpersteine stehen im README unter „Sicherung“.

## Was feststeht

- **Ziel:** Das BQ Aquaris M10 wird ein Surftablet für das Heimnetz. Schwerpunkt Tempo und Sicherheit, möglichst wenige Apps.
- **Weg:** LineageOS (inoffiziell) mit einem Browser, der noch Updates bekommt. Der Besitzer hat diesem Weg zugestimmt, obwohl es Android und kein klassisches Linux ist.
- **Repository:** öffentlich. Speicherabbilder, Firmware, Passwörter und Seriennummern kommen nicht hinein (siehe `.gitignore`).

## Was noch niemand weiß

Diese Fragen zuerst klären, am Gerät und nicht aus dem Gedächtnis:

1. Startet das Tablet überhaupt, und hält der Akku?
2. Welche Variante ist es: HD (unter Android `freezerhd`, unter Ubuntu `cooler`, 1280 × 800) oder FHD (`freezerfhd` bzw. `frieza`, 1920 × 1200)? Auf der Rückseite steht nur „Aquaris M10“.
3. Welches System läuft: Android (welche Version) oder die Ubuntu Edition?
4. Lässt sich USB-Debugging einschalten, und erkennt `adb` das Gerät?
5. Lässt sich der Bootloader entsperren (`fastboot oem unlock` oder Schalter „OEM-Entsperrung“)?
6. Welche LineageOS-Versionen gibt es für genau diese Variante, wie alt sind sie, und wie vertrauenswürdig ist die Quelle?
7. Welcher aktuelle Browser unterstützt die Android-Version dieses LineageOS noch?

Erst nach Punkt 6 und 7 steht fest, ob der LineageOS-Weg wirklich die bessere Wahl ist. Wenn es nur sehr alte oder zweifelhafte Builds gibt, die Entscheidung mit dem Besitzer neu besprechen.

## Reihenfolge

1. **Bestandsaufnahme** (verändert nichts): Fragen 1 bis 5 beantworten, Ergebnis ins README schreiben.
2. **Sichern:** Den kompletten Speicher auslesen, bevor irgendetwas geschrieben wird. Die Firmware-Downloads von BQ sind vermutlich nicht mehr online, die eigene Sicherung ist dann die einzige Rückfallebene. Die Sicherung gehört auf den PC, nicht ins Repository.
3. **Recherche:** Fragen 6 und 7. Quellen im README festhalten.
4. **Entscheidung** mit dem Besitzer, dann installieren und abspecken.
5. **Absichern:** Bildschirmsperre, Verschlüsselung, keine Google-Dienste, automatische Browser-Updates.

Vor jedem Schritt, der auf das Tablet schreibt (Bootloader entsperren, flashen), den Besitzer fragen. Entsperren löscht alle Daten.

## Werkzeuge auf dem Entwicklungsrechner (Windows)

Vom Schwesterprojekt [tierfon](https://github.com/KungFuBrot/tierfon) ist schon vorhanden:

| Was | Wo |
|---|---|
| `adb`, `fastboot` | `%LOCALAPPDATA%\Android\Sdk\platform-tools` (nicht im `PATH`) |
| JDK 17 | `%LOCALAPPDATA%\Programs\Temurin17\jdk-17.0.21+9` |
| Git Bash, Node 24, WSL | installiert |

Es fehlt: **Python**. Das Sicherungswerkzeug `mtkclient` für MediaTek-Geräte braucht Python und einen USB-Treiber. Alternative ist das SP Flash Tool mit einer passenden Scatter-Datei. Downloads und Treiberinstallationen vorher mit dem Besitzer abstimmen.

## Hinweise zum Gerät

- Chip: MediaTek MT8163 (64-Bit ARM). Der Startcode im Chip hat einen USB-Notfallmodus; darüber lässt sich das Tablet auch dann wiederherstellen, wenn der Bootloader beschädigt ist. Das setzt die eigene Sicherung voraus.
- Auf der Rückseite sind Modellname und Seriennummer eingeprägt. Die Seriennummer gehört nicht ins Repository.
- Der Kernel des Tablets bekommt keine Sicherheitsupdates mehr. Das Tablet ist deshalb nur für das Heimnetz gedacht und nicht für Bankgeschäfte.

## Erfahrungen aus dem Schwesterprojekt

- `adb` zeigt „offline“: am Gerät die USB-Debugging-Autorisierungen widerrufen, Debugging aus- und einschalten, Kabel neu stecken, Abfrage bestätigen.
- Mehrzeilige Dateiänderungen in Git Bash als Node-Skript in eine Datei schreiben, nicht als Heredoc.
- Auf Android-Geräten fehlt oft `awk`; Ausgaben von `adb shell` auf dem PC auswerten.
- Commits in diesem Repository laufen unter `KungFuBrot@users.noreply.github.com`, damit keine private E-Mail-Adresse öffentlich wird.
