"""Genera las páginas de Kairós Studio con el mismo encabezado, llamada de contacto y pie.

Uso (desde la raíz del repositorio):  python3 _src/build.py
Edita los textos aquí y vuelve a ejecutar; los .html de la raíz se sobrescriben.
REVISION = True muestra las notas y el aviso de la versión de revisión; ponlo en False para publicar.
"""
import os
from urllib.parse import quote

REVISION = False
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = "https://kairos-studio-ec.vercel.app"
NOMBRE = "Kairós Studio"
TEL_VISIBLE = "098 298 1089"
WA_NUM = "593982981089"
IG = "https://www.instagram.com/kairos.estudio.ec/"
FB = "https://www.facebook.com/profile.php?id=61595387390430"

def wa(texto):
    return f"https://wa.me/{WA_NUM}?text={quote(texto)}"

WA_NEGOCIO = wa("Hola, Kairós Studio. Escribo por mi negocio.\nServicio de interés: \nLo que quiero lograr: ")
WA_MOMENTOS = wa("Hola, Kairós Studio. Quiero consultar por una sesión o evento.\nTipo de trabajo: \nFecha: \nLugar: ")
WA_GENERAL = wa("Hola, Kairós Studio. Quiero hacer una consulta.")

NUEVA = '<span class="visually-hidden"> (se abre en una pestaña nueva)</span>'
EXT = 'target="_blank" rel="noopener noreferrer"'

# ---------- Iconos (trazo) ----------
def ico(path, s=20, sw=1.7):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{path}</svg>')
I_WA = '<path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.4L3 20.5l1.6-5.2A8.5 8.5 0 1 1 21 11.5z"></path>'
I_IG = '<rect x="3" y="3" width="18" height="18" rx="5"></rect><circle cx="12" cy="12" r="4"></circle><circle cx="17.3" cy="6.7" r="0.6" fill="currentColor"></circle>'
I_FB = '<path d="M15 3h-2.5A4.5 4.5 0 0 0 8 7.5V10H5.5v4H8v7h4v-7h3l.5-4H12V7.8c0-.6.5-.8 1-.8h2z"></path>'
I_PIN = '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"></path><circle cx="12" cy="9.5" r="2.5"></circle>'
I_CAM = '<path d="M4 8h3l2-3h6l2 3h3v11H4z"></path><circle cx="12" cy="13" r="3.5"></circle>'

def greca():
    return ('<svg class="greca" viewBox="0 0 96 20" aria-hidden="true" focusable="false">'
            '<path d="M1 19V1h18v16H7V7h7v5M25 19V1h18v16H31V7h7v5M49 19V1h18v16H55V7h7v5M73 19V1h18v16H79V7h7v5" '
            'fill="none" stroke="currentColor" stroke-width="2"></path></svg>')

# ---------- Fotos reales ----------
# _src/fotos.json asigna una foto a cada espacio: {"portada": {"archivo": "x.jpg", "alt": "…", "posicion": "50% 40%"}}
# _src/optimizar.py convierte el original de _src/fotos-originales/ en assets/fotos/<clave>-800.webp y -1600.webp.
import json
_FOTOS_JSON = os.path.join(RAIZ, "_src", "fotos.json")
FOTOS = json.load(open(_FOTOS_JSON, encoding="utf-8")) if os.path.exists(_FOTOS_JSON) else {}
TAMANOS = {"retrato": "(max-width: 820px) 92vw, 44vw", "alta": "(max-width: 820px) 92vw, 40vw",
           "cuadrada": "(max-width: 820px) 92vw, 40vw", "apaisada": "(max-width: 820px) 92vw, 46vw"}

def foto(forma, que, clave=None, prioridad=False):
    """Muestra la foto real asignada a `clave`; si no existe, un marco «Foto pendiente» claramente identificado."""
    datos = FOTOS.get(clave) if clave else None
    nombre = os.path.splitext(datos["archivo"])[0] if datos else None
    if datos and os.path.exists(os.path.join(RAIZ, "assets", "fotos", f"{nombre}-1600.webp")):
        w, h = datos.get("ancho", 1600), datos.get("alto", 1200)
        pos = f' style="object-position: {datos["posicion"]}"' if datos.get("posicion") else ""
        carga = 'fetchpriority="high"' if prioridad else 'loading="lazy"'
        # Imágenes de ambiente que no son trabajos de clientes: se marcan a la vista
        etiqueta = '<figcaption class="foto-etiqueta">Imagen ilustrativa creada con IA</figcaption>' if datos.get("ilustrativa") else ''
        return (f'<figure class="foto foto--{forma}"><img src="/assets/fotos/{nombre}-1600.webp" '
                f'srcset="/assets/fotos/{nombre}-800.webp 800w, /assets/fotos/{nombre}-1600.webp 1600w" sizes="{TAMANOS[forma]}" '
                f'width="{w}" height="{h}" alt="{datos["alt"]}" {carga} decoding="async"{pos}>{etiqueta}</figure>')
    if not REVISION:
        return ""  # al publicar, los espacios sin foto real se ocultan
    return (f'<figure class="foto foto--{forma} foto--pendiente" role="img" aria-label="Espacio para foto pendiente: {que}">'
            f'<figcaption class="foto-nota">{ico(I_CAM, 26, 1.4)}<strong>Foto pendiente</strong><span>{que}</span></figcaption></figure>')

def nota(texto):
    return f'<p class="nota-revision"><strong>Pendiente de confirmar:</strong> {texto}</p>' if REVISION else ''

def redes():
    return f'''<ul class="redes">
<li><a class="red" href="{IG}" {EXT}>{ico(I_IG, 22)}<span>Instagram<small>@kairos.estudio.ec</small></span>{NUEVA}</a></li>
<li><a class="red" href="{FB}" {EXT}>{ico(I_FB, 22)}<span>Facebook</span>{NUEVA}</a></li>
</ul>'''

MENU = [("inicio", "/", "Inicio"), ("negocio", "/negocio", "Para tu negocio"),
        ("momentos", "/momentos", "Para tus momentos"), ("proyectos", "/proyectos", "Proyectos"),
        ("sobre", "/sobre", "Sobre Kairós")]

def encabezado(activa):
    enlaces = "\n".join(f'<a class="menu-enlace" href="{h}"' + (' aria-current="page"' if k == activa else '') + f'>{t}</a>'
                        for k, h, t in MENU)
    contacto_actual = ' aria-current="page"' if activa == "contacto" else ''
    aviso = ('<p class="aviso-revision"><strong>Versión de revisión.</strong> Los espacios marcados como pendientes se completan con material real antes de publicar.</p>'
             if REVISION else '')
    return f'''<a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="site-header">
{aviso}
<div class="wrap cabecera">
<a class="marca" href="/" aria-label="{NOMBRE}, ir a Inicio"><img src="/assets/logo-petroleo.webp" alt="{NOMBRE}" width="157" height="62"></a>
<button class="boton-menu" type="button" aria-expanded="false" aria-controls="menu">
{ico('<path d="M4 7h16M4 12h16M4 17h16"></path>', 20, 1.8).replace('<svg ', '<svg class="ico-abrir" ', 1)}
{ico('<path d="M6 6l12 12M18 6L6 18"></path>', 20, 1.8).replace('<svg ', '<svg class="ico-cerrar" ', 1)}
Menú
</button>
<nav id="menu" class="menu" aria-label="Principal">
{enlaces}
<a class="btn btn-oscuro btn-s" href="/contacto"{contacto_actual}>Contacto</a>
</nav>
</div>
</header>'''

def llamada_contacto():
    return f'''<section class="sobre-oscuro bloque" aria-labelledby="llamada-titulo">
<div class="wrap llamada">
<div class="pila">
{greca()}
<h2 id="llamada-titulo" class="t-seccion">¿Tienes un proyecto o una fecha en mente?</h2>
<p class="entrada">Escríbenos por WhatsApp. Con unos pocos datos te respondemos con una propuesta a la medida.</p>
</div>
<div class="llamada-opciones">
<a class="llamada-opcion" href="/contacto#negocio"><strong>Para tu negocio</strong><span>Cuéntanos qué servicio te interesa y qué quieres lograr.</span></a>
<a class="llamada-opcion" href="/contacto#momentos"><strong>Para una sesión o evento</strong><span>Cuéntanos el tipo de trabajo, la fecha y el lugar.</span></a>
</div>
</div>
</section>'''

def pie():
    paginas = "\n".join(f'<li><a href="{h}">{t}</a></li>' for _, h, t in MENU) + '\n<li><a href="/contacto">Contacto</a></li>'
    return f'''<footer class="site-footer">
<div class="wrap pie">
<div class="pie-marca">
<a href="/" aria-label="{NOMBRE}, ir a Inicio"><img src="/assets/logo-marfil.webp" alt="{NOMBRE}: marketing, fotografía, eventos" width="202" height="80"></a>
<p>Marcas que crecen, momentos que cuentan.</p>
</div>
<nav aria-label="Páginas del sitio">
<h2>Páginas</h2>
<ul class="pie-enlaces">
{paginas}
</ul>
</nav>
<div>
<h2>Síguenos</h2>
{redes()}
</div>
<div>
<h2>Contacto</h2>
<ul class="pie-enlaces">
<li><a href="{WA_GENERAL}" {EXT}>WhatsApp {TEL_VISIBLE}{NUEVA}</a></li>
<li class="texto">Quito, Ecuador</li>
</ul>
</div>
</div>
<div class="wrap"><p class="pie-final">© 2026 {NOMBRE}. Marcas que crecen, momentos que cuentan.</p></div>
</footer>'''

def migas(etiqueta):
    return f'''<nav class="migas" aria-label="Ruta de navegación"><ol><li><a href="/">Inicio</a></li><li><span aria-current="page">{etiqueta}</span></li></ol></nav>'''

JSONLD = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ProfessionalService","name":"{NOMBRE}","url":"{SITIO}/","image":"{SITIO}/assets/og.jpg",
"slogan":"Marcas que crecen, momentos que cuentan.","telephone":"+{WA_NUM}",
"address":{{"@type":"PostalAddress","addressLocality":"Quito","addressCountry":"EC"}},"areaServed":"Quito",
"sameAs":["{IG}","{FB}"]}}
</script>'''

def pagina(ruta, titulo, descripcion, activa, cuerpo, extra_head=""):
    url = SITIO + ruta
    indexar = '<meta name="robots" content="noindex">' if ruta == "/404" else f'<link rel="canonical" href="{url}">'
    return f'''<!doctype html>
<html lang="es-EC">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
{indexar}
<meta name="theme-color" content="#10292D">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_EC">
<meta property="og:site_name" content="{NOMBRE}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:image" content="{SITIO}/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&amp;family=Jost:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="/css/site.css">
<script>
document.documentElement.classList.add('js');
(function(){{var m={{'#servicios':'/negocio','#proceso':'/sobre#proceso','#eventos':'/momentos','#portafolio':'/proyectos','#nosotros':'/sobre'}};function ir(){{var p=location.pathname;if((p==='/'||p==='/index.html'||p==='/index')&&m[location.hash]){{location.replace(m[location.hash]);}}}}ir();window.addEventListener('hashchange',ir);}})();
</script>
<script src="/js/site.js" defer></script>
{extra_head}
</head>
<body>
{encabezado(activa)}
<main id="contenido">
{cuerpo}
</main>
{pie()}
</body>
</html>
'''

# =====================================================================
# Contenido
# =====================================================================

SERVICIOS = [
    {
        "id": "marketing", "nombre": "Marketing digital",
        "resumen": "Estrategia, mensajes y campañas para llegar a quien te compra.",
        "necesidad": "Publicas y anuncias, pero no tienes claro si llegas a las personas correctas ni qué está funcionando.",
        "ayuda": "Definimos a quién le hablas, qué decir y en qué canales, y lo convertimos en acciones que se pueden revisar y ajustar.",
        "incluye": ["Diagnóstico de tu marca y de tu competencia", "Estrategia de comunicación y mensajes clave",
                    "Campañas pagadas en Meta y Google", "Revisión de resultados y ajustes"],
        "foto": "pieza de una campaña hecha por Kairós Studio",
    },
    {
        "id": "redes", "nombre": "Gestión de redes y planificación de contenido",
        "resumen": "Un calendario claro y publicaciones con una misma voz.",
        "necesidad": "Tus redes se actualizan cuando hay tiempo y cada publicación parece de una marca distinta.",
        "ayuda": "Planificamos qué publicar y cuándo, y cuidamos que el tono y la imagen sean reconocibles en cada pieza.",
        "incluye": ["Calendario de contenido", "Diseño de publicaciones e historias", "Redacción de textos",
                    "Programación de publicaciones", "Revisión periódica de lo que mejor funciona"],
        "foto": "cuadrícula de publicaciones de un cliente en Instagram",
    },
    {
        "id": "fotografia", "nombre": "Fotografía comercial y de producto",
        "resumen": "Imágenes propias que muestran la calidad de lo que vendes.",
        "necesidad": "Las fotos hechas con el celular no reflejan la calidad de tus productos ni de tu espacio.",
        "ayuda": "Fotografiamos tus productos, tu local y tu equipo pensando en dónde se va a usar cada imagen.",
        "incluye": ["Fotos de producto con fondo neutro o en contexto", "Fotos de tu local, tu equipo o tu proceso",
                    "Imágenes editadas y adaptadas a redes, web y catálogo"],
        "foto": "fotografía de producto hecha por Kairós Studio",
    },
    {
        "id": "video", "nombre": "Video para redes y campañas",
        "resumen": "Piezas cortas, grabadas y editadas para cada formato.",
        "necesidad": "Quieres mostrar tu marca en movimiento, pero no tienes quién grabe ni edite.",
        "ayuda": "Grabamos y editamos videos cortos con un mensaje claro desde los primeros segundos.",
        "incluye": ["Reels y videos verticales", "Video promocional para campañas",
                    "Edición, subtítulos y versiones para cada red"],
        "foto": "fotograma de un video para redes hecho por Kairós Studio",
    },
]

COBERTURAS = [("Bodas", "Ceremonia, recepción y sesión de pareja"),
              ("Graduaciones", "Ceremonias y sesiones de egresados"),
              ("Bautizos", "El día y la familia, con calma"),
              ("Conferencias", "Cobertura, ponentes y video resumen")]
SESIONES = ["Sesión de pareja", "Sesión de graduación", "Sesión familiar"]

PASOS = [("Consulta inicial", "Conversamos sobre tu objetivo o tu evento, los plazos y el material que ya tienes."),
         ("Propuesta y alcance", "Te enviamos por escrito qué haremos, qué recibirás y en qué fechas."),
         ("Producción", "Planificamos, fotografiamos, grabamos, diseñamos y escribimos según lo acordado."),
         ("Revisión y entrega", "Revisas el material, hacemos los ajustes acordados y te entregamos los archivos finales.")]

def pasos_html():
    return '<ol class="pasos">' + "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in PASOS) + '</ol>'


def hay_foto(clave):
    return clave in FOTOS and os.path.exists(os.path.join(RAIZ, "assets", "fotos", os.path.splitext(FOTOS[clave]["archivo"])[0] + "-1600.webp"))

INICIO_LINEAS = [("inicio-1", "Marketing y redes", "/negocio#marketing"),
                 ("inicio-2", "Fotografía comercial", "/negocio#fotografia"),
                 ("inicio-3", "Video y eventos", "/negocio#video")]

def seccion_trabajos():
    """Inicio: fotos de trabajos reales («Trabajos») o, mientras sean ilustrativas, «Lo que hacemos»."""
    claves = [k for k, _, _ in INICIO_LINEAS]
    if not REVISION and not any(hay_foto(k) for k in claves):
        return ""
    ilustrativas = all(FOTOS.get(k, {}).get("ilustrativa") for k in claves if hay_foto(k)) and any(hay_foto(k) for k in claves)
    if ilustrativas:
        titulo, texto, enlace = "Lo que hacemos", "Marketing, fotografía y video para marcas, y cobertura de tus celebraciones.", ("/negocio", "Ver servicios")
    else:
        titulo, texto, enlace = "Trabajos", "Cada proyecto explica qué necesitaba el cliente, qué hicimos y qué entregamos.", ("/proyectos", "Ver todos los proyectos")
    figuras = "".join(f'''<div class="pila-s">{foto("apaisada", etiqueta.lower(), k)}<p class="proyecto-cat"><a href="{h}">{etiqueta}</a></p></div>''' for k, etiqueta, h in INICIO_LINEAS)
    return f'''<section class="bloque" aria-labelledby="trabajos-titulo">
<div class="wrap">
<div class="encabezado-fila">
<div class="pila-s"><h2 id="trabajos-titulo" class="t-seccion">{titulo}</h2><p class="suave medida">{texto}</p></div>
<a class="enlace-flecha" href="{enlace[0]}">{enlace[1]}</a>
</div>
<div class="proyectos" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 32px 24px">
{figuras}
</div>
</div>
</section>'''

# ---------- Inicio ----------
inicio = f'''<div class="wrap portada">
<div class="portada-texto">
<h1 class="t-portada">Marcas que crecen, momentos que cuentan.</h1>
<p class="entrada">Somos un estudio creativo en Quito. Ayudamos a negocios a comunicar mejor con marketing digital, redes, fotografía y video, y acompañamos a personas en sus sesiones y celebraciones.</p>
<div class="botones">
<a class="btn btn-principal" href="/contacto">Pedir una propuesta</a>
<a class="btn btn-linea" href="/proyectos">Ver proyectos</a>
</div>
<p class="portada-lugar">{ico(I_PIN, 18)}Quito, Ecuador</p>
</div>
{foto("retrato", "imagen principal con un trabajo real de Kairós Studio", "portada", prioridad=True)}
</div>

<section class="diptico" aria-label="Elige tu recorrido">
<div class="recorrido recorrido--negocio sobre-oscuro">
<p class="etiqueta" style="color: var(--dorado)">Para empresas y emprendedores</p>
<h2>Para tu negocio</h2>
<p>Estrategia y contenido para que tu marca se vea bien, se entienda y llegue a más clientes. La fotografía y el video aportan imágenes propias a cada campaña.</p>
<ul class="recorrido-lista">
{"".join(f"<li>{s['nombre']}</li>" for s in SERVICIOS)}
</ul>
<div class="botones"><a class="btn btn-principal" href="/negocio">Ver servicios para negocios</a></div>
</div>
<div class="recorrido recorrido--momentos sobre-jade">
<p class="etiqueta">Para personas y familias</p>
<h2>Para tus momentos</h2>
<p>Sesiones fotográficas y cobertura en foto y video de celebraciones, para conservar las fechas que no se repiten.</p>
<ul class="recorrido-lista">
<li>Sesiones fotográficas</li>
<li>Bodas, graduaciones y bautizos</li>
<li>Conferencias y encuentros</li>
</ul>
<div class="botones"><a class="btn btn-principal" href="/momentos">Ver sesiones y eventos</a></div>
</div>
</section>

{seccion_trabajos()}

<section class="bloque fondo-papel" aria-labelledby="enfoque-titulo">
<div class="wrap significado">
<div class="pila">
{greca()}
<h2 id="enfoque-titulo" class="t-seccion">El momento oportuno</h2>
<p class="suave">En griego, <em>kairós</em> es el instante exacto en que algo importante sucede. Así entendemos nuestro trabajo.</p>
<a class="enlace-flecha" href="/sobre">Conoce cómo trabajamos</a>
</div>
<div>
<blockquote>Entender primero qué necesitas y después decidir qué contar, cómo y en qué formato.</blockquote>
<div class="significado-pares">
<div><p class="etiqueta">En marketing</p><p>Llegar con el mensaje correcto, en el momento correcto.</p></div>
<div><p class="etiqueta">En eventos</p><p>Capturar el instante que no se repite.</p></div>
</div>
</div>
</div>
</section>

<section class="bloque" aria-labelledby="proceso-titulo">
<div class="wrap">
<div class="encabezado-fila">
<h2 id="proceso-titulo" class="t-seccion">Cómo trabajamos</h2>
<a class="enlace-flecha" href="/sobre#proceso">Ver el proceso completo</a>
</div>
{pasos_html()}
</div>
</section>

{llamada_contacto()}'''

# ---------- Para tu negocio ----------
def servicio_html(s):
    foto_html = foto("apaisada", s["foto"], "servicio-" + s["id"]) if s["foto"] else ""
    return f'''<article class="servicio" id="{s['id']}" aria-labelledby="{s['id']}-titulo">
<div class="servicio-titulo">
<h2 id="{s['id']}-titulo" class="t-sub" style="font-size: clamp(30px, 3.2vw, 40px); line-height: 1.08">{s['nombre']}</h2>
<p class="suave">{s['resumen']}</p>
{foto_html}
</div>
<div class="servicio-detalle">
<div class="ancho"><h3>Lo que resuelve</h3><p class="necesidad">{s['necesidad']}</p></div>
<div><h3>Cómo te ayudamos</h3><p>{s['ayuda']}</p>
<p style="margin-top: 20px"><a class="enlace-flecha" href="/contacto?servicio={quote(s['nombre'])}#negocio">Consultar por este servicio</a></p></div>
<div><h3>Puede incluir</h3><ul class="lista-guion">{"".join(f"<li>{x}</li>" for x in s['incluye'])}</ul></div>
</div>
</article>'''

negocio = f'''<section class="cabecera-pagina" aria-labelledby="negocio-titulo">
<div class="wrap">
{migas("Para tu negocio")}
<div class="cabecera-pagina-grid">
<div class="pila">
<h1 id="negocio-titulo" class="t-pagina">Para tu negocio</h1>
<p class="entrada">Te ayudamos a comunicar lo que vendes con claridad y constancia. El marketing y el contenido van al centro; la fotografía y el video aportan imágenes propias y cuidadas.</p>
</div>
<nav aria-label="Servicios en esta página">
<ul class="lista-guion">
{"".join(f'<li><a href="#{s["id"]}">{s["nombre"]}</a></li>' for s in SERVICIOS)}
<li><a href="#formas">Proyecto puntual o acompañamiento mensual</a></li>
</ul>
</nav>
</div>
</div>
</section>

<section class="fondo-blanco bloque" aria-label="Servicios">
<div class="wrap">
{"".join(servicio_html(s) for s in SERVICIOS)}
</div>
</section>

<section id="formas" class="bloque" aria-labelledby="formas-titulo">
<div class="wrap">
<div class="pila" style="margin-bottom: clamp(32px, 4vw, 56px)">
<h2 id="formas-titulo" class="t-seccion">Dos formas de trabajar juntos</h2>
<p class="entrada suave">Puedes contratar un servicio por separado o combinarlos. El alcance, la cantidad de piezas y los plazos se definen contigo en la propuesta.</p>
</div>
<div class="formas">
<div class="forma">
<p class="etiqueta">Proyecto puntual</p>
<h3 class="t-sub">Para un objetivo concreto, con inicio y cierre</h3>
<p class="suave">Ideal cuando necesitas resolver algo específico en una fecha determinada.</p>
<ul class="combos">
<li><strong>Lanzamiento</strong><span>Estrategia de comunicación, sesión de producto y videos para redes.</span></li>
<li><strong>Renovar tu imagen en redes</strong><span>Fotografía de marca, diseño de publicaciones y un primer calendario de contenido.</span></li>
<li><strong>Campaña</strong><span>Mensajes, piezas gráficas, video promocional y campaña pagada en Meta o Google.</span></li>
</ul>
</div>
<div class="forma forma--mensual">
<p class="etiqueta">Acompañamiento mensual</p>
<h3 class="t-sub">Para mantener tu marca activa y medir cómo avanza</h3>
<p class="suave">Trabajamos contigo de forma continua y ajustamos cada mes según los resultados.</p>
<ul class="combos">
<li><strong>Contenido y redes</strong><span>Planificación mensual, diseño, textos y programación de publicaciones.</span></li>
<li><strong>Contenido con producción propia</strong><span>Lo anterior, más sesiones de fotografía y video para tener material nuevo.</span></li>
<li><strong>Marketing completo</strong><span>Estrategia, redes, producción y campañas pagadas, con revisión de resultados.</span></li>
</ul>
</div>
</div>
</div>
</section>

<section class="sobre-jade bloque--corto" aria-label="Pedir una propuesta">
<div class="wrap encabezado-fila" style="margin-bottom: 0">
<p class="t-sub" style="font-family: var(--serif); max-width: 22em">Cuéntanos qué servicio te interesa y qué quieres lograr. Te respondemos con una propuesta.</p>
<a class="btn btn-principal" href="/contacto#negocio">{ico(I_WA, 20, 1.8)}Armar mi mensaje para WhatsApp</a>
</div>
</section>'''

# ---------- Para tus momentos ----------
momentos = f'''<section class="cabecera-pagina" aria-labelledby="momentos-titulo">
<div class="wrap">
{migas("Para tus momentos")}
<div class="cabecera-pagina-grid">
<div class="pila">
<h1 id="momentos-titulo" class="t-pagina">Para tus momentos</h1>
<p class="entrada">Fotografía y video para las fechas que quieres recordar tal como fueron: una sesión pensada para ti o la cobertura completa de tu celebración.</p>
{nota("en el documento del proyecto, la línea de eventos aparece como «a futuro». Confirma que ya se puede reservar, qué tipos de sesión ofreces y cómo se entregan las fotos y videos.")}
</div>
{foto("alta", "sesión o celebración fotografiada por Kairós Studio", "momentos")}
</div>
</div>
</section>

<section class="fondo-blanco bloque" aria-label="Sesiones y cobertura">
<div class="wrap momentos-grid">
<article class="momento" aria-labelledby="sesiones-titulo">
<h2 id="sesiones-titulo" class="t-seccion">Sesiones fotográficas</h2>
<p>Una sesión con tiempo y sin prisa, en un lugar que tenga sentido para ti, para tu pareja o para tu familia.</p>
<ul class="lista-guion">{"".join(f"<li>{x}</li>" for x in SESIONES)}</ul>
<p><a class="enlace-flecha" href="/contacto?trabajo={quote('Sesión fotográfica')}#momentos">Consultar por una sesión</a></p>
</article>
<article class="momento" aria-labelledby="cobertura-titulo">
<h2 id="cobertura-titulo" class="t-seccion">Cobertura de celebraciones</h2>
<p>Fotografía, video o ambos durante tu evento, con edición posterior y entrega de los archivos finales.</p>
<ul class="tipos">{"".join(f"<li><strong>{n}</strong><span>{d}</span></li>" for n, d in COBERTURAS)}</ul>
<p><a class="enlace-flecha" href="/contacto?trabajo={quote('Cobertura de un evento')}#momentos">Consultar por una fecha</a></p>
</article>
</div>
</section>

<section class="bloque" aria-labelledby="alcance-titulo">
<div class="wrap alcance">
<div class="pila">
<h2 id="alcance-titulo" class="t-seccion">Qué incluye y qué no</h2>
<p class="suave">Para que sepas desde el inicio con qué cuentas.</p>
</div>
<div class="pila-l">
<div><h3 class="etiqueta" style="font-family: var(--sans); margin-bottom: 8px">Nos encargamos de</h3>
<ul class="lista-guion"><li>Fotografía de la sesión o del evento</li><li>Grabación y edición de video, si lo eliges</li><li>Edición de las imágenes y entrega de los archivos finales</li></ul></div>
<div><h3 class="etiqueta" style="font-family: var(--sans); margin-bottom: 8px">No incluimos</h3>
<p class="suave">Organización del evento, decoración, catering ni coordinación de proveedores. Si tienes un organizador, acordamos con esa persona los horarios de la cobertura.</p></div>
</div>
</div>
</section>

<section class="sobre-jade bloque--corto" aria-label="Consultar una fecha">
<div class="wrap encabezado-fila" style="margin-bottom: 0">
<p class="t-sub" style="font-family: var(--serif); max-width: 22em">Cuéntanos el tipo de sesión o evento, la fecha y el lugar, y te confirmamos disponibilidad.</p>
<a class="btn btn-principal" href="/contacto#momentos">{ico(I_WA, 20, 1.8)}Armar mi mensaje para WhatsApp</a>
</div>
</section>'''

# ---------- Proyectos ----------
CATEGORIAS = [("marketing", "Marketing y redes"), ("fotografia", "Fotografía comercial"),
              ("video", "Video"), ("momentos", "Sesiones y eventos")]

def proyecto_pendiente(cat, etiqueta):
    return f'''<article class="proyecto" data-categoria="{cat}">
{foto("apaisada", f"imagen del proyecto de {etiqueta.lower()}", "proyecto-" + cat)}
<p class="proyecto-cat">{etiqueta}</p>
<h3 class="t-sub">[Nombre del proyecto]</h3>
<dl>
<div><dt>Cliente</dt><dd class="pendiente-txt">Pendiente: nombre o tipo de negocio, con su permiso</dd></div>
<div><dt>Necesidad</dt><dd class="pendiente-txt">Pendiente: qué problema u objetivo tenía</dd></div>
<div><dt>Qué hicimos</dt><dd class="pendiente-txt">Pendiente: la intervención de Kairós Studio</dd></div>
<div><dt>Entregables</dt><dd class="pendiente-txt">Pendiente: piezas, fotos o videos entregados</dd></div>
</dl>
</article>'''


PROYECTOS_REALES = []  # Cuando haya proyectos reales con permiso del cliente, se agregan aquí.

def lista_proyectos():
    if REVISION or PROYECTOS_REALES:
        return f'''<section class="fondo-blanco bloque" aria-labelledby="lista-titulo">
<div class="wrap">
<h2 id="lista-titulo" class="visually-hidden">Lista de proyectos</h2>
<div class="filtros" role="group" aria-label="Filtrar proyectos por categoría">
<button class="filtro" type="button" data-filtro="todos" aria-pressed="true">Todos</button>
{"".join(f'<button class="filtro" type="button" data-filtro="{c}" aria-pressed="false">{e}</button>' for c, e in CATEGORIAS)}
</div>
<p id="estado-filtro" class="estado-filtro" aria-live="polite"></p>
<div class="proyectos">
{"".join(proyecto_pendiente(c, e) for c, e in CATEGORIAS)}
</div>
</div>
</section>'''
    enlaces = {"marketing": "/negocio#marketing", "fotografia": "/negocio#fotografia", "video": "/negocio#video", "momentos": "/momentos"}
    tarjetas = "".join(f'''<article class="proyecto">{foto("apaisada", e.lower(), "proyecto-" + c)}<h3 class="t-sub">{e}</h3><p><a class="enlace-flecha" href="{enlaces[c]}">Ver el servicio</a></p></article>''' for c, e in CATEGORIAS)
    galeria = f'''<h2 id="categorias-titulo" class="visually-hidden">Categorías</h2><div class="proyectos" style="margin-top: clamp(40px, 5vw, 64px)">{tarjetas}</div>''' if any(hay_foto("proyecto-" + c) for c, _ in CATEGORIAS) else ""
    return f'''<section class="fondo-blanco bloque" aria-labelledby="pronto-titulo">
<div class="wrap"><div class="pila medida">
{greca()}
<h2 id="pronto-titulo" class="t-sub">Estamos reuniendo los primeros proyectos</h2>
<p class="suave">Aquí verás cada trabajo con lo que necesitaba el cliente, lo que hicimos y lo que entregamos. Mientras tanto, puedes seguir a Kairós Studio en Instagram o escribirnos para conversar sobre tu proyecto.</p>
<div class="botones"><a class="btn btn-principal" href="/contacto">Pedir una propuesta</a><a class="btn btn-linea" href="{IG}" {EXT}>Ver Instagram{NUEVA}</a></div>
</div>
{galeria}
</div>
</section>'''

proyectos = f'''<section class="cabecera-pagina" aria-labelledby="proyectos-titulo">
<div class="wrap">
{migas("Proyectos")}
<div class="pila">
<h1 id="proyectos-titulo" class="t-pagina">Proyectos</h1>
<p class="entrada">Cada proyecto muestra qué necesitaba el cliente, qué hicimos y qué entregamos. Los resultados aparecen solo cuando hay datos reales que los respalden.</p>
{nota("aún no hay proyectos publicados. Cada ficha de abajo es un espacio reservado para un trabajo real, con sus fotos, la autorización del cliente y, si existen, resultados medibles.")}
</div>
</div>
</section>

{lista_proyectos()}

{llamada_contacto()}'''

# ---------- Sobre Kairós ----------
sobre = f'''<section class="cabecera-pagina" aria-labelledby="sobre-titulo">
<div class="wrap">
{migas("Sobre Kairós")}
<div class="cabecera-pagina-grid">
<div class="pila">
<h1 id="sobre-titulo" class="t-pagina">Sobre Kairós Studio</h1>
<p class="entrada">En griego, <em>kairós</em> es el momento oportuno: el instante exacto en que algo importante sucede. En marketing, es llegar con el mensaje correcto en el momento correcto. En una celebración, es capturar el instante que no se repite.</p>
</div>
{foto("cuadrada", "retrato o espacio de trabajo de Kairós Studio", "sobre")}
</div>
</div>
</section>

<section class="fondo-blanco bloque" aria-labelledby="enfoque2-titulo">
<div class="wrap">
<h2 id="enfoque2-titulo" class="t-seccion" style="margin-bottom: clamp(32px, 4vw, 56px)">Nuestro enfoque</h2>
<div class="enfoque">
<div class="pila-s">{foto("apaisada", "conversación con un cliente", "enfoque-entender")}<h3 class="t-sub">Primero entender</h3><p class="suave">Antes de proponer, escuchamos: qué vendes o qué celebras, a quién quieres llegar y qué tienes hoy.</p></div>
<div class="pila-s">{foto("apaisada", "planificación visual de un proyecto", "enfoque-intencion")}<h3 class="t-sub">Contar con intención</h3><p class="suave">Estrategia, imagen y texto trabajan juntos. Cada pieza tiene un propósito y un lugar donde se va a usar.</p></div>
<div class="pila-s">{foto("apaisada", "revisión del material junto al cliente", "enfoque-acompanar")}<h3 class="t-sub">Acompañar el proceso</h3><p class="suave">Te explicamos cada paso con claridad, revisamos contigo antes de entregar y te dejamos el material listo para usar.</p></div>
</div>
</div>
</section>

<section id="proceso" class="bloque" aria-labelledby="proceso2-titulo">
<div class="wrap">
<div class="pila" style="margin-bottom: clamp(32px, 4vw, 56px)">
<h2 id="proceso2-titulo" class="t-seccion">Cómo trabajamos</h2>
<p class="entrada suave">Cuatro pasos, igual para un negocio que para una sesión o un evento.</p>
</div>
{pasos_html()}
</div>
</section>

<section class="fondo-papel bloque" aria-label="Misión y visión">
<div class="wrap mv">
<div class="pila">{greca()}<h2 class="t-sub">Misión</h2><p class="grande">Hacemos crecer marcas y capturamos los momentos que cuentan. Unimos estrategia digital, contenido, fotografía y video para que negocios y personas cuenten sus historias con intención, lleguen a quien deben llegar y conserven lo que no se repite.</p></div>
<div class="pila">{greca()}<h2 class="t-sub">Visión</h2><p class="grande">Ser el aliado creativo que acompaña a marcas y personas en cada etapa importante de su historia, desde el primer lanzamiento hasta la celebración de sus logros.</p></div>
</div>
</section>

{llamada_contacto()}'''

# ---------- Contacto ----------
OPC_SERVICIO = [s["nombre"] for s in SERVICIOS] + ["Varios servicios", "Aún no lo sé"]
OPC_TRABAJO = SESIONES + ["Sesión fotográfica", "Boda", "Graduación", "Bautizo", "Conferencia", "Cobertura de un evento", "Otro"]

def opciones(lista, placeholder):
    return f'<option value="">{placeholder}</option>' + "".join(f'<option>{o}</option>' for o in lista)

contacto = f'''<section class="cabecera-pagina" aria-labelledby="contacto-titulo" style="padding-bottom: clamp(32px, 4vw, 56px)">
<div class="wrap">
{migas("Contacto")}
<div class="pila">
<h1 id="contacto-titulo" class="t-pagina">Contacto</h1>
<p class="entrada">La forma más rápida de hablar con nosotros es WhatsApp. Elige tu caso, completa unos datos y se abrirá WhatsApp con el mensaje listo para que lo envíes tú.</p>
</div>
</div>
</section>

<section class="bloque--corto" style="padding-top: 0" aria-label="Armar mensaje de WhatsApp">
<div class="wrap contacto-grid">

<div class="panel" id="negocio">
<h2 class="t-sub">Para tu negocio</h2>
<p class="suave">Cuéntanos qué servicio te interesa y qué quieres lograr.</p>
<form data-whatsapp="negocio" novalidate>
<div class="campo">
<label for="n-servicio">Servicio de interés</label>
<select id="n-servicio" name="servicio" aria-describedby="error-n-servicio" data-obligatorio="Elige un servicio o «Aún no lo sé».">{opciones(OPC_SERVICIO, "Elige una opción")}</select>
<p id="error-n-servicio" class="error"></p>
</div>
<div class="campo">
<label for="n-objetivo">¿Qué quieres lograr?</label>
<p id="ayuda-n-objetivo" class="ayuda">Por ejemplo: lanzar un producto, vender más por Instagram, renovar tus fotos.</p>
<textarea id="n-objetivo" name="objetivo" aria-describedby="ayuda-n-objetivo error-n-objetivo" data-obligatorio="Escribe en pocas palabras qué quieres lograr."></textarea>
<p id="error-n-objetivo" class="error"></p>
</div>
<div class="campo">
<label for="n-negocio">Nombre de tu negocio <span class="suave">(opcional)</span></label>
<input id="n-negocio" name="negocio" type="text" autocomplete="organization">
</div>
<div class="pila-s"><p class="vista-titulo">Así se verá tu mensaje</p><p class="vista-previa" aria-live="polite"></p></div>
<a class="btn btn-principal abrir-whatsapp" href="{WA_NEGOCIO}" {EXT}>{ico(I_WA, 20, 1.8)}Abrir WhatsApp con este mensaje{NUEVA}</a>
<p class="aclaracion">El mensaje no se envía desde esta página: lo revisas y lo envías tú en WhatsApp.</p>
</form>
</div>

<div class="panel panel--momentos" id="momentos">
<h2 class="t-sub">Para una sesión o evento</h2>
<p class="suave">Cuéntanos el tipo de trabajo, la fecha y el lugar.</p>
<form data-whatsapp="momentos" novalidate>
<div class="campo">
<label for="m-trabajo">Tipo de trabajo</label>
<select id="m-trabajo" name="trabajo" aria-describedby="error-m-trabajo" data-obligatorio="Elige el tipo de sesión o evento.">{opciones(OPC_TRABAJO, "Elige una opción")}</select>
<p id="error-m-trabajo" class="error"></p>
</div>
<div class="campo">
<label for="m-fecha">Fecha</label>
<p id="ayuda-m-fecha" class="ayuda">Si aún no es definitiva, escribe una aproximada.</p>
<input id="m-fecha" name="fecha" type="text" aria-describedby="ayuda-m-fecha error-m-fecha" data-obligatorio="Escribe la fecha, aunque sea aproximada.">
<p id="error-m-fecha" class="error"></p>
</div>
<div class="campo">
<label for="m-lugar">Lugar</label>
<p id="ayuda-m-lugar" class="ayuda">Ciudad, sector o nombre del lugar.</p>
<input id="m-lugar" name="lugar" type="text" aria-describedby="ayuda-m-lugar error-m-lugar" data-obligatorio="Escribe dónde será.">
<p id="error-m-lugar" class="error"></p>
</div>
<div class="campo">
<label for="m-detalles">Detalles <span class="suave">(opcional)</span></label>
<textarea id="m-detalles" name="detalles" placeholder="Cantidad aproximada de invitados, si prefieres foto, video o ambos…"></textarea>
</div>
<div class="pila-s"><p class="vista-titulo">Así se verá tu mensaje</p><p class="vista-previa" aria-live="polite"></p></div>
<a class="btn btn-principal abrir-whatsapp" href="{WA_MOMENTOS}" {EXT}>{ico(I_WA, 20, 1.8)}Abrir WhatsApp con este mensaje{NUEVA}</a>
<p class="aclaracion">El mensaje no se envía desde esta página: lo revisas y lo envías tú en WhatsApp.</p>
</form>
</div>

</div>
</section>

<section class="fondo-blanco bloque--corto" aria-label="Datos de contacto">
<div class="wrap datos-directos">
<div><h2>WhatsApp</h2><p><a href="{WA_GENERAL}" {EXT}>{TEL_VISIBLE}{NUEVA}</a></p></div>
<div><h2>Redes</h2>{redes()}</div>
<div><h2>Ubicación</h2><p>Quito, Ecuador</p>{nota("correo electrónico de contacto y si atiendes fuera de Quito.")}</div>
</div>
</section>'''

# ---------- 404 ----------
no_encontrada = f'''<section class="bloque">
<div class="wrap pila no-encontrada">
{greca()}
<h1 class="t-pagina">No encontramos esta página</h1>
<p class="entrada suave">Puede que la dirección haya cambiado. Desde aquí puedes volver al inicio o ir directo a lo que buscas.</p>
<div class="botones"><a class="btn btn-oscuro" href="/">Volver a Inicio</a><a class="btn btn-linea" href="/negocio">Para tu negocio</a><a class="btn btn-linea" href="/momentos">Para tus momentos</a></div>
</div>
</section>'''

# =====================================================================
PAGINAS = {
    "index.html": ("/", f"{NOMBRE} · Marketing digital, fotografía y video en Quito",
                   "Estudio creativo en Quito: marketing digital, gestión de redes, fotografía comercial y video para negocios; sesiones y cobertura de celebraciones.",
                   "inicio", inicio, JSONLD),
    "negocio.html": ("/negocio", f"Marketing, redes, fotografía y video para negocios · {NOMBRE}",
                     "Marketing digital, gestión de redes y contenido, fotografía comercial y de producto, y video para redes y campañas. Proyectos puntuales o acompañamiento mensual en Quito.",
                     "negocio", negocio, ""),
    "momentos.html": ("/momentos", f"Sesiones fotográficas y cobertura de eventos · {NOMBRE}",
                      "Sesiones fotográficas y cobertura en foto y video de bodas, graduaciones, bautizos y conferencias en Quito.",
                      "momentos", momentos, ""),
    "proyectos.html": ("/proyectos", f"Proyectos · {NOMBRE}",
                       "Trabajos de Kairós Studio por categoría: qué necesitaba cada cliente, qué hicimos y qué entregamos.",
                       "proyectos", proyectos, ""),
    "sobre.html": ("/sobre", f"Sobre nosotros y cómo trabajamos · {NOMBRE}",
                   "Qué significa kairós, nuestro enfoque creativo y los cuatro pasos con los que trabajamos: consulta, propuesta, producción y entrega.",
                   "sobre", sobre, ""),
    "contacto.html": ("/contacto", f"Contacto por WhatsApp · {NOMBRE}",
                      "Escríbenos por WhatsApp para pedir una propuesta para tu negocio o consultar una fecha para tu sesión o evento en Quito.",
                      "contacto", contacto, ""),
    "404.html": ("/404", f"Página no encontrada · {NOMBRE}", "La página que buscas no existe.", None, no_encontrada, ""),
}

if __name__ == "__main__":
    for archivo, (ruta, titulo, desc, activa, cuerpo, extra) in PAGINAS.items():
        with open(os.path.join(RAIZ, archivo), "w", encoding="utf-8") as f:
            f.write(pagina(ruta, titulo, desc, activa, cuerpo, extra))
    rutas = [r for r, *_ in PAGINAS.values() if r != "/404"]
    with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{SITIO}{r}</loc></url>\n" for r in rutas) + "</urlset>\n")
    print("Páginas generadas:", ", ".join(PAGINAS))
