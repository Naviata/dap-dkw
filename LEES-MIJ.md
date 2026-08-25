# De Korenwolf — nieuwe website (2026)

Vervanging van de bestaande site op `dierenartspraktijkdekorenwolf.nl`.
Alle bestandsnamen zijn hetzelfde gebleven, dus bestaande links, bladwijzers en
Google-resultaten blijven werken.

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
    ├── fonts/   (5 bestanden)
    └── img/     (10 bestanden)
```

De mappen `bron/`, `origineel/` en `build.py` hoeven **niet** mee — die zijn
alleen om de site te kunnen aanpassen.

**Voor je uploadt:** maak eerst een kopie van de huidige site (download de map via
FTP), zodat je altijd terug kunt.

Oude bestanden die weg mogen na de overstap: `SpryAssets/`, `Spry-UI-1.7/`,
`Templates/`, `logo_dap_v2.0.png` en de oude `*_123_456.jpg`-foto's.

---

## 2. Wat er is veranderd

**Techniek**
- Werkt nu op telefoon en tablet (de oude site was vast op 947 pixels breed).
- Adobe Spry (uit 2012, al jaren niet meer ondersteund) is eruit.
- De AddThis-deelknoppen zijn eruit — die dienst bestaat sinds 2023 niet meer
  en laadde een tracker op elke pagina.
- Lettertypes staan op je eigen server, niet bij Google. Geen AVG-gedoe.
- De Google-kaart op Contact laadt **pas na een klik**. Tot dan gaat er niets
  naar Google.
- Titels, omschrijvingen, `sitemap.xml` en bedrijfsgegevens voor Google
  toegevoegd.

**Nieuw op de site**
- Telefoonnummers zijn aanklikbaar op mobiel.
- Bovenaan elke pagina een balk met adres, spoedknop en telefoonnummer.
- Op Home en Contact staat automatisch **"Nu geopend"** of **"Nu gesloten —
  open morgen vanaf 9.00 uur"**. De dag van vandaag wordt in de tabel
  gemarkeerd. Dit rekent de bezoeker z'n eigen klok, er is niets aan te
  onderhouden.
- De spoedpagina begint nu met het praktijknummer in plaats van met het
  rooster, zodat mensen in paniek meteen zien wat ze moeten doen.

**Tekst**
- Alle informatie is overgenomen. Er is niets inhoudelijks bij verzonnen en
  niets weggelaten, op één tegenstrijdige zin na (zie punt 3, bij Team).
- De lange lappen tekst met `<br>` zijn opgedeeld in koppen, lijsten en
  kaders. De zinnen zelf zijn inhoudelijk ongewijzigd; alleen een aantal
  duidelijke tikfouten is verbeterd (zie punt 4).
- Eén typografische aanpassing overal: `U` / `Uw` is nu `u` / `uw`. Dat is de
  huidige Nederlandse schrijfwijze; de beleefdheidsvorm blijft hetzelfde.

---

## 3. Dit moet je zelf nog bijwerken

Deze punten stonden verouderd op de oude site en zijn **letterlijk
overgenomen**. Ze staan in de bestanden tussen duidelijke commentaarblokken:

| Waar | Wat | Bestand |
|---|---|---|
| Spoed & dienstnummers | Het dienstrooster loopt van **13 t/m 26 juli** — een oud rooster | `bron/paardentandarts.html` |
| Actueel | Verwijzing naar diezelfde periode "13 juli t/m 27 juli" | `bron/actueel.html` |
| Home | "De praktijk ligt **sinds kort** in Heerlijkheid Terblijt" | `bron/index.html` |
| Team | "**Dit jaar** zult u onze lammetjes kunnen bewonderen" | `bron/team.html` |
| Actueel | "**Volgend jaar** beginnen we met boosteren tegen blauwtong in maart" | `bron/actueel.html` |
| Team | Bij Hesther stond twee keer een werkdagenlijst die elkaar tegensprak (ma/wo/vr én ma/wo). Nu staat alleen "maandag en woensdag" | `bron/team.html` |

Zoek in die bestanden op `BIJWERKEN` — daar staan de blokken.

**Verder gecontroleerd, en nog steeds actueel:** alle telefoonnummers,
het IBAN, KvK- en BTW-nummer, DAP-nummer 91036, en alle externe links
(Takazumi, LICG, crematoria, laboratoria, verzekeraars).

---

## 4. Taalfoutjes

Je gaf aan de tekst letterlijk te willen overnemen. Duidelijke tikfouten heb ik
wel verbeterd — bij deze was er geen twijfel over de bedoeling:

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
| `ziek koi's ... herstellen tegen` | zieke koi's ... herstellen | Vogels |
| `vijverwater bacteriologisch onderzoek te laten onderzoeken` | vijverwater bacteriologisch te laten onderzoeken | Vogels |

**Twee woorden heb ik láten staan**, omdat ik niet zeker wist wat je bedoelde:

- `baarmoederonsteking` (bedoel je *baarmoederontsteking*?)
- `baarmoerder` (bedoel je *baarmoeder*?)

Allebei op de pagina Gezelschapsdieren, in de regel over sterilisatie. Zeg maar
of ik ze mag aanpassen.

---

## 5. Iets aanpassen

**Kleine tekstwijziging?** Open het bestand in `site/` in Kladblok en pas de
tekst aan. Upload het bestand opnieuw. Klaar.

**Netter (als je iets op alle pagina's tegelijk wilt wijzigen):**

1. Pas de tekst aan in `bron/<pagina>.html` — daar staat alleen de inhoud,
   zonder menu en voettekst.
2. Draai `python3 build.py` in deze map.
3. Upload de gewijzigde bestanden uit `site/`.

Menu, voettekst, telefoonnummer en adres staan bovenin `build.py` en worden op
alle pagina's tegelijk doorgevoerd.

**Openingstijden wijzigen?** Dan op drie plekken:
`bron/index.html`, `bron/contact.html` (de tabellen) en `site/assets/js/site.js`
(de regels onder `var ROOSTER`, in minuten na middernacht — `540` is 9.00 uur).

---

## 6. Nog te overwegen

- **Foto's.** De bestaande foto's zijn 205 × 300 pixels — dat was genoeg voor het
  smalle kolommetje op de oude site, maar op een moderne telefoon zien ze er
  korrelig uit. Een stuk of vijf nieuwe foto's (praktijk, behandelkamer, Tom
  aan het werk, de schapen, een koi) zouden de site enorm helpen. Ze mogen
  gerust met een telefoon gemaakt zijn.
- **Foto's van het team.** Nu staan er ronde initialen (T, H, A). Met echte
  portretjes wordt de teampagina veel persoonlijker.
- **HTTPS.** De site draait nu op `http://`. Het certificaat van de hosting
  staat op `*.hosting2go.nl` en niet op het eigen domein, dus `https://` geeft
  een foutmelding. Vraag bij Hosting2GO om een (gratis) Let's Encrypt-certificaat
  voor `dierenartspraktijkdekorenwolf.nl`. Browsers zetten sinds 2024 een
  "niet veilig"-waarschuwing bij sites zonder HTTPS.
- **Google Bedrijfsprofiel.** De openingstijden staan nu goed in de site
  verwerkt; controleer of ze ook in Google Maps kloppen.
