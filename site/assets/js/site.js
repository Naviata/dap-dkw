/* Dierenartspraktijk De Korenwolf
   Alleen het menu: uitklappen op telefoon en de twee submenu's. */
(function () {
  'use strict';

  var knop = document.querySelector('.menuknop');
  var lijst = document.getElementById('menu');

  if (knop && lijst) {
    knop.addEventListener('click', function () {
      var open = knop.getAttribute('aria-expanded') === 'true';
      knop.setAttribute('aria-expanded', String(!open));
      lijst.classList.toggle('open', !open);
    });
  }

  var subknoppen = document.querySelectorAll('.uitklap');

  function sluitSubmenus(behalve) {
    Array.prototype.forEach.call(subknoppen, function (b) {
      if (b !== behalve) b.setAttribute('aria-expanded', 'false');
    });
  }

  Array.prototype.forEach.call(subknoppen, function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('aria-expanded') === 'true';
      sluitSubmenus(b);
      b.setAttribute('aria-expanded', String(!open));
    });
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest || !e.target.closest('.heeft-sub')) sluitSubmenus(null);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') sluitSubmenus(null);
  });
})();
