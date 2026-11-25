# Contributing

Bug reports, ideas and pull requests are welcome.

## Reporting a bug

Open an [issue](https://github.com/roquerodrigo/ha-anthropic-theme/issues/new/choose) with:

- the Home Assistant version, the integration version, the browser and whether the problem shows in light mode, dark mode or both;
- what you did, what you expected and what happened, with a screenshot when the problem is visual;
- the diagnostics downloaded from the integration's menu and the relevant log lines.

## Project layout

| Path | What it is |
| --- | --- |
| [`custom_components/ha_anthropic_theme/`](custom_components/ha_anthropic_theme) | The integration. `themes/` and `frontend/` inside it are generated. |
| [`themes-src/`](themes-src) | Theme definitions. |
| [`toolkit/`](toolkit) | Token capture, reference docs, palette tools and the theme builder. Not shipped. |
| [`catalog/tokens.json`](catalog/tokens.json) | The token catalog the builder validates against (generated). |
| [`docs/`](docs) | The theming guide, the theme definition reference and the generated token references. |
| [`dev/`](dev) | Configuration of the development instance, with demo entities and the Theme Lab dashboard. |
| [`previews/`](previews) | Palette sheets and screenshots of every theme in both modes (generated). |

Generated files are never edited by hand. Change the source, rebuild and commit the output with it.

## Development setup

You need Python 3.14, [uv](https://docs.astral.sh/uv/) and Google Chrome (the token capture and the previews drive it through Playwright).

```bash
scripts/setup              # install the dependencies into .venv
scripts/dev-server         # run Home Assistant at http://localhost:8123 with this integration loaded
scripts/ha-anthropic-theme onboard  # first run only: create the test user and add the integration
```

`scripts/dev-server` runs Home Assistant with [`dev/config/`](dev/config) and copies `custom_components/ha_anthropic_theme` into it on every start. After a build, restart Home Assistant (from the UI or by restarting `scripts/dev-server`) to see the change. Reloading the integration is not enough: it reinstalls the copy made at the last start.

## Toolkit commands

| Command | What it does |
| --- | --- |
| `scripts/ha-anthropic-theme build [slug…] [--strict] [--verbose]` | Build `themes-src/` into the integration and validate every theme |
| `scripts/ha-anthropic-theme preview [slug…] [--palette-only]` | Render the palette sheets and screenshot the themes in Google Chrome |
| `scripts/ha-anthropic-theme palette [slug…]` | Rank the chart series orders that pass the checks, and list the entity colors |
| `scripts/ha-anthropic-theme catalog` | Capture the token catalog from the development instance and regenerate the reference docs |
| `scripts/ha-anthropic-theme docs` | Regenerate the reference docs from `catalog/tokens.json` |

To create or change a theme, follow [docs/creating-a-theme.md](docs/creating-a-theme.md). [docs/theming-guide.md](docs/theming-guide.md) explains how the current frontend applies themes and which parts the support module covers.

After changing a theme, its roles or palettes, the builder or the support module, run `scripts/ha-anthropic-theme build --strict`, commit the regenerated files and check the result in Google Chrome in light and dark mode. Regenerate `previews/` with `scripts/ha-anthropic-theme preview` when the change is visual.

## Checks

Run these before opening a pull request. CI runs the same ones, and `pre-commit install` runs the first three on every commit.

```bash
uv run ruff format .       # format
uv run ruff check . --fix  # lint
uv run mypy                # type-check the integration
uv run pytest              # tests, coverage of the integration must stay at 90 % or more
```

`scripts/lint` runs the same four in check mode, as CI does. The toolkit has lighter lint rules in `toolkit/ruff.toml`, and its tests do not count toward the coverage gate. To run them alone, use `uv run pytest toolkit/tests --no-cov`. `toolkit/tests/test_generated_files.py` fails when the committed themes or support module are out of date with their sources.

Read [CODE_STYLE.md](CODE_STYLE.md) before adding or restructuring code.

## Updating to a new Home Assistant release

1. Bump `homeassistant`, `home-assistant-frontend` and `pytest-homeassistant` (released with the same version as Home Assistant) in `pyproject.toml`, and `homeassistant` in `hacs.json`, then run `uv sync`. Dependabot ignores these three packages. pytest and pytest-asyncio are not pinned here because `pytest-homeassistant` pins them. `toolkit/tests/test_pinned_versions.py` fails until the catalog is captured again.
2. Restart `scripts/dev-server` and run `scripts/ha-anthropic-theme catalog`.
3. Review the diff of `catalog/tokens.json` and of the generated docs: new, removed and changed tokens, and the list of broken references.
4. Run `scripts/ha-anthropic-theme build --strict`. Unknown tokens point at themes that need updating.
5. Review what is kept by hand against the new frontend: `UPSTREAM_FIXES` in `toolkit/ha_theme_kit/theme/roles.py` (drop fixes the frontend no longer needs), `FRONTEND_SERIES` in `chart_palette.py`, `FRONTEND_NAMED_HUES` in `entity_palette.py`, `FRONTEND_LAYERING` in `neutral_layers.py`, `ICON_TILE_ENTITY_COLORS` and the stock radii, selectors and fill tokens of the form field stylesheets in `toolkit/ha_theme_kit/support/ha-anthropic-theme.js`, and the version header and known issues table of `docs/theming-guide.md`. Run `scripts/lint`: tests fail while these disagree with the new catalog.
6. Regenerate the previews and compare them with the previous ones.

## How the catalog is captured

- Runtime: Playwright drives the installed Google Chrome with an isolated profile. In light and dark mode it reads every custom property declared on `html` in the document and in adopted stylesheets, the inline values the theme engine sets, and their computed values.
- Bundle scan: every chunk of the installed frontend package is scanned for `var(--token, fallback)` references, script reads and names built at runtime. This yields how widely each token is used and the component hooks that are never declared globally.

## Brand assets

`custom_components/ha_anthropic_theme/brand/` holds the images Home Assistant shows for the integration, on a transparent background. `icon.svg` is the Anthropic symbol from [Simple Icons](https://simpleicons.org/?q=anthropic) (CC0), and `logo.svg` is the Anthropic wordmark from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Anthropic_logo.svg) (public domain), both drawn in the brand's dark color (`#141413`). `icon.png` and `logo.png` are renders of them for light backgrounds; `dark_icon.png` and `dark_logo.png` are renders with the fill swapped to the brand's light color (`#faf9f5`) for dark backgrounds. The icons are square, and the logos are trimmed to the wordmark at 128 px high. Each image has an `@2x` variant at twice the size. Render the PNGs in Google Chrome at the sizes `tests/test_brand.py` checks. The symbol and the wordmark are trademarks of Anthropic PBC; this project is not affiliated with or endorsed by Anthropic.

## Pull requests

1. Fork the repository and branch from `main`.
2. Write the pull request title and commit messages as [Conventional Commits](https://www.conventionalcommits.org/). Releases and their notes are generated from them. Mark breaking changes with `!` or a `BREAKING CHANGE:` footer.
3. Leave the version in `manifest.json`, `pyproject.toml` and `uv.lock` alone. The release pull request bumps it.
4. Update `translations/en.json` and `translations/pt-BR.json` together when you change user-facing strings.
5. Update the README when what users see or do changes.
6. Fill in the pull request template.

## License

Contributions are released under the project's [MIT License](LICENSE).
