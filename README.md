# Kairós · Sitio web

Sitio estático de **Kairós** — *Marcas que crecen, momentos que cuentan.*
Publicado en https://kairos-studio-ec.vercel.app

## Páginas
| URL | Archivo | Contenido |
|---|---|---|
| `/` | `index.html` | Portada, ¿Por qué kairós?, resúmenes de Servicios, Eventos y Portafolio, Misión y Visión (`/#nosotros`) |
| `/servicios` | `servicios.html` | Los 8 servicios y «Cómo trabajamos» (`/servicios#proceso`) |
| `/eventos` | `eventos.html` | Kairós Eventos (próximamente) y tipos de evento |
| `/portafolio` | `portafolio.html` | Trabajos y proyectos |
| — | `404.html` | Página de error con regreso a Inicio |

Todas comparten el mismo menú, la sección de contacto (WhatsApp + redes) y el pie de página.
Los enlaces antiguos de la página única (`/#servicios`, `/#eventos`, `/#portafolio`, `/#proceso`) redirigen a su nueva página.

## Estructura
- `css/site.css` — estilos compartidos (colores, tipografías, componentes).
- `js/site.js` — menú desplegable en celular.
- `assets/` — logos, favicon e imagen para compartir en redes.
- `vercel.json` — URLs limpias (`/servicios` en lugar de `/servicios.html`) y caché de imágenes.

> El menú, el contacto y el pie se repiten en cada página: si cambias uno, cámbialo en los cinco archivos HTML.

## Redes conectadas
- Instagram: https://www.instagram.com/kairos.estudio.ec/
- Facebook: https://www.facebook.com/profile.php?id=61595387390430
- WhatsApp: 098 298 1089

## Pendientes
- Completar `[TU CORREO]` en la sección de contacto.
- Sustituir los espacios `[FOTO DE PROYECTO]` y `[Cliente · Servicio]` del portafolio por trabajos reales.

## Despliegue
Sin comando de build: Vercel sirve los archivos tal cual. Cada `git push` a `main` publica una nueva versión.
