# ai-code

A basic Python application scaffold using a `src/` package layout.

## Requirements

- Python 3.11+

## Run

Run from the repository root:

```bash
PYTHONPATH=src python -m ai_code --name Cursor
```

Or install the package locally and use the console script:

```bash
python -m pip install -e .
ai-code --name Cursor
```

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests
```
