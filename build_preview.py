#!/usr/bin/env python3
"""
Bouwt een voorbeeldversie van de hele site als EEN los HTML-bestand.

Alle 12 pagina's zitten erin, met werkende navigatie, zodat je de site kunt
doorklikken voordat je hem uploadt. Afbeeldingen en CSS staan in het bestand
zelf; alleen de lettertypes komen van Google Fonts.

Dit bestand is alleen voor de voorvertoning. Wat je uploadt is de map site/.
"""

import base64
import os
import re

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HIER, 'site')
UIT = os.path.join(HIER, 'voorbeeld.html')

VOLGORDE = ['index', 'contact', 'team', 'actueel', 'gezelschapsdieren',
            'landbouwhuisdieren', 'vogels', 'kittenopvang', 'paardentandarts',
            'verzekering', 'links', 'voorwaarden']

MIME = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg'}


def data_uri(pad):
    ext = os.path.splitext(pad)[1].lower()
    with open(pad, 'rb') as f:
        return 'data:%s;base64,%s' % (MIME.get(ext, 'application/octet-stream'),
                                      base64.b64encode(f.read()).decode('ascii'))


def pak(html, tag):
    """Haalt de binnenkant van het eerste <tag ...> ... </tag> blok op."""
    m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), html, re.S)
    return m.group(1) if m else ''


def blok(html, opening):
    """Pakt een <div>-blok inclusief de bijbehorende sluittag, door te tellen.

    Regexen tellen niet, en de blokken hier bevatten geneste divs. Deze functie
    loopt vanaf de openingstag door de tekst en houdt bij hoeveel divs er open
    staan, zodat we precies de juiste </div> te pakken krijgen.
    """
    start = html.find(opening)
    if start < 0:
        return ''
    diepte = 0
    for m in re.finditer(r'<div\b|</div>', html[start:]):
        diepte += 1 if m.group(0) != '</div>' else -1
        if diepte == 0:
            return html[start:start + m.end()]
    return ''


def bouw():
    # ---- CSS, zonder de @import naar de lokale fonts
    css = open(os.path.join(SITE, 'assets/css/stijl.css'), encoding='utf-8').read()
    css = css.replace("@import url('../fonts/fonts.css');", '')
    css = css.replace("'Source Sans 3'", "'Source Sans 3'")

    # ---- afbeeldingen inbakken
    plaatjes = {}
    imgdir = os.path.join(SITE, 'assets/img')
    for naam in os.listdir(imgdir):
        if os.path.splitext(naam)[1].lower() in MIME:
            plaatjes['assets/img/' + naam] = data_uri(os.path.join(imgdir, naam))

    def vervang_paden(s):
        for pad, uri in plaatjes.items():
            s = s.replace('src="%s"' % pad, 'src="%s"' % uri)
        return s

    index = open(os.path.join(SITE, 'index.html'), encoding='utf-8').read()

    # gedeelde onderdelen: spoedbalk, header, footer
    banner = blok(index, '<div class="banner">')
    menu = re.search(r'<nav class="menubalk".*?</nav>', index, re.S).group(0)
    footer = re.search(r'<footer class="voet">.*?</footer>', index, re.S).group(0)

    # ---- de losse pagina's
    delen = []
    titels = {}
    for slug in VOLGORDE:
        pad = os.path.join(SITE, slug + '.html')
        if not os.path.exists(pad):
            continue
        html = open(pad, encoding='utf-8').read()
        titels[slug] = re.search(r'<title>(.*?)</title>', html, re.S).group(1)
        inhoud = blok(html, '<div class="inhoud"')
        delen.append('<div class="pv-pagina" id="pv-%s" hidden>\n%s\n</div>'
                     % (slug, inhoud))

    body = '\n'.join(['<div class="blad">', banner, menu] + delen + [footer, '</div>'])
    body = vervang_paden(body)

    extra_css = """
/* alleen voor deze voorvertoning */
.pv-pagina[hidden]{display:none}
.pv-balk{position:fixed;left:50%;transform:translateX(-50%);bottom:16px;z-index:300;
  background:var(--blauw-diep);color:#fff;border-radius:999px;padding:.5rem .95rem;
  font:600 .8rem/1.3 var(--sans);box-shadow:0 8px 30px rgba(0,0,0,.3);
  display:flex;align-items:center;gap:.6rem;max-width:calc(100% - 2rem)}
.pv-balk span{opacity:.75;font-weight:400}
.pv-balk button{background:rgba(255,255,255,.14);color:#fff;border:0;border-radius:999px;
  padding:.25rem .7rem;font:inherit;cursor:pointer}
.pv-balk button:hover{background:rgba(255,255,255,.26)}
@media print{.pv-balk{display:none}}
"""

    router = """
<script>
(function(){
  var VOLGORDE = %s;
  var TITELS = %s;
  function toon(slug, push){
    if(!document.getElementById('pv-'+slug)) slug='index';
    VOLGORDE.forEach(function(s){
      var el=document.getElementById('pv-'+s);
      if(el) el.hidden = (s!==slug);
    });
    document.querySelectorAll('.menubalk a').forEach(function(a){
      var h=a.getAttribute('href')||'';
      if(h===slug+'.html') a.setAttribute('aria-current','page');
      else a.removeAttribute('aria-current');
    });
    document.title = TITELS[slug] || 'De Korenwolf';
    if(push) history.replaceState(null,'','#'+slug);
    window.scrollTo(0,0);
    var lijst=document.getElementById('menu');
    if(lijst) lijst.classList.remove('open');
    var t=document.querySelector('.menuknop');
    if(t) t.setAttribute('aria-expanded','false');
  }
  document.addEventListener('click', function(e){
    var a=e.target.closest && e.target.closest('a');
    if(!a) return;
    var h=a.getAttribute('href')||'';
    var m=h.match(/^([a-z0-9_-]+)\\.html$/);
    if(m){ e.preventDefault(); toon(m[1], true); }
  }, true);
  toon((location.hash||'#index').slice(1), false);
})();
</script>
"""% (repr(VOLGORDE).replace("'", '"'),
      '{' + ','.join('"%s":%s' % (k, repr(v).replace("'", '"')) for k, v in titels.items()) + '}')

    balk = ('<div class="pv-balk">Voorvertoning'
            '<span>alle 12 pagina&rsquo;s, klik het menu door</span>'
            '<button type="button" onclick="this.parentNode.remove()">verbergen</button></div>')

    site_js = open(os.path.join(SITE, 'assets/js/site.js'), encoding='utf-8').read()

    uit = []
    uit.append('<title>De Korenwolf</title>')
    uit.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
    uit.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    uit.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
               'family=Source+Sans+3:wght@400;600;700'
               '&display=swap">')
    uit.append('<style>\n%s\n%s</style>' % (css, extra_css))
    uit.append(body)
    uit.append(balk)
    uit.append('<script>%s</script>' % site_js)
    uit.append(router)

    with open(UIT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(uit))

    kb = os.path.getsize(UIT) / 1024
    print('voorbeeld.html gebouwd: %d pagina%s, %.0f KB'
          % (len(delen), '' if len(delen) == 1 else "'s", kb))


if __name__ == '__main__':
    bouw()
