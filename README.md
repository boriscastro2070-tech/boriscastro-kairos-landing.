# Kairós · Landing page

Sitio estático de **Kairós** — *Marcas que crecen, momentos que cuentan.*

## Estructura
- `index.html` — la página completa (HTML + CSS, sin dependencias ni build).
- `assets/` — logos, favicon e imagen para compartir en redes.
- `vercel.json` — configuración de Vercel (URLs limpias y caché de imágenes).

## Pendientes antes de publicar
- Reemplazar `https://wa.me/` por `https://wa.me/593XXXXXXXXX` (tu número, sin `+` ni espacios).
- Completar `[TU NÚMERO DE WHATSAPP]` y `[TU CORREO]`.
- Enlazar Instagram, TikTok y Facebook en el pie de página.
- Sustituir los espacios `[FOTO DE PROYECTO]` del portafolio por imágenes reales.

## Despliegue
Vercel detecta el sitio como estático: sin comando de build y con el directorio raíz como salida.
Cada `git push` a `main` publica una nueva versión.
