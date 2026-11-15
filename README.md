<div align="center">

<img src="assets/hero.svg" alt="Feed Folio animated illustration" width="100%"/>

# Feed Folio

**A standard-library feed reader that exports a clean Markdown digest.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-2F855A.svg)](LICENSE)

</div>

## Why it exists

Turn noisy RSS and Atom feeds into a calm reading list. Reads RSS 2.0 and Atom XML from a URL or local file. It does not persist subscriptions, deduplicate across runs or execute feed-provided HTML.

## Features

- RSS and Atom entry parsing
- Local XML files or remote feeds
- Readable Markdown output
- Request timeout and 2 MB response cap

## Quick start

Python 3.10+; no third-party packages.

```bash
git clone https://github.com/MofidChallenge10/feed-folio.git
cd feed-folio
python tool.py --help
```

### Example

```bash
python tool.py https://example.com/feed.xml --limit 12
```

## Self-test

```bash
python tool.py --self-test
```

The self-test uses the standard-library `unittest` module and does not contact external services.

## Scope and safety

Reads RSS 2.0 and Atom XML from a URL or local file. It does not persist subscriptions, deduplicate across runs or execute feed-provided HTML. Review output before using it in production workflows.

## Design notes

The illustration is an original lightweight SVG. Its motion is decorative only and respects `prefers-reduced-motion`; the CLI itself stays plain and pipe-friendly.

## Contributing

Issues and pull requests are welcome. Keep the standard-library-first approach, add focused tests for behavior changes, and update examples when options change.

## License

MIT — see [LICENSE](LICENSE).
