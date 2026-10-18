"""Optimiza las fotos reales de _src/fotos-originales/ según _src/fotos.json.

Uso:  python3 _src/optimizar.py   (después: python3 _src/build.py)
Genera assets/fotos/<clave>-800.webp y -1600.webp, corrige la orientación de la cámara,
quita los metadatos (incluida la ubicación GPS) y anota ancho y alto en fotos.json.
Los originales no se suben a GitHub (.gitignore).
"""
import json, os
from PIL import Image, ImageOps

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(RAIZ, "_src", "fotos-originales")
DEST = os.path.join(RAIZ, "assets", "fotos")
JSON = os.path.join(RAIZ, "_src", "fotos.json")

fotos = json.load(open(JSON, encoding="utf-8"))
os.makedirs(DEST, exist_ok=True)
for clave, datos in fotos.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(ORIG, datos["archivo"]))).convert("RGB")
    for ancho in (800, 1600):
        copia = im.copy()
        if copia.width > ancho:
            copia = copia.resize((ancho, round(copia.height * ancho / copia.width)), Image.LANCZOS)
        copia.save(os.path.join(DEST, f"{clave}-{ancho}.webp"), "WEBP", quality=82, method=6)
        if ancho == 1600:
            datos["ancho"], datos["alto"] = copia.size
    print(f"{clave}: {datos['archivo']} -> {datos['ancho']}x{datos['alto']}")
json.dump(fotos, open(JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
