# Dierenartspraktijk De Korenwolf — website

Website van [Dierenartspraktijk De Korenwolf](http://www.dierenartspraktijkdekorenwolf.nl/)
in Berg en Terblijt (Zuid-Limburg).

Een opfrisbeurt van de Dreamweaver/Spry-site uit 2013: dezelfde opzet en
dezelfde indeling, maar responsive, beter leesbaar en zonder verouderde
techniek. Statische HTML en CSS met een klein beetje JavaScript voor het menu.
Geen framework, geen CMS, geen build-stap nodig om de site te draaien.

## Mappen

| Map | Wat |
|---|---|
| `site/` | **Dit is wat je uploadt.** De volledige site, klaar voor de webhosting. |
| `bron/` | Alleen de inhoud van elke pagina, zonder banner, menu en voettekst. |
| `build.py` | Plakt `bron/` + banner + menu + voettekst samen tot `site/`. |
| `build_preview.py` | Maakt `voorbeeld.html`: alle 12 pagina's in één bestand. |
| `origineel/` | Het oorspronkelijke logo, bewaard als bronmateriaal. |

## Aanpassen

```bash
# 1. pas de tekst aan in bron/<pagina>.html
# 2. bouw de site opnieuw
python3 build.py
# 3. upload de gewijzigde bestanden uit site/
```

Menu, voettekst, adres, telefoonnummer en de foto per pagina staan bovenin
`build.py` en worden in één keer op alle pagina's doorgevoerd.

## Opzet

```
logobanner
──────────────────────────────────────
blauwe menubalk (uitklapmenu op telefoon)
──────────────────────────────────────
tekst                    │  foto
──────────────────────────────────────
voettekst
```

- Het blauw van het logo (`#558ED5`) voor balken, randen en lijnen; een iets
  diepere tint (`#2C6CB0`) waar tekst erop staat, vanwege het contrast.
- Eén lettertype, Source Sans 3, in `site/assets/fonts/` — geen verzoek naar
  Google, dus geen AVG-bezwaar.
- Bestandsnamen zijn gelijk aan de oude site, zodat bestaande links en
  zoekresultaten blijven werken. `paardentandarts.html` is dus nog steeds de
  pagina met de spoednummers.

## Verder lezen

**[LEES-MIJ.md](LEES-MIJ.md)** — uploadinstructies, wat er precies veranderd is,
en een lijst van teksten die nog bijgewerkt moeten worden.
