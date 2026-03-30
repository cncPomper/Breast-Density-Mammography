# Breast-Density-Mammography

![PyPI version](https://img.shields.io/pypi/v/Breast-Density-Mammography.svg)

Breast Density on X-Ray Mammography

* [GitHub](https://github.com/cncPomper/Breast-Density-Mammography/) | [PyPI](https://pypi.org/project/Breast-Density-Mammography/) | [Documentation](https://cncPomper.github.io/Breast-Density-Mammography/)
* Created by [Piotr Kitłowski](https://audrey.feldroy.com/) | GitHub [@cncPomper](https://github.com/cncPomper) | PyPI [@cncPomper](https://pypi.org/user/cncPomper/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://cncPomper.github.io/Breast-Density-Mammography/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/Breast-Density-Mammography.git
cd Breast-Density-Mammography

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `breast_density_mammography`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

Breast-Density-Mammography was created in 2026 by Piotr Kitłowski.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
