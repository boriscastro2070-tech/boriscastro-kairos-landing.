# Kairós Studio · Sitio web

Estudio creativo en Quito — *Marcas que crecen, momentos que cuentan.*
Producción: https://kairos-studio-ec.vercel.app (rama `main`).

## Páginas
| URL | Archivo | Contenido |
|---|---|---|
| `/` | `index.html` | Lema, los dos recorridos (negocio / momentos), trabajos, enfoque, proceso y contacto |
| `/negocio` | `negocio.html` | 4 servicios (necesidad → ayuda → posibles entregables) y dos formas de trabajar |
| `/momentos` | `momentos.html` | Sesiones fotográficas, cobertura de celebraciones y qué incluye / qué no |
| `/proyectos` | `proyectos.html` | Proyectos por categoría con filtros: cliente, necesidad, qué hicimos, entregables |
| `/sobre` | `sobre.html` | Significado de kairós, enfoque, cómo trabajamos (`#proceso`), misión y visión |
| `/contacto` | `contacto.html` | Asistentes que arman el mensaje de WhatsApp para negocio o para sesión/evento |
| — | `404.html` | Página no encontrada |

Las direcciones anteriores (`/servicios`, `/eventos`, `/portafolio` y los `/#…` de la primera versión) redirigen a las nuevas.

## Cómo editar
Los textos viven en `_src/build.py`. Después de cambiarlos:

```
python3 _src/build.py
```

Esto regenera todos los `.html` y `sitemap.xml`. No edites los `.html` a mano: el siguiente build los sobrescribe.

- `REVISION = True` muestra el aviso superior y las notas «Pendiente de confirmar». **Cámbialo a `False` antes de publicar.**
- Fotos: cada `foto(...)` dibuja un marco «Foto pendiente». Para usar una foto real, guárdala en `assets/` (WebP o JPG, de unos 1600 px de lado como máximo) y reemplaza la llamada por un `<img>` con `alt` descriptivo.
- `css/site.css` contiene la paleta, la tipografía y los componentes. `js/site.js` contiene el menú en celular, los filtros y los mensajes de WhatsApp.

## Datos confirmados
- WhatsApp: 098 298 1089
- Instagram: https://www.instagram.com/kairos.estudio.ec/
- Facebook: https://www.facebook.com/profile.php?id=61595387390430

## Pendiente de contenido real
- Fotos: portada, servicios, sesiones y «Sobre Kairós Studio».
- Proyectos: nombre, cliente (con permiso), necesidad, intervención, entregables y, si existen, resultados medibles.
- Confirmar que la línea de sesiones y eventos ya está disponible, qué sesiones ofreces y cómo entregas el material.
- Correo electrónico y zona de cobertura fuera de Quito.

## Despliegue
Sitio estático, sin build en Vercel (`_src/` y este README no se publican; ver `.vercelignore`).
Un `git push` a `main` publica en producción; cualquier otra rama genera solo una vista previa.
