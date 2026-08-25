# Dierenartspraktijk De Korenwolf — website

Website van [Dierenartspraktijk De Korenwolf](http://www.dierenartspraktijkdekorenwolf.nl/)
in Berg en Terblijt (Zuid-Limburg). Vervangt de Dreamweaver/Spry-site uit 2013.

Statische HTML, CSS en een klein beetje JavaScript. Geen framework, geen
build-stap nodig om de site te draaien, geen CMS.

## Mappen

| Map | Wat |
|---|---|
| `site/` | **Dit is wat je uploadt.** De volledige site, klaar voor de webhosting. |
| `bron/` | Alleen de inhoud van elke pagina, zonder menu en voettekst. |
| `build.py` | Plakt `bron/` + menu + voettekst samen tot `site/`. |
| `build_preview.py` | Maakt `voorbeeld.html`: alle 12 pagina's in één bestand. |
| `origineel/` | Het oorspronkelijke logo, bewaard als bronmateriaal. |

## Aanpassen

```bash
# 1. pas de tekst aan in bron/<pagina>.html
# 2. bouw de site opnieuw
python3 build.py
# 3. upload de gewijzigde bestanden uit site/
```

Menu, voettekst, adres en telefoonnummer staan bovenin `build.py` en worden in
één keer op alle pagina's doorgevoerd.

## Uitgangspunten

- Werkt op telefoon, tablet en desktop.
- Lettertypes staan in `site/assets/fonts/` — geen verzoek naar Google, dus
  geen AVG-bezwaar.
- De Google-kaart op Contact laadt pas nadat de bezoeker daarop klikt.
- Openingstijden staan op drie plekken: de tabellen in `bron/index.html` en
  `bron/contact.html`, en het `ROOSTER` in `site/assets/js/site.js` (dat
  verzorgt de "nu open / nu gesloten"-melding).
- Bestandsnamen zijn gelijk aan de oude site, zodat bestaande links en
  zoekresultaten blijven werken.

## Verder lezen

**[LEES-MIJ.md](LEES-MIJ.md)** — uploadinstructies, wat er precies veranderd is,
en een lijst van teksten die nog bijgewerkt moeten worden.
