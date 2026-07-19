# Scraper de scroll infinito con Selenium

Script que extrae productos de una página con carga dinámica por scroll infinito (sin paginación por URL ni botón "next"), usando Selenium.

## Qué extrae
- Nombre del producto
- Precio
- Link a la ficha individual

## Técnica clave
En vez de esperar un elemento puntual (como en paginación clásica), se usa
una condición personalizada con `lambda` dentro de `WebDriverWait` que compara
la cantidad de elementos cargados antes y después de cada scroll, hasta que
la altura de la página deja de crecer.

## Tecnologías
- Python 3
- Selenium (headless Firefox)
- Pandas (exportación a Excel)

## Cómo correrlo
\`\`\`bash
pip install selenium pandas openpyxl
python proyecto1.py
\`\`\`
