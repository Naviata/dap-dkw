#!/usr/bin/env python3
"""
Bouwt de statische site van Dierenartspraktijk De Korenwolf.

Gebruik:  python3 build.py
Leest:    bron/<slug>.html   (alleen de inhoud van de pagina)
Schrijft: site/<slug>.html   (complete pagina met banner, menu en voettekst)

De map site/ is wat je naar de webhosting uploadt.
"""

import os

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.join(HIER, 'bron')
UIT = os.path.join(HIER, 'site')

# ---------------------------------------------------------------- gegevens
PRAKTIJK = {
    'naam': 'Dierenartspraktijk de Korenwolf',
    'straat': 'Lindenstraat 8',
    'postcode': '6325 PB',
    'plaats': 'Berg en Terblijt',
    'tel': '06-455 60 220',
    'tel_link': '+31645560220',
    'email': 'dapdekorenwolf@hotmail.com',
    'kvk': '14126029',
    'btw': 'NL001838190B04',
    'dapnr': '91036',
}

MAPS_EMBED = (
    'https://maps.google.com/maps?width=100%25&amp;height=380&amp;hl=nl'
    '&amp;q=Lindenstraat%208,%206325%20PB%20Berg%20en%20Terblijt'
    '&amp;t=&amp;z=16&amp;ie=UTF8&amp;iwloc=B&amp;output=embed'
)
MAPS_LINK = ('https://www.google.com/maps/search/?api=1'
             '&amp;query=Lindenstraat+8+6325+PB+Berg+en+Terblijt')

# ---------------------------------------------------------------- menu
# Namen exact zoals op de oorspronkelijke site.
NAV = [
    ('index.html', 'Home', None),
    ('contact.html', 'Contact &amp; Openingstijden', None),
    ('team.html', 'Team', None),
    ('actueel.html', 'Actueel', None),
    ('#diersoorten', 'Diersoorten', [
        ('gezelschapsdieren.html', 'Gezelschapsdieren'),
        ('landbouwhuisdieren.html', 'Landbouwhuisdieren'),
        ('vogels.html', 'Vogels &amp; Koikarpers'),
    ]),
    ('kittenopvang.html', 'Kittenopvang', None),
    ('paardentandarts.html', 'Dienst-Spoednummers', None),
    ('#diversen', 'Diversen', [
        ('verzekering.html', 'Verzekering'),
        ('links.html', 'Links'),
    ]),
    ('voorwaarden.html', 'Voorwaarden', None),
]

# slug: (titel in <title>, kop boven de tekst, meta description)
PAGINAS = {
    'index': (
        'Dierenartspraktijk De Korenwolf | Berg en Terblijt',
        'Welkom bij Dierenartspraktijk De Korenwolf!',
        'Dierenartspraktijk De Korenwolf in Berg en Terblijt. Voor gezelschapsdieren, '
        'kleine herkauwers, hobbyvarkens, vogels en koikarpers. Bel 06-455 60 220.'),
    'contact': (
        'Contact &amp; Openingstijden',
        'Contact &amp; Openingstijden',
        'Adres, telefoonnummer, e-mail en openingstijden van Dierenartspraktijk De Korenwolf '
        'aan de Lindenstraat 8 in Berg en Terblijt.'),
    'team': (
        'Team',
        'Team',
        'Maak kennis met dierenarts Tom en de dierenartsassistentes Hesther en Anouk van '
        'Dierenartspraktijk De Korenwolf.'),
    'actueel': (
        'Actueel',
        'Actueel',
        'Actuele mededelingen van Dierenartspraktijk De Korenwolf: nieuwe klanten, '
        'vaccinaties, assortiment en beoordeling op foto.'),
    'gezelschapsdieren': (
        'Gezelschapsdieren',
        'Gezelschapsdieren',
        'Behandelingen, operaties, vaccinaties, onderzoek en dieetvoeding voor hond, kat en '
        'konijn bij Dierenartspraktijk De Korenwolf.'),
    'landbouwhuisdieren': (
        'Landbouwhuisdieren',
        'Landbouwhuisdieren o.a. kleine herkauwers (:schaap, geit, alpaca e.d.) en hobby-varken',
        'Dierenarts voor schapen, geiten, alpacas en hobbyvarkens in Zuid-Limburg. '
        'DAP-nummer 91036.'),
    'vogels': (
        'Vogels &amp; Koikarpers',
        'Vogels, koikarpers, goudvissen e.d.',
        'Onderzoek en behandeling van vogels, pluimvee, koikarpers en goudvissen. '
        'Officieel dealer van Takazumi.'),
    'kittenopvang': (
        'Kittenopvang',
        'Kittenopvang',
        'Kittenbemiddeling bij Dierenartspraktijk De Korenwolf. Geef uw voorkeur voor '
        'geslacht en kleur door.'),
    'paardentandarts': (
        'Dienst-Spoednummers',
        'Dienstverband-spoednummers',
        'Spoednummers en avonddienst van Dierenartspraktijk De Korenwolf en de aangesloten '
        'praktijken in Zuid-Limburg.'),
    'verzekering': (
        'Verzekering',
        'Huisdierverzekering',
        'Informatie over huisdierverzekeringen voor hond en kat: Ohra, Figopet en Petsecur.'),
    'links': (
        'Links',
        'Links',
        'Handige links: dierencrematoria, chipregistratie, laboratoria en '
        'vijverbenodigdheden in Limburg.'),
    'voorwaarden': (
        'Voorwaarden',
        'Voorwaarden',
        'Voorwaarden van Dierenartspraktijk De Korenwolf: operatie, ruilen van producten, '
        'betaling en betalingscondities.'),
}

# foto rechts naast de tekst, zoals in de oude zijkolom
FOTOS = {
    'index': ('praktijk-ingang.jpg', 'De ingang van de praktijk aan de Lindenstraat 8.'),
    'contact': ('praktijk-ingang.jpg', 'De ingang aan de Lindenstraat 8.'),
    'team': ('praktijk-tuin.jpg', ''),
    'actueel': ('actueel.jpg', ''),
    'gezelschapsdieren': ('katten.jpg', ''),
    'landbouwhuisdieren': ('schapen.jpg', ''),
    'vogels': ('koi.jpg', ''),
    'kittenopvang': ('kittens.jpg', ''),
    'paardentandarts': ('spoed.jpg', ''),
    'verzekering': ('verzekering.jpg', ''),
    'links': ('links.jpg', ''),
    'voorwaarden': ('voorwaarden.jpg', ''),
}

BEDRIJF_JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VeterinaryCare",
  "name": "Dierenartspraktijk De Korenwolf",
  "url": "https://www.dierenartspraktijkdekorenwolf.nl/",
  "telephone": "+31645560220",
  "email": "dapdekorenwolf@hotmail.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Lindenstraat 8",
    "postalCode": "6325 PB",
    "addressLocality": "Berg en Terblijt",
    "addressCountry": "NL"
  },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Friday"], "opens": "09:00", "closes": "12:00" },
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Friday"], "opens": "12:30", "closes": "18:00" },
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Tuesday","Wednesday","Thursday"], "opens": "09:00", "closes": "12:00" },
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Tuesday","Wednesday","Thursday"], "opens": "12:30", "closes": "17:00" }
  ]
}
</script>
"""

SJABLOON = """<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{omschrijving}">
<meta name="theme-color" content="#2C6CB0">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/img/favicon-64.png" sizes="64x64" type="image/png">
<link rel="apple-touch-icon" href="assets/img/korenwolf-mark-180.png">
<link rel="canonical" href="https://www.dierenartspraktijkdekorenwolf.nl/{slug}.html">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="Dierenartspraktijk De Korenwolf">
<meta property="og:title" content="{titel}">
<meta property="og:description" content="{omschrijving}">
<meta property="og:url" content="https://www.dierenartspraktijkdekorenwolf.nl/{slug}.html">
<link rel="preload" href="assets/fonts/sourcesans3-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/stijl.css">
{extra_head}</head>
<body>
{kop}
<div class="inhoud" id="inhoud">
<div class="tekst">
<h1 class="paginatitel">{h1}</h1>
{inhoud}
</div>
{foto}
</div>
{voet}
</body>
</html>
"""


def menu_html(actief):
    """Bouwt de menubalk en markeert de actieve pagina."""
    r = ['<nav class="menubalk" aria-label="Hoofdmenu">',
         '<button type="button" class="menuknop" aria-expanded="false" '
         'aria-controls="menu">Menu</button>',
         '<ul id="menu">']
    for href, label, sub in NAV:
        if sub:
            sleutel = href.lstrip('#')
            r.append('<li class="heeft-sub">')
            r.append('<button type="button" class="uitklap" aria-expanded="false" '
                     'aria-controls="sub-%s">%s</button>' % (sleutel, label))
            r.append('<ul class="submenu" id="sub-%s">' % sleutel)
            for shref, slabel in sub:
                cur = ' aria-current="page"' if shref == actief else ''
                r.append('<li><a href="%s"%s>%s</a></li>' % (shref, cur, slabel))
            r.append('</ul></li>')
        else:
            cur = ' aria-current="page"' if href == actief else ''
            r.append('<li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    r.append('</ul></nav>')
    return '\n'.join(r)


def kop_html(slug):
    """Logobanner plus menubalk, zoals bovenaan de oorspronkelijke site."""
    return """<a class="overslaan" href="#inhoud">Naar de inhoud</a>
<div class="blad">

<div class="banner">
  <a href="index.html">
    <img src="assets/img/logo.png" width="946" height="281"
         alt="Dierenartspraktijk De Korenwolf">
  </a>
</div>

%s
""" % menu_html(slug + '.html')


def voet_html():
    return """
<footer class="voet">
  <div class="binnen">
    <p>{straat}, {postcode} {plaats} &middot;
       <a href="tel:{tel_link}">{tel}</a> &middot;
       <a href="mailto:{email}">{email}</a></p>
    <p>{naam} &middot; &copy; <span id="jaar">2026</span></p>
  </div>
</footer>

</div><!-- /blad -->

<script src="assets/js/site.js" defer></script>
<script>document.getElementById('jaar').textContent = new Date().getFullYear();</script>
""".format(**PRAKTIJK)


def foto_html(slug):
    if slug not in FOTOS:
        return ''
    bestand, bijschrift = FOTOS[slug]
    onder = '\n    <figcaption>%s</figcaption>' % bijschrift if bijschrift else ''
    return ('<div class="fotokolom">\n  <figure>\n'
            '    <img class="foto" src="assets/img/%s" width="205" height="300"\n'
            '         loading="lazy" alt="%s">%s\n  </figure>\n</div>'
            % (bestand, bijschrift, onder))


def bouw():
    gebouwd = []
    for slug, (titel, h1, omschrijving) in PAGINAS.items():
        pad = os.path.join(BRON, slug + '.html')
        if not os.path.exists(pad):
            print('  ontbreekt: bron/%s.html' % slug)
            continue
        with open(pad, encoding='utf-8') as f:
            inhoud = f.read()

        inhoud = (inhoud
                  .replace('{{TEL}}', PRAKTIJK['tel'])
                  .replace('{{TEL_LINK}}', PRAKTIJK['tel_link'])
                  .replace('{{EMAIL}}', PRAKTIJK['email'])
                  .replace('{{MAPS_EMBED}}', MAPS_EMBED)
                  .replace('{{MAPS_LINK}}', MAPS_LINK))

        volle_titel = titel if slug == 'index' else titel + ' | Dierenartspraktijk De Korenwolf'
        html = SJABLOON.format(
            titel=volle_titel,
            omschrijving=omschrijving,
            slug=slug,
            h1=h1,
            extra_head=BEDRIJF_JSONLD if slug in ('index', 'contact') else '',
            kop=kop_html(slug),
            inhoud=inhoud.strip(),
            foto=foto_html(slug),
            voet=voet_html(),
        )
        with open(os.path.join(UIT, slug + '.html'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        gebouwd.append(slug)

    basis = 'https://www.dierenartspraktijkdekorenwolf.nl/'
    with open(os.path.join(UIT, 'robots.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n' % basis)
    urls = ''.join(
        '  <url><loc>%s%s.html</loc><priority>%s</priority></url>\n'
        % (basis, s, '1.0' if s == 'index' else '0.8') for s in gebouwd)
    with open(os.path.join(UIT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                '%s</urlset>\n' % urls)

    print('Gebouwd: %d paginas -> site/' % len(gebouwd))


if __name__ == '__main__':
    bouw()
