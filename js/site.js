// Kairós Studio · interacciones del sitio (menú, filtros de proyectos, mensajes de WhatsApp)
(function () {
  'use strict';
  var WHATSAPP = '593982981089';

  // ---------- Menú en celular y tableta ----------
  var boton = document.querySelector('.boton-menu');
  var menu = document.getElementById('menu');
  if (boton && menu) {
    var abrir = function (abierto) {
      boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      menu.classList.toggle('abierto', abierto);
    };
    boton.addEventListener('click', function () {
      abrir(boton.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('abierto')) { abrir(false); boton.focus(); }
    });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) abrir(false); });
  }

  // ---------- Filtros de proyectos ----------
  var filtros = document.querySelectorAll('.filtro');
  if (filtros.length) {
    var proyectos = document.querySelectorAll('.proyecto');
    var estado = document.getElementById('estado-filtro');
    var aplicar = function (cat, etiqueta) {
      var visibles = 0;
      proyectos.forEach(function (p) {
        var ver = cat === 'todos' || p.getAttribute('data-categoria') === cat;
        p.hidden = !ver;
        if (ver) visibles++;
      });
      filtros.forEach(function (f) { f.setAttribute('aria-pressed', f.getAttribute('data-filtro') === cat ? 'true' : 'false'); });
      if (estado) estado.textContent = 'Mostrando ' + visibles + (visibles === 1 ? ' proyecto' : ' proyectos') + (cat === 'todos' ? '' : ' de ' + etiqueta.toLowerCase()) + '.';
    };
    filtros.forEach(function (f) {
      f.addEventListener('click', function () { aplicar(f.getAttribute('data-filtro'), f.textContent.trim()); });
    });
    var inicial = (location.hash || '').replace('#', '');
    var porHash = document.querySelector('.filtro[data-filtro="' + inicial + '"]');
    if (porHash) aplicar(inicial, porHash.textContent.trim());
  }

  // ---------- Asistentes de mensaje para WhatsApp ----------
  document.querySelectorAll('form[data-whatsapp]').forEach(function (form) {
    var tipo = form.getAttribute('data-whatsapp');
    var enlace = form.querySelector('.abrir-whatsapp');
    var vista = form.querySelector('.vista-previa');
    var campo = function (n) { var el = form.elements[n]; return el ? el.value.trim() : ''; };

    // Preselección desde los enlaces de cada servicio (?servicio=… o ?trabajo=…)
    var params = new URLSearchParams(location.search);
    ['servicio', 'trabajo'].forEach(function (n) {
      var el = form.elements[n], v = params.get(n);
      if (el && v && Array.prototype.some.call(el.options, function (o) { return o.value === v || o.text === v; })) el.value = v;
    });

    var mensaje = function () {
      if (tipo === 'negocio') {
        var lineas = ['Hola, Kairós Studio. Escribo por mi negocio.'];
        if (campo('negocio')) lineas.push('Negocio: ' + campo('negocio'));
        lineas.push('Servicio de interés: ' + (campo('servicio') || '(por definir)'));
        lineas.push('Lo que quiero lograr: ' + (campo('objetivo') || '(por completar)'));
        return lineas.join('\n');
      }
      var l = ['Hola, Kairós Studio. Quiero consultar por una sesión o evento.'];
      l.push('Tipo de trabajo: ' + (campo('trabajo') || '(por definir)'));
      l.push('Fecha: ' + (campo('fecha') || '(por completar)'));
      l.push('Lugar: ' + (campo('lugar') || '(por completar)'));
      if (campo('detalles')) l.push('Detalles: ' + campo('detalles'));
      return l.join('\n');
    };

    var actualizar = function () {
      var texto = mensaje();
      if (vista) vista.textContent = texto;
      enlace.href = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(texto);
    };

    var obligatorios = form.querySelectorAll('[data-obligatorio]');
    var validar = function () {
      var primero = null;
      obligatorios.forEach(function (el) {
        var error = document.getElementById(el.getAttribute('aria-describedby').split(' ').filter(function (id) { return id.indexOf('error') === 0; })[0]);
        var vacio = !el.value.trim();
        el.setAttribute('aria-invalid', vacio ? 'true' : 'false');
        if (error) error.textContent = vacio ? el.getAttribute('data-obligatorio') : '';
        if (vacio && !primero) primero = el;
      });
      return primero;
    };

    form.addEventListener('input', function (e) {
      actualizar();
      if (e.target.getAttribute('aria-invalid') === 'true' && e.target.value.trim()) {
        e.target.setAttribute('aria-invalid', 'false');
        var ids = (e.target.getAttribute('aria-describedby') || '').split(' ');
        ids.forEach(function (id) { if (id.indexOf('error') === 0) { var er = document.getElementById(id); if (er) er.textContent = ''; } });
      }
    });
    form.addEventListener('change', actualizar);
    enlace.addEventListener('click', function (e) {
      var faltante = validar();
      if (faltante) { e.preventDefault(); faltante.focus(); return; }
      actualizar();
    });
    form.addEventListener('submit', function (e) { e.preventDefault(); enlace.click(); });
    form.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && e.target.tagName === 'INPUT') { e.preventDefault(); enlace.click(); }
    });
    actualizar();
  });
})();
