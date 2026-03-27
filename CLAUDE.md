# CLAUDE.md — rheti-python

Enneagram RHETI test web application. Administers the 144-question test, stores results, and displays type scores.

## Claude Monitor

**Always keep `~/.claude-monitor/rheti-python.json` updated** during non-trivial tasks.

Status file format:
```json
{
  "task_name": "Brief description",
  "status": "in_progress",
  "progress_percent": 45,
  "current_step": "What's happening right now",
  "message": "Optional extra context",
  "needs_attention": false,
  "updated_at": "2026-03-27T12:00:00Z"
}
```

Use the **Write tool** (not Bash) to update this file. Valid statuses: `pending`, `in_progress`, `blocked`, `waiting`, `completed`, `error`.

## Project Structure

```
rheti/
  __init__.py          # Public API: load_questions(), score()
  __main__.py          # CLI test runner
  loader.py            # CSV → Question objects
  scorer.py            # Type scoring + descriptions
  question.py          # Question / Choice classes
  questions.csv        # 144 questions — auto-reloaded on change
pages/                 # Individual PDF pages (for reference/editing)
web/                   # Flask web application (in development)
extract_questions.py   # Pixel-based bracket detection (dev tool)
extract_text_vision.py # Vision LLM text extraction (dev tool)
```

## Question Data

`rheti/questions.csv` — the source of truth. The web app reloads from this file on each new session (mtime-checked), so edits appear immediately without restart.

Columns: `question, choice, text, value`
- `value` is A–I, mapping to Enneagram types (see `rheti/scorer.py` TYPE_MAP)
- q1–q23 are verified ground truth; q24–q144 are OCR-extracted (~91% accuracy)
- **q51, q69, q71, q76, q77** have uncertain column assignments (page 10 of PDF has score sheet overlay)

## Web App (planned)

- **Framework:** Flask + Flask-Login + Flask-Mail + Flask-SQLAlchemy
- **DB:** SQLite (file: `web/rheti.db`) — can migrate to Postgres later
- **Auth:** Email + password with email verification via nthmost.com SMTP
- **Domain:** TBD subdomain of nthmost.com
- **Server:** zephyr (149.28.77.210) via Apache reverse proxy

## DNS

DNS is managed via Gandi for nthmost.com. See `~/projects/nthmost-systems/inventory.md` for current records. The server IP is **149.28.77.210**.

To add a subdomain: use the Gandi LiveDNS API or web interface. SPF already covers this IP.

## Mail

nthmost.com MX is Gandi-hosted. For outbound from the app, use the server's SMTP (port 587 or 465) with credentials from `~/projects/nthmost-systems/.secrets/`.
