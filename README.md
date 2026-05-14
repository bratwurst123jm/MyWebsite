<div align="center">
  <img src="profile-avatar.png" alt="Profile Avatar" width="120" height="120" style="border-radius: 50%; border: 3px solid #0a0a0f;">

  # Modern Link-in-Bio Template

  <p>
    <strong>Ein modernes, erweitertes Link-in-Bio Template</strong><br>
    Dark Theme · Glassmorphismus · Animierte Partikel · Responsive
  </p>

  <p>
    <a href="#✨-features">Features</a> •
    <a href="#🚀-quick-start">Quick Start</a> •
    <a href="#🎨-customization">Customization</a> •
    <a href="#📁-project-structure">Structure</a>
  </p>

  <br>

  ![Preview](profile-avatar.png)
</div>

---

## ✨ Features

- **Dark Theme** — Tiefes Purple/Blue-Farbschema mit Gradient-Orbs
- **Glassmorphismus** — Karten mit `backdrop-filter: blur()` und sanften Übergängen
- **Animierte Partikel** — Canvas-basiertes Partikelsystem mit Verbindungslinien
- **Conic-Gradient Avatar-Ring** — Rotierender Farbverlauf mit Glow-Effekt
- **Status-Badge** — Pulsierender Online-Status-Indikator
- **6 Social-Media-Karten** — X, Instagram, Discord, GitHub, YouTube, Twitch
- **Staggered Entrance** — Gestaffelte Einblende-Animationen
- **Ripple-Effekt** — Klick-Ripple auf allen Karten
- **Responsive** — 4 Breakpoints (360px–1024px+)
- **Barrierefreiheit** — `prefers-reduced-motion`, `focus-visible`, ARIA-Labels
- **CSS Custom Properties** — Einfaches Theming über Design-Tokens
- **Print-Styles** — Saubere Druckansicht

## 🚀 Quick Start

### Variante 1: Direkt im Browser öffnen

```bash
# Einfach die index.html im Browser öffnen
open modern-template/index.html
```

### Variante 2: Mit Python-Server

```bash
cd modern-template
python server.py
```

Dann öffne [http://localhost:7000](http://localhost:7000) im Browser.

### Variante 3: Mit Docker (optional)

```bash
cd modern-template
docker build -t link-in-bio .
docker run -p 27000:27000 link-in-bio
```

## 🎨 Customization

### Profil anpassen

Öffne [`index.html`](index.html) und ändere:

```html
<!-- Profilbild -->
<img src="profile-avatar.png" alt="Dein Name">

<!-- Name und Handle -->
<h1 class="profile-name">Dein Name</h1>
<p class="profile-handle">@deinhandle</p>

<!-- Status -->
<span class="status-badge">
  <span class="status-dot"></span>
  Verfügbar
</span>
```

### Links anpassen

Jede Link-Karte folgt diesem Muster:

```html
<a href="https://deine-url.com" target="_blank" rel="noopener noreferrer"
   class="link-card" data-brand="x">
  <div class="link-icon">
    <!-- SVG Icon -->
  </div>
  <div class="link-info">
    <span class="link-title">Plattform</span>
    <span class="link-desc">Beschreibung</span>
  </div>
  <div class="link-arrow">
    <!-- Pfeil SVG -->
  </div>
</a>
```

### Farben anpassen

Alle Farben sind als CSS-Variablen in [`styles.css`](styles.css) definiert:

```css
:root {
  --bg-primary: #0a0a0f;
  --accent-purple: #7c5cff;
  --accent-pink: #ff6b9d;
  --accent-teal: #00d4aa;
  /* ... */
}
```

## 📁 Project Structure

```
modern-template/
├── profile-avatar.png    # Profilbild (austauschbar)
├── index.html            # Haupt-Template
├── styles.css            # Design-System
├── server.py             # Python HTTP Server
└── README.md             # Diese Dokumentation
```

## 🖥️ Browser Support

| Browser | Support |
|---------|---------|
| Chrome / Edge | ✅ Neueste 2 Versionen |
| Firefox | ✅ Neueste 2 Versionen |
| Safari | ✅ Neueste 2 Versionen |
| Mobile (iOS/Android) | ✅ Voll unterstützt |

## ♿ Accessibility

- Semantische HTML5-Elemente (`<main>`, `<nav>`, `<section>`)
- ARIA-Labels für Navigation und Icons
- `prefers-reduced-motion` deaktiviert Animationen
- `focus-visible` Styles für Tastaturnavigation
- Ausreichende Farbkontraste

## 📱 Responsive Breakpoints

| Breakpoint | Anpassungen |
|-----------|-------------|
| > 768px | Desktop-Layout |
| ≤ 768px | Verkleinerte Abstände |
| ≤ 480px | Mobiles Layout |
| ≤ 360px | Extra-kompakt |

## 📄 License

MIT — Frei verwendbar und anpassbar.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://x.com/bratwurst123jm">@bratwurst123jm</a></sub>
</div>
