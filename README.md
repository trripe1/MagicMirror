# MagicMirror² — Setup Valencia

Configuración personal de [MagicMirror²](https://magicmirror.builders/) con sistema multipágina, cotizaciones en tiempo real, Spotify, galería de imágenes y control remoto vía API REST.

---

## Estructura de páginas

| Página | Módulos | Descripción |
|--------|---------|-------------|
| **1 — Inicio** | `clock` · `compliments` · `weather` | Reloj, meteorología Valencia, frases |
| **2 — Finanzas** | `MMM-Jast` · `MMM-Spotify` | Cotizaciones (Yahoo Finance) + reproductor Spotify |
| **3 — Galería** | `MMM-SmartWebDisplay` | Carrusel de imágenes local |

**Módulos fijos** (visibles en todas las páginas): `alert` · `MMM-Remote-Control` · `MMM-Page-Indicator` · `newsfeed`

---

## Requisitos

- Node.js >= 20
- npm >= 10
- Cuenta de [OpenWeatherMap](https://openweathermap.org/api) (plan gratuito válido)
- Cuenta de [Spotify Developer](https://developer.spotify.com/dashboard) (para MMM-Spotify)

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/trripe1/MagicMirror
cd MagicMirror
npm install
```

### 2. Instalar los módulos custom

```bash
cd modules

# Sistema multipágina
git clone https://github.com/edward-shen/MMM-pages.git
cd MMM-pages && npm install && cd ..

# Indicador de página
git clone https://github.com/edward-shen/MMM-page-indicator.git MMM-Page-Indicator
cd MMM-Page-Indicator && npm install && cd ..

# Panel de control remoto
git clone https://github.com/Jopyth/MMM-Remote-Control.git
cd MMM-Remote-Control && npm install && cd ..

# Cotizaciones (sin API key, usa Yahoo Finance)
git clone https://github.com/jalibu/MMM-Jast.git
cd MMM-Jast && npm install && cd ..

# Reproductor Spotify
git clone https://github.com/skuethe/MMM-Spotify.git
cd MMM-Spotify && npm install && cd ..

# Visor de imágenes / URLs
git clone https://github.com/AgP42/MMM-SmartWebDisplay.git
cd MMM-SmartWebDisplay && npm install && cd ..

cd ..
```

### 3. Configurar

```bash
cp config/config.js.sample config/config.js
```

Edita `config/config.js` y reemplaza `YOUR_OPENWEATHERMAP_API_KEY` con tu clave de [OpenWeatherMap](https://openweathermap.org/api).

### 4. Galería de imágenes

Copia tus imágenes en `modules/MMM-SmartWebDisplay/imagenes_a_mostrar/` con los nombres `img1.jpg` … `img7.jpg` (el carrusel cambia cada minuto).

---

## Configuración de Spotify

Crea una app en [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) con la **Redirect URI**: `http://TU_IP_LOCAL:8888/callback`

Crea el archivo `modules/MMM-Spotify/spotify.config.json` (usa `spotify.config.json.example-single` como referencia):

```json
[
  {
    "USERNAME": "tu_usuario_spotify",
    "CLIENT_ID": "tu_client_id",
    "CLIENT_SECRET": "tu_client_secret",
    "TOKEN": "./USERNAME_token.json",
    "REDIRECT_URI": "http://TU_IP_LOCAL:8888/callback"
  }
]
```

Autentica (solo la primera vez):

```bash
node modules/MMM-Spotify/auth_windows.js
```

---

## Arranque

```bash
npm start
```

Accesible en `http://localhost:8080`

---

## Control remoto

| Recurso | URL |
|---------|-----|
| Panel de control | `http://localhost:8080/remote.html` |
| Panel de páginas | `http://localhost:8080/modules/MMM-Remote-Control/PAGINAS.html` |
| Cambiar página (API) | `POST /api/notification/PAGE_CHANGED` · body: `{"payload": 0\|1\|2}` |
| Página siguiente | `POST /api/notification/PAGE_INCREMENT` |
| Página anterior | `POST /api/notification/PAGE_DECREMENT` |

---

## Módulos adicionales instalados (no activos en config)

Están instalados pero no incluidos en `config.js`. Se pueden activar añadiéndolos al array `modules`:

| Módulo | Repo |
|--------|------|
| MMM-Carousel | https://github.com/shbatm/MMM-Carousel |
| MMM-OpenWeatherForecast | https://github.com/jclarke0000/MMM-OpenWeatherForecast |
| MMM-CardDavBirthdaysProvider | https://github.com/ulrichwisser/MMM-CardDavBirthdaysProvider |

---

## Licencia

Configuración personal sobre [MagicMirror²](https://github.com/MagicMirrorOrg/MagicMirror), distribuido bajo licencia MIT.
