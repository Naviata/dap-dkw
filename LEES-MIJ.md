# De Korenwolf — opgefriste website (2026)

Dezelfde site als die nu online staat, opgefrist en werkend op telefoon en
tablet. Alle bestandsnamen zijn hetzelfde gebleven, dus bestaande links,
bladwijzers en Google-resultaten blijven werken.

---

## 1. Uploaden

Upload **de inhoud van de map `site/`** naar de webruimte bij Hosting2GO
(de map waar nu `index.html` staat, meestal `httpdocs`, `public_html` of `www`).

```
site/
├── index.html, contact.html, team.html, …   (12 pagina's)
├── robots.txt, sitemap.xml
└── assets/
    ├── css/stijl.css
    ├── js/site.js
    ├── fonts/   (4 bestanden)
    └── img/     (15 bestanden)
```

De mappen `bron/`, `origineel/`, `build.py` en `build_preview.py` hoeven
**niet** mee — die zijn alleen om de site te kunnen aanpassen.

**Voor je uploadt:** maak eerst een kopie van de huidige site (download de map
via FTP), zodat je altijd terug kunt.

Oude bestanden die weg mogen na de overstap: `SpryAssets/`, `Spry-UI-1.7/`,
`Templates/` en de oude `*_123_456.jpg`-foto's. Het oude `logo_dap_v2.0.png`
mag blijven staan; de nieuwe site gebruikt hetzelfde logo onder de naam
`assets/img/logo.png`.

---

## 2. Wat er veranderd is

De opzet is met opzet hetzelfde gebleven: logobanner bovenaan, blauwe menubalk
eronder, tekst links met de foto rechts, grijze voettekst. Ook de menunamen en
de volgorde van de pagina's zijn ongewijzigd.

**Techniek**
- Werkt nu op telefoon en tablet. De oude site was vast op 947 pixels breed,
  waardoor je op een telefoon moest in- en uitzoomen.
- Op smalle schermen wordt de menubalk een uitklapmenu.
- Adobe Spry (uit 2012, al jaren niet meer ondersteund) is eruit; het menu is
  nu gewone CSS met een klein beetje JavaScript.
- De AddThis-deelknoppen zijn eruit — die dienst bestaat sinds 2023 niet meer
  en laadde een tracker op elke pagina.
- Het lettertype staat op je eigen server, niet bij Google. Geen AVG-gedoe.
- Titels, omschrijvingen, `sitemap.xml` en bedrijfsgegevens voor Google
  toegevoegd.

**Leesbaarheid**
- De tekst is van 12 pixels Verdana naar 17 pixels gegaan, met meer regelafstand
  en een beperkte regellengte.
- De lange lappen tekst met `<br>` erin zijn opgedeeld in koppen, alinea's,
  lijsten en tabellen. De zinnen zelf zijn inhoudelijk ongewijzigd.
- Telefoonnummers zijn aanklikbaar op mobiel.
- De drie echte waarschuwingen (narcose, spoednummer, betaling) staan in een
  kader zodat ze opvallen. Verder geen kaders of gekleurde vlakken.

**Kleur**
Het blauw van het logo (`#558ED5`) is aangehouden voor de menubalk, randen en
lijnen. Voor tekst óp die kleur is een iets diepere tint gebruikt (`#2C6CB0`),
omdat wit op het lichte blauw te weinig contrast geeft om comfortabel te lezen.

---

## 3. Dit moet je zelf nog bijwerken

Deze punten stonden verouderd op de oude site en zijn **letterlijk
overgenomen**. Ze staan in de bestanden tussen duidelijke commentaarblokken —
zoek op `BIJWERKEN`:

| Waar | Wat | Bestand |
|---|---|---|
| Dienst-Spoednummers | Het dienstrooster loopt van **13 t/m 26 juli** — een oud rooster | `bron/paardentandarts.html` |
| Actueel | Verwijzing naar diezelfde periode "13 juli t/m 27 juli" | `bron/actueel.html` |
| Home | "De praktijk ligt **sinds kort** in Heerlijkheid Terblijt" | `bron/index.html` |
| Team | "**Dit jaar** zult u onze lammetjes kunnen bewonderen" | `bron/team.html` |
| Actueel | "**Volgend jaar** beginnen we met boosteren tegen blauwtong in maart" | `bron/actueel.html` |
| Team | Bij Hesther stonden twee werkdagenlijsten die elkaar tegenspraken (ma/wo/vr én ma/wo). Nu staat er alleen "maandag en woensdag" | `bron/team.html` |

**Gecontroleerd en nog steeds actueel:** alle telefoonnummers, het IBAN, KvK- en
BTW-nummer, DAP-nummer 91036, en alle externe links (Takazumi, LICG,
crematoria, laboratoria, verzekeraars).

---

## 4. Taalfoutjes

Duidelijke tikfouten zijn verbeterd — bij deze was er geen twijfel over de
bedoeling:

| Oud | Nieuw | Pagina |
|---|---|---|
| `devolgende` | de volgende | Vogels, Landbouwhuisdieren |
| `fimpjes` | filmpjes | Actueel |
| `konijnenorene` | konijnenoren | Gezelschapsdieren |
| `draagalgprobleem` | draadalgprobleem | Vogels |
| `bourgonische` | bourgondische | Team |
| `laboraroria` | laboratoria | Vogels |
| `verrwijderd` | verwijderd | Gezelschapsdieren |
| `Dan betaald U` | dan betaalt u | Voorwaarden |
| `pathogenen bacteriën` | pathogene bacteriën | Vogels |
| `Er wordt samen gewerkt` | er wordt samengewerkt | Vogels |

Verder is `U` / `Uw` overal `u` / `uw` geworden. Dat is de huidige Nederlandse
schrijfwijze; de beleefdheidsvorm blijft hetzelfde.

**Twee woorden zijn blijven staan**, omdat niet zeker was wat bedoeld werd —
allebei op Gezelschapsdieren, in de regel over sterilisatie:

- `baarmoederonsteking` (bedoeld: *baarmoederontsteking*?)
- `baarmoerder` (bedoeld: *baarmoeder*?)

---

## 5. Iets aanpassen

**Kleine tekstwijziging?** Open het bestand in `site/` in Kladblok, pas de tekst
aan en upload het opnieuw. Klaar.

**Netter (als je iets op alle pagina's tegelijk wilt wijzigen):**

1. Pas de tekst aan in `bron/<pagina>.html` — daar staat alleen de inhoud,
   zonder banner, menu en voettekst.
2. Draai `python3 build.py` in deze map.
3. Upload de gewijzigde bestanden uit `site/`.

Menu, voettekst, adres, telefoonnummer en de foto per pagina staan bovenin
`build.py` en worden in één keer op alle pagina's doorgevoerd.

**Openingstijden wijzigen?** Alleen in `bron/contact.html`.

---

## 6. Nog te overwegen

- **Foto's.** De bestaande foto's zijn 205 × 300 pixels — genoeg voor het smalle
  kolommetje op de oude site, maar op een moderne telefoon zien ze er korrelig
  uit. Een stuk of vijf nieuwe foto's (praktijk, behandelkamer, Tom aan het
  werk, de schapen, een koi) zouden veel schelen. Ze mogen gerust met een
  telefoon gemaakt zijn.
- **HTTPS.** De site draait nu op `http://`. Het certificaat van de hosting
  staat op `*.hosting2go.nl` en niet op het eigen domein, dus `https://` geeft
  een foutmelding. Vraag bij Hosting2GO om een (gratis) Let's
  Encrypt-certificaat voor `dierenartspraktijkdekorenwolf.nl`. Browsers zetten
  sinds 2024 een "niet veilig"-waarschuwing bij sites zonder HTTPS.
- **Google-kaart en AVG.** De kaart op Contact laadt direct mee, net als op de
  oude site. Daarmee gaat er een verzoek naar Google zodra iemand de pagina
  opent. Wil je dat liever niet, dan kan de kaart pas na een klik laden — laat
  het weten.
- **Google Bedrijfsprofiel.** Controleer of de openingstijden daar ook kloppen.
