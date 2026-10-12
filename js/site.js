// Kairós · menú móvil
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('menu');
  if (!toggle || !menu) return;

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    menu.classList.toggle('is-open', open);
  }

  toggle.addEventListener('click', function () {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && menu.classList.contains('is-open')) {
      setOpen(false);
      toggle.focus();
    }
  });

  // Cierra el menú al elegir un enlace interno de la misma página (p. ej. Nosotros en Inicio)
  menu.addEventListener('click', function (e) {
    if (e.target.closest('a')) setOpen(false);
  });
})();
