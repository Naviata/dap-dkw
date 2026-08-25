#!/usr/bin/env python3
"""
Bouwt de statische site van Dierenartspraktijk De Korenwolf.

Gebruik:  python3 build.py
Leest:    bron/<slug>.html   (alleen de inhoud van de pagina)
Schrijft: site/<slug>.html   (complete pagina met kop, menu en voettekst)

De map site/ is wat je naar de webhosting uploadt.
"""

import os
import re
import shutil

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.join(HIER, 'bron')
UIT = os.path.join(HIER, 'site')

# ---------------------------------------------------------------- gegevens
PRAKTIJK = {
    'naam': 'Dierenartspraktijk De Korenwolf',
    'kort': 'De Korenwolf',
    'straat': 'Lindenstraat 8',
    'postcode': '6325 PB',
    'plaats': 'Berg en Terblijt',
    'tel': '06-455 60 220',
    'tel_link': '+31645560220',
    'email': 'dapdekorenwolf@hotmail.com',
    'btw': 'NL001838190B04',
    'bank': 'NL58ABNA0447939211',
    'kvk': '14126029',
    'dapnr': '91036',
}

MAPS_EMBED = (
    'https://maps.google.com/maps?width=100%25&amp;height=420&amp;hl=nl'
    '&amp;q=Lindenstraat%208,%206325%20PB%20Berg%20en%20Terblijt'
    '&amp;t=&amp;z=16&amp;ie=UTF8&amp;iwloc=B&amp;output=embed'
)
MAPS_LINK = 'https://www.google.com/maps/search/?api=1&amp;query=Lindenstraat+8+6325+PB+Berg+en+Terblijt'

# ---------------------------------------------------------------- navigatie
NAV = [
    ('index.html', 'Home', None),
    ('contact.html', 'Contact', None),
    ('team.html', 'Team', None),
    ('actueel.html', 'Actueel', None),
    ('#diersoorten', 'Diersoorten', [
        ('gezelschapsdieren.html', 'Gezelschapsdieren', 'Hond, kat, konijn en knaagdier'),
        ('landbouwhuisdieren.html', 'Landbouwhuisdieren', 'Schaap, geit, alpaca, hobbyvarken'),
        ('vogels.html', 'Vogels &amp; koikarpers', 'Pluimvee, siervogels en vijvervissen'),
    ]),
    ('kittenopvang.html', 'Kittenopvang', None),
    ('paardentandarts.html', 'Spoed', None),
    ('#meer', 'Meer', [
        ('verzekering.html', 'Verzekering', 'Huisdierverzekeringen vergelijken'),
        ('links.html', 'Links', 'Crematoria, laboratoria en vijver'),
        ('voorwaarden.html', 'Voorwaarden', 'Betaling, ruilen en operaties'),
    ]),
]

# slug: (titel in <title>, h1, lead onder h1, meta description)
PAGINAS = {
    'index': (
        'Dierenartspraktijk De Korenwolf | Berg en Terblijt',
        None, None,
        'Dierenartspraktijk De Korenwolf in Berg en Terblijt. Voor gezelschapsdieren, '
        'kleine herkauwers, hobbyvarkens, vogels en koikarpers. Bel 06-455 60 220.'),
    'contact': (
        'Contact &amp; openingstijden',
        'Contact &amp; openingstijden',
        'Bel ons tijdens openingstijden of stuur een mail om een afspraak te maken. '
        'Geef bij een mail een aantal dagen en tijdstippen door waarop u langs kunt komen.',
        'Adres, telefoonnummer, e-mail en openingstijden van Dierenartspraktijk De Korenwolf '
        'aan de Lindenstraat 8 in Berg en Terblijt.'),
    'team': (
        'Ons team',
        'Ons team',
        'Een kleine praktijk met korte lijnen: u ziet steeds dezelfde vertrouwde gezichten.',
        'Maak kennis met dierenarts Tom en de dierenartsassistentes Hesther en Anouk van '
        'Dierenartspraktijk De Korenwolf.'),
    'actueel': (
        'Actueel',
        'Actueel',
        'Nieuws, mededelingen en praktische informatie over de praktijk.',
        'Actuele mededelingen van Dierenartspraktijk De Korenwolf: nieuwe klanten, '
        'vaccinaties, assortiment en beoordeling op foto.'),
    'gezelschapsdieren': (
        'Gezelschapsdieren',
        'Gezelschapsdieren',
        'Voor vrijwel alle zaken rond uw hond, kat, konijn of knaagdier kunt u bij ons terecht.',
        'Behandelingen, operaties, vaccinaties, onderzoek en dieetvoeding voor hond, kat en '
        'konijn bij Dierenartspraktijk De Korenwolf.'),
    'landbouwhuisdieren': (
        'Landbouwhuisdieren',
        'Landbouwhuisdieren',
        'Kleine herkauwers zoals schaap, geit en alpaca, en daarnaast het hobbyvarken.',
        'Dierenarts voor schapen, geiten, alpacas en hobbyvarkens in Zuid-Limburg. '
        'DAP-nummer 91036.'),
    'vogels': (
        'Vogels &amp; koikarpers',
        'Vogels, koikarpers en goudvissen',
        'Een dierenarts met een verleden in de pluimveegeneeskunde en een jarenlange liefde voor koi.',
        'Onderzoek en behandeling van vogels, pluimvee, koikarpers en goudvissen. '
        'Officieel dealer van Takazumi.'),
    'kittenopvang': (
        'Kittenopvang',
        'Kittenopvang',
        'Al sinds 2009 helpen wij kittens en moederpoezen aan een nieuw thuis.',
        'Kittenbemiddeling bij Dierenartspraktijk De Korenwolf. Geef uw voorkeur voor '
        'geslacht en kleur door.'),
    'paardentandarts': (
        'Spoed &amp; dienstnummers',
        'Spoed &amp; dienstnummers',
        'Bij spoed of een ernstig ziek huisdier belt u altijd eerst het gewone praktijknummer.',
        'Spoednummers en avonddienst van Dierenartspraktijk De Korenwolf en de aangesloten '
        'praktijken in Zuid-Limburg.'),
    'verzekering': (
        'Huisdierverzekering',
        'Huisdierverzekering',
        'Een verzekering kan de kosten van onverwachte behandelingen opvangen.',
        'Informatie over huisdierverzekeringen voor hond en kat: Ohra, Figopet en Petsecur.'),
    'links': (
        'Links',
        'Links',
        'Crematoria, laboratoria, registraties en adressen voor vijverbenodigdheden.',
        'Handige links: dierencrematoria, chipregistratie, laboratoria en '
        'vijverbenodigdheden in Limburg.'),
    'voorwaarden': (
        'Voorwaarden',
        'Voorwaarden',
        'Afspraken over operaties, het ruilen van producten en betaling.',
        'Voorwaarden van Dierenartspraktijk De Korenwolf: operatie, ruilen van producten, '
        'betaling en betalingscondities.'),
}

# ---------------------------------------------------------------- fragmenten
AAR_SVG = (
    '<svg viewBox="0 0 24 40" fill="none" stroke="currentColor" stroke-width="1.25" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 39V13"/>'
    '<path d="M12 31c-4.1 0-6.7-2.3-6.7-5.8 3.9-.4 6.7 1.7 6.7 5.8z" fill="currentColor" fill-opacity=".16"/>'
    '<path d="M12 31c4.1 0 6.7-2.3 6.7-5.8-3.9-.4-6.7 1.7-6.7 5.8z" fill="currentColor" fill-opacity=".16"/>'
    '<path d="M12 22.5c-3.6 0-5.9-2.1-5.9-5.2 3.5-.3 5.9 1.5 5.9 5.2z" fill="currentColor" fill-opacity=".16"/>'
    '<path d="M12 22.5c3.6 0 5.9-2.1 5.9-5.2-3.5-.3-5.9 1.5-5.9 5.2z" fill="currentColor" fill-opacity=".16"/>'
    '<path d="M12 14.5c-3 0-4.9-1.9-4.9-4.6 2.9-.3 4.9 1.3 4.9 4.6z" fill="currentColor" fill-opacity=".16"/>'
    '<path d="M12 14.5c3 0 4.9-1.9 4.9-4.6-2.9-.3-4.9 1.3-4.9 4.6z" fill="currentColor" fill-opacity=".16"/>'
    '<path d="M12 10V4.5"/>'
    '</svg>'
)

PIJL = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M3 8h10M9 4l4 4-4 4"/></svg>')

TEL_SVG = ('<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M18 14.2v2.3a1.5 1.5 0 0 1-1.6 1.5 14.8 14.8 0 0 1-6.5-2.3 14.6 14.6 0 0 1-4.5-4.5A14.8 14.8 0 0 1 3 4.6 1.5 1.5 0 0 1 4.5 3h2.3a1.5 1.5 0 0 1 1.5 1.3c.1.8.3 1.5.6 2.2a1.5 1.5 0 0 1-.4 1.6l-1 1a12 12 0 0 0 4.4 4.4l1-1a1.5 1.5 0 0 1 1.6-.3c.7.3 1.4.5 2.2.6a1.5 1.5 0 0 1 1.3 1.5z"/></svg>')

MAIL_SVG = ('<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<rect x="2.5" y="4" width="15" height="12" rx="2"/><path d="m3 5.5 7 5 7-5"/></svg>')


def nav_html(actief):
    """Bouwt het hoofdmenu; markeert de actieve pagina."""
    uit = ['<nav class="hoofdnav" id="hoofdnav" aria-label="Hoofdmenu">', '<ul>']
    for href, label, sub in NAV:
        if sub:
            key = href.lstrip('#')
            open_sub = any(s[0] == actief for s in sub)
            uit.append('<li class="heeft-sub">')
            uit.append(
                '<button type="button" class="sub-knop" aria-expanded="false" '
                'aria-controls="sub-{k}">{l}'
                '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" '
                'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                '<path d="m2.5 4.5 3.5 3.5 3.5-3.5"/></svg></button>'.format(k=key, l=label))
            uit.append('<ul class="submenu" id="sub-{k}">'.format(k=key))
            for shref, slabel, suit in sub:
                cur = ' aria-current="page"' if shref == actief else ''
                uit.append(
                    '<li><a href="{h}"{c}>{l}<span class="sub-uitleg">{u}</span></a></li>'
                    .format(h=shref, c=cur, l=slabel, u=suit))
            uit.append('</ul></li>')
            if open_sub:
                pass
        else:
            cur = ' aria-current="page"' if href == actief else ''
            uit.append('<li><a href="{h}"{c}>{l}</a></li>'.format(h=href, c=cur, l=label))
    uit.append('</ul></nav>')
    return '\n'.join(uit)


def kop_html(slug, titel, h1, lead):
    """Spoedbalk + sitekop + (voor subpaginas) de blauwe paginakop."""
    p = PRAKTIJK
    blokken = []
    blokken.append('''<a class="skip" href="#inhoud">Naar de inhoud</a>

<div class="spoedbalk">
  <div class="wrap">
    <p>{straat}, {postcode} {plaats} &middot; ma&ndash;vr geopend, weekend gesloten</p>
    <p><a class="pill" href="paardentandarts.html">Spoed</a>
       <a href="tel:{tel_link}">{tel}</a></p>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <a class="merk" href="index.html">
      <img src="assets/img/korenwolf-mark.png" width="122" height="149"
           alt="" role="presentation">
      <span class="merk-tekst">
        <span class="merk-boven">Dierenartspraktijk</span>
        <span class="merk-naam">De Korenwolf</span>
      </span>
    </a>
    <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="hoofdnav">
      <svg class="streep" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.9"
           stroke-linecap="round" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14"/></svg>
      <svg class="kruis" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.9"
           stroke-linecap="round" aria-hidden="true"><path d="m5 5 10 10M15 5 5 15"/></svg>
      Menu
    </button>
    {nav}
  </div>
</header>
<div class="nav-overlay" hidden></div>
'''.format(nav=nav_html(slug + '.html'), **p))

    if h1:
        blokken.append('''
<div class="paginakop">
  <div class="wrap">
    <p class="kruimels"><a href="index.html">Home</a><span>/</span>{titel}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</div>
'''.format(titel=titel, h1=h1, lead=lead))
    return ''.join(blokken)


def voet_html():
    p = PRAKTIJK
    return '''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <p class="footer-merk">
          <img src="assets/img/korenwolf-mark.png" width="122" height="149" alt="">
          <strong>De Korenwolf</strong>
        </p>
        <p>Dierenartspraktijk voor gezelschapsdieren, kleine herkauwers,
           hobbyvarkens en koikarpers in Berg en Terblijt.</p>
        <p>{straat}<br>{postcode} {plaats}</p>
        <p><a href="tel:{tel_link}">{tel}</a><br>
           <a href="mailto:{email}">{email}</a></p>
      </div>
      <div>
        <h3>Praktijk</h3>
        <ul>
          <li><a href="contact.html">Contact &amp; openingstijden</a></li>
          <li><a href="team.html">Ons team</a></li>
          <li><a href="actueel.html">Actueel</a></li>
          <li><a href="paardentandarts.html">Spoed &amp; dienstnummers</a></li>
        </ul>
      </div>
      <div>
        <h3>Diersoorten</h3>
        <ul>
          <li><a href="gezelschapsdieren.html">Gezelschapsdieren</a></li>
          <li><a href="landbouwhuisdieren.html">Landbouwhuisdieren</a></li>
          <li><a href="vogels.html">Vogels &amp; koikarpers</a></li>
          <li><a href="kittenopvang.html">Kittenopvang</a></li>
        </ul>
      </div>
      <div>
        <h3>Goed om te weten</h3>
        <ul>
          <li><a href="voorwaarden.html">Voorwaarden</a></li>
          <li><a href="verzekering.html">Verzekering</a></li>
          <li><a href="links.html">Links</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-onder">
      <p>&copy; <span id="jaar">2026</span> {naam}</p>
      <p>KvK {kvk} &middot; BTW-id {btw} &middot; DAP-nr {dapnr}</p>
    </div>
  </div>
</footer>

<script src="assets/js/site.js" defer></script>
<script>document.getElementById('jaar').textContent = new Date().getFullYear();</script>
'''.format(**p)


SJABLOON = '''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{omschrijving}">
<meta name="theme-color" content="#0E355E">
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
<meta property="og:image" content="https://www.dierenartspraktijkdekorenwolf.nl/assets/img/korenwolf-mark-180.png">
<link rel="preload" href="assets/fonts/sourcesans3-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/newsreader-500-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/stijl.css">
{extra_head}</head>
<body class="layout-body">
{kop}
<main id="inhoud">
{inhoud}
</main>
{voet}
</body>
</html>
'''

BEDRIJF_JSONLD = '''<script type="application/ld+json">
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
      "dayOfWeek": ["Monday","Friday"],
      "opens": "09:00", "closes": "12:00" },
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Friday"],
      "opens": "12:30", "closes": "18:00" },
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Tuesday","Wednesday","Thursday"],
      "opens": "09:00", "closes": "12:00" },
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Tuesday","Wednesday","Thursday"],
      "opens": "12:30", "closes": "17:00" }
  ]
}
</script>
'''


def bouw():
    gebouwd = []
    for slug, (titel, h1, lead, omschrijving) in PAGINAS.items():
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
                  .replace('{{AAR}}', AAR_SVG)
                  .replace('{{PIJL}}', PIJL)
                  .replace('{{TEL_SVG}}', TEL_SVG)
                  .replace('{{MAIL_SVG}}', MAIL_SVG)
                  .replace('{{MAPS_EMBED}}', MAPS_EMBED)
                  .replace('{{MAPS_LINK}}', MAPS_LINK))

        volle_titel = titel if slug == 'index' else titel + ' | Dierenartspraktijk De Korenwolf'
        html = SJABLOON.format(
            titel=volle_titel,
            omschrijving=omschrijving,
            slug=slug,
            extra_head=BEDRIJF_JSONLD if slug in ('index', 'contact') else '',
            kop=kop_html(slug, titel, h1, lead),
            inhoud=inhoud.strip(),
            voet=voet_html(),
        )
        with open(os.path.join(UIT, slug + '.html'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        gebouwd.append(slug)

    # robots.txt en sitemap
    basis = 'https://www.dierenartspraktijkdekorenwolf.nl/'
    with open(os.path.join(UIT, 'robots.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n' % basis)
    urls = ''.join(
        '  <url><loc>%s%s.html</loc><priority>%s</priority></url>\n'
        % (basis, s, '1.0' if s == 'index' else '0.8')
        for s in gebouwd)
    with open(os.path.join(UIT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                '%s</urlset>\n' % urls)

    print('Gebouwd: %d pagina%s -> site/' % (len(gebouwd), '' if len(gebouwd) == 1 else 's'))
    for s in gebouwd:
        print('  site/%s.html' % s)


if __name__ == '__main__':
    bouw()
