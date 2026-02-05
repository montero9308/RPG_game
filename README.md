# RPG Game (Python + OpenGL)

Proyecto público y colaborativo para iniciar un videojuego RPG en Python con OpenGL.
Este repositorio contiene un esqueleto mínimo para comenzar a construir el juego,
con un punto de entrada claro y una estructura simple para crecer por módulos.

## Objetivos iniciales

- Definir una base de juego 2D/3D ligera y extensible.
- Mantener el proyecto abierto a colaboración.
- Proveer un flujo de desarrollo fácil de instalar y ejecutar.

## Tecnologías

- **Python 3.10+**
- **OpenGL** a través de **pyglet** (ventana y contexto gráfico).
- **pygame** y **PyQt6** se incluyen como dependencias opcionales para herramientas
  auxiliares, prototipos o editores, según sea necesario.

## Estructura del proyecto

```
src/
  rpg_game/
    __init__.py
    config.py
    game.py
    localization.py
    locales/
      es.json
      en.json
    main.py
    ui/
      menu.py
```

## Instalación

Se recomienda usar un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-tools.txt
```

También puedes instalar extras con:

```bash
pip install -e ".[tools]"
```

## Ejecutar el juego (esqueleto)

```bash
python -m rpg_game.main
```

Se abrirá una ventana básica con un fondo de color, lista para extender.

## Idiomas

Los textos de la interfaz viven en `src/rpg_game/locales/` con archivos JSON
por idioma (por ejemplo `es.json` y `en.json`). Es un formato extensible para
agregar nuevos idiomas en el futuro.

## Contribuciones

¡Bienvenidas! Por favor abre un issue o pull request con tus ideas o mejoras.

## Licencia

Este proyecto se distribuye bajo la licencia **GNU GPLv3**. Ver [LICENSE](LICENSE).
