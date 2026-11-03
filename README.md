# Semestralni_projekt_py


## Plán práce

Síťové šachy v Pythonu: hra pro dva hráče po síti, celá v Pythonu (server kontroluje pravidla, klient v pygame).

### Cíl a rozsah

**Cíl:** funkční šachy pro dva hráče po síti s plnými pravidly a ukládáním partií.

**Součástí projektu:**
- jádro šachových pravidel (tahy, šach, mat, pat, rošáda, braní mimochodem, proměna pěšce),
- server (místnosti, ověřování tahů, ukládání partií do SQLite),
- grafický klient v pygame (šachovnice, lobby, síťová vrstva),
- automatické testy, dokumentace, uživatelská příručka.

**Mimo rozsah (pouze pokud zbyde čas):** šachové hodiny, uživatelské účty a žebříček, hra proti počítači.

### Architektura

```
chess/
  core/      # Board, tahy, pravidla, mat/pat (čistý Python, bez sítě)
  server/    # asyncio + websockets, místnosti, databáze
  client/    # pygame: šachovnice, lobby, síťová vrstva
  shared/    # formát zpráv (protokol), konstanty
  tests/     # pytest
```

Server je jediný zdroj pravdy: klient pošle jen žádost o tah, server ověří jeho legálnost, uloží ho a rozešle nový stav oběma hráčům.

### Milníky

| Milník | Obsah | Termín |
|---|---|---|
| M1 | Jádro pravidel s testy, hra pro dva hráče na jednom počítači | 29. 11. 2026 |
| M2 | Server a protokol, hra přes síť ve dvou oknech | 20. 12. 2026 |
| M3 | Lobby, ukládání partií, opětovné připojení | 3. 1. 2027 |
| M4 | Dokumentace, uživatelská příručka, závěrečná zpráva | 15. 1. 2027 |

### Týdenní plán

| Týden | Období | Práce | Výstup |
|---|---|---|---|
| 1–2 | 5. 10.–18. 10. | Volba technologií, návrh architektury a protokolu, kostra repozitáře | Struktura `chess/`, popis protokolu |
| 3 | 19. 10.–25. 10. | Datový model šachovnice, figurky, základní pohyby | `core`: Board a pohyby figur |
| 4 | 26. 10.–1. 11. | Legální tahy (král nesmí zůstat v šachu), detekce šachu | `core`: ověřování tahů |
| 5 | 2. 11.–8. 11. | Rošáda, braní mimochodem, proměna pěšce | `core`: speciální pravidla |
| 6 | 9. 11.–15. 11. | Mat, pat, remízy; testy pravidel (porovnání s `python-chess`) | `core` kompletní, sada testů |
| 7 | 16. 11.–22. 11. | Klient v pygame: šachovnice, figurky, výběr a zvýraznění tahů | Klient pro hru na jednom počítači |
| 8 | 23. 11.–29. 11. | Dokončení lokální hry, opravy | **M1** |
| 9 | 30. 11.–6. 12. | Server: websockets, místnosti, formát zpráv | Server s protokolem |
| 10 | 7. 12.–13. 12. | Síťová vrstva klienta (vlákno nebo asyncio a fronta událostí) | Hra přes síť ve dvou oknech |
| 11 | 14. 12.–20. 12. | Ověřování tahů na serveru, konec partie, chybové stavy | **M2** |
| 12–13 | 21. 12.–3. 1. | Lobby, ukládání partií do SQLite, opětovné připojení | **M3** |
| 14 | 4. 1.–10. 1. | Testování na dvou počítačích, opravy | Stabilní verze |
| 15 | 11. 1.–15. 1. | Dokumentace, uživatelská příručka, závěrečná zpráva | **M4** |

### Spuštění (příklad !!!!!!)

```bash
pip install -r requirements.txt
python -m server.main      # spustí server
python -m client.main      # spustí klienta
pytest                     # spustí testy
```