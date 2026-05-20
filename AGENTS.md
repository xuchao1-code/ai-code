# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal Python CLI application (`ai-code`) with zero third-party dependencies.

### Running & Testing

- **Install**: `pip install -e .` (editable mode from `pyproject.toml`)
- **Run CLI**: `ai-code --name Cursor` or `PYTHONPATH=src python3 -m ai_code --name Cursor`
- **Run tests**: `PYTHONPATH=src python3 -m unittest discover -s tests -v`

### Gotchas

- The `ai-code` console script installs to `~/.local/bin`. Ensure this is on `PATH` (it is by default in the Cloud Agent VM).
- There is no linter or formatter configured in `pyproject.toml` as a project dependency. The `.gitignore` references `.ruff_cache/` and `.mypy_cache/`, suggesting ruff and mypy may be used ad-hoc but are not required.
- There is no `requirements.txt` or lock file; `pyproject.toml` is the sole dependency definition.
