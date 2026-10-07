# jasontrost.com

Source for [jasontrost.com](https://jasontrost.com), a static personal site hosted on GitHub Pages.

## Structure

- `index.html`, `about.html`, `media.html` — main pages
- `notes/` — notes index, posts, and RSS feed (`notes/rss.xml`)
- `style.css` — all styling
- `fonts/` — self-hosted woff2 fonts (Cormorant, Hanken Grotesk)
- `sitemap.xml`, `robots.txt`, `CNAME` — SEO and custom-domain config
- Images live at the repo root and in `notes/images/`

## Local development

No build step, but the site uses root-relative paths (`/style.css`, `/about.html`), so opening files directly via `file://` renders unstyled. Serve the directory instead:

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Deployment

Pushing to `main` deploys automatically via GitHub Pages. The site is served at the custom domain in `CNAME`.

## Caching

The site sits behind Cloudflare, which caches `style.css` for four hours. Every page links the stylesheet with a version query (`/style.css?v=YYYYMMDD`). Bump that value on all pages whenever you change the CSS, or the live site will serve the old styles until the cache expires.

## Adding a note

1. Create `notes/<slug>.html` (copy an existing post for the page structure and meta tags).
2. Add a card linking to it in `notes/index.html`.
3. Add an `<item>` to `notes/rss.xml`.
4. Add a `<url>` entry to `sitemap.xml`.
