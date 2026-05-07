# Copilot Instructions for `Kharapsy`

## Build, test, lint, and maintenance commands

Use these from the repository root.

| Task | Command |
| --- | --- |
| Install Python deps | `pip install -r requirements.txt` |
| Run CLI app locally | `python3 src/app.py` |
| Build Docker image | `make docker-build` |
| Start app + MySQL via Compose | `make up` |
| Stop Compose services | `make down` |
| Show Compose logs | `make logs` |
| List goodbye messages | `make list` |
| Add goodbye message | `make add-message message="Your message"` |
| Remove goodbye message | `make remove-message message="Your message"` |
| Update goodbye message | `make update-message old_message="Old" new_message="New"` |
| Run full test suite | Not configured in this repository |
| Run a single test | Not configured in this repository |
| Run linter | Not configured in this repository |

Note: this repository uses a lowercase `makefile`, so use `make` from the repo root (as shown above).

## High-level architecture

This repo currently centers on one application:

1. **Python CLI assistant (`src/`)**: `src/app.py` is a menu-driven entrypoint that dispatches to feature modules (`start_knowledge_base`, `start_media_controller`, `start_scheduler`, `start_voice_recognition`, `scraper_configuration`). This part is intentionally retained as a long-term backlog project.

For the Python app:

- Runtime config is file-based under `config/`.
- `src/contact_scraper.py` scrapes user-provided HTML selectors, then persists rows into MySQL table `contacts` using credentials from `config/db_config.json`.
- `src/goodbye_module.py` loads `config/messages_config.json` once at import, shuffles messages, and emits one message per exit call.
- Docker runtime is defined by `Dockerfile` + `docker-compose.yml` (service name `mysql` must match DB host used in `db_config.json`).

## Key codebase conventions

- **Feature module contract**: menu features are expected to expose `start_<feature>()` in their module; `app.py` imports and calls these directly.
- **Config path convention in `src/`**: modules resolve config paths relative to the module file with `os.path.dirname(__file__)` + `.. / config / ...`, not absolute paths.
- **Message storage contract**: goodbye messages are stored under `BASE_GOODBYE_MESSAGES` in `config/messages_config.json`; helper scripts in `bin/` read/write that exact key.
- **Script execution context**: `bin/list_messages.py` and `bin/update_messages.py` use `config/messages_config.json` as a repo-root-relative path, so they should be run from repository root (as Make targets do).
