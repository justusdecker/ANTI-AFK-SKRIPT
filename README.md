# Python Anti-AFK Skript 🛡️

> [!CAUTION]
> Aktuell ist die Readme noch im Aufbau!

Ein kleines, rein terminal-basiertes Anti-AFK-Tool, geschrieben in Python. Es wurde speziell für Windows entwickelt, simuliert das simple Tastendrücken, um Inaktivitäts-Timeouts zu verhindern, bietet akustisches Feedback.

# ⚙️ Hauptfunktionen
* 100% Terminal-basiert: Kein grafischer Schnickschnack, übersichtliches textbasiertes Dashboard.
* **Anti-Erkennungs-Mechanismus**: Nutzt zufällige Verzögerungen (random.randint), um starre, wiederkehrende Muster zu vermeiden.
* **Akustisches Feedback**: Nutzt Windows-Systemtöne (win32api.Beep), um Statusänderungen (Start, Beenden) zu signalisieren.
* **Multithreading**: Läuft dank threading.Thread im Hintergrund, sodass das Terminal für Eingaben oder Überwachung frei bleibt.
* **Automatischer Update-Checker**: Fragt beim Start über requests.get eine Versionsdatei von einem Remoteserver (z. B. GitHub) ab und warnt dich im Terminal, falls eine neuere Version verfügbar ist.

# 🛠️ Voraussetzungen & Abhängigkeiten
Das Skript basiert auf folgenden Python-Modulen (von denen einige installiert werden müssen):
keyboard — Zur globalen Überwachung von Tastatureingaben/Tasten.

pywin32 (für win32api) — Für native Windows-Systembeeps.

requests — Zum Abrufen der aktuellen Versionsdaten aus dem Internet.
Installation
Stelle sicher, dass Python 3.x unter Windows installiert ist.

Installiere die benötigten Bibliotheken über das Terminal:

```bash
pip install keyboard requests pywin32
```
