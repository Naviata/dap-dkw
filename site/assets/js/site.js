/* Dierenartspraktijk De Korenwolf - site.js
   1. Mobiel menu
   2. Openingstijden: "nu open / nu gesloten"
   3. Google Maps pas laden na toestemming (privacyvriendelijk)
*/
(function () {
  'use strict';

  /* ---------- 1. Mobiel menu ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('hoofdnav');
  var overlay = document.querySelector('.nav-overlay');

  function sluitMenu() {
    if (!toggle || !nav) return;
    toggle.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.classList.remove('nav-open');
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('open', !open);
      if (overlay) overlay.classList.toggle('open', !open);
      document.body.classList.toggle('nav-open', !open);
    });
  }
  if (overlay) overlay.addEventListener('click', sluitMenu);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      sluitMenu();
      Array.prototype.forEach.call(document.querySelectorAll('.sub-knop[aria-expanded="true"]'), function (b) {
        b.setAttribute('aria-expanded', 'false');
      });
    }
  });

  /* Submenu's: klik op mobiel, hover op desktop (CSS) */
  Array.prototype.forEach.call(document.querySelectorAll('.sub-knop'), function (knop) {
    knop.addEventListener('click', function () {
      var open = knop.getAttribute('aria-expanded') === 'true';
      Array.prototype.forEach.call(document.querySelectorAll('.sub-knop'), function (a) {
        if (a !== knop) a.setAttribute('aria-expanded', 'false');
      });
      knop.setAttribute('aria-expanded', String(!open));
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest || !e.target.closest('.heeft-sub')) {
      Array.prototype.forEach.call(document.querySelectorAll('.sub-knop[aria-expanded="true"]'), function (b) {
        b.setAttribute('aria-expanded', 'false');
      });
    }
  });

  /* ---------- 2. Nu open of gesloten? ---------- */
  /* ma=1 ... vr=5. Tijden in minuten na middernacht. */
  var ROOSTER = {
    1: [[540, 720], [750, 1080]],
    2: [[540, 720], [750, 1020]],
    3: [[540, 720], [750, 1020]],
    4: [[540, 720], [750, 1020]],
    5: [[540, 720], [750, 1080]],
    6: [],
    0: []
  };
  var DAGEN = ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag'];

  function hhmm(m) {
    var h = Math.floor(m / 60), mi = m % 60;
    return h + '.' + (mi < 10 ? '0' + mi : mi) + ' uur';
  }

  function status() {
    var nu = new Date();
    var dag = nu.getDay();
    var min = nu.getHours() * 60 + nu.getMinutes();
    var blokken = ROOSTER[dag] || [];
    for (var i = 0; i < blokken.length; i++) {
      if (min >= blokken[i][0] && min < blokken[i][1]) {
        return { open: true, tekst: 'Nu geopend - vandaag tot ' + hhmm(blokken[i][1]) };
      }
    }
    /* eerstvolgende opening zoeken */
    for (var d = 0; d < 8; d++) {
      var dd = (dag + d) % 7;
      var bl = ROOSTER[dd] || [];
      for (var j = 0; j < bl.length; j++) {
        if (d > 0 || bl[j][0] > min) {
          var wanneer = d === 0 ? 'vandaag' : (d === 1 ? 'morgen' : DAGEN[dd]);
          return { open: false, tekst: 'Nu gesloten - open ' + wanneer + ' vanaf ' + hhmm(bl[j][0]) };
        }
      }
    }
    return { open: false, tekst: 'Nu gesloten' };
  }

  var doel = document.querySelector('[data-nu-status]');
  if (doel) {
    var s = status();
    doel.innerHTML = '<span class="stip ' + (s.open ? 'open' : 'dicht') + '" aria-hidden="true"></span><span>' + s.tekst + '</span>';
  }

  /* Dag van vandaag markeren in de openingstijdentabel */
  var vandaag = new Date().getDay();
  var rij = document.querySelector('.tijden tr[data-dag~="' + vandaag + '"]');
  if (rij) rij.classList.add('vandaag');

  /* ---------- 3. Kaart pas laden na klik ---------- */
  var kaartKnop = document.querySelector('[data-kaart-laden]');
  if (kaartKnop) {
    kaartKnop.addEventListener('click', function () {
      var blok = kaartKnop.closest('.kaart-blok');
      var src = kaartKnop.getAttribute('data-kaart-laden');
      var frame = document.createElement('iframe');
      frame.src = src;
      frame.title = 'Kaart met de locatie van Dierenartspraktijk De Korenwolf';
      frame.loading = 'lazy';
      frame.setAttribute('referrerpolicy', 'no-referrer-when-downgrade');
      frame.setAttribute('allowfullscreen', '');
      blok.innerHTML = '';
      blok.appendChild(frame);
    });
  }
})();
