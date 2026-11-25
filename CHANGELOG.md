# Changelog

## [2.0.0](https://github.com/roquerodrigo/ha-anthropic-theme/compare/v1.1.1...v2.0.0) (2026-11-25)

The integration is renamed to Anthropic Theme with a new domain, which requires reinstalling it and renaming any custom theme variables.

### Breaking changes

- The integration is renamed from HA Themes to Anthropic Theme and its domain changes from ha_themes to ha_anthropic_theme, so it does not update in place: delete the HA Themes entry, uninstall it, install Anthropic Theme from roquerodrigo/ha-anthropic-theme, add it again and restart. If the theme was set as default with frontend.set_theme, run that action again. ([#40](https://github.com/roquerodrigo/ha-anthropic-theme/pull/40))
- Custom themes that set ha-themes-* variables must rename them to ha-anthropic-theme-*. ([#40](https://github.com/roquerodrigo/ha-anthropic-theme/pull/40))

### Improvements

- Theme files left in themes/ha_themes/ by the previous version are now deleted on start, so they cannot replace the new copy of the Anthropic theme. ([#40](https://github.com/roquerodrigo/ha-anthropic-theme/pull/40))
- The integration icon now shows the Anthropic symbol and its logo the Anthropic wordmark, with variants for dark backgrounds. ([#40](https://github.com/roquerodrigo/ha-anthropic-theme/pull/40))
- The README is rewritten for people installing the theme, with screenshots, requirements, setup, troubleshooting, known limitations and upgrade steps from HA Themes. ([#36](https://github.com/roquerodrigo/ha-anthropic-theme/pull/36), [#40](https://github.com/roquerodrigo/ha-anthropic-theme/pull/40))

## [1.1.1](https://github.com/roquerodrigo/ha-anthropic-theme/compare/v1.1.0...v1.1.1) (2026-11-08)

### Improvements

- Dropdown menus, selects and picker popovers no longer dim the page behind them; the page keeps its normal brightness while they are open. ([#29](https://github.com/roquerodrigo/ha-anthropic-theme/pull/29))

## [1.1.0](https://github.com/roquerodrigo/ha-anthropic-theme/compare/v1.0.0...v1.1.0) (2026-11-08)

Open menus dim the page slightly, icon tiles take the theme's rounded corners, and chart and code editor text now uses the theme font.

### New features

- Dropdown menus, selects and picker popups now dim the page slightly behind them, so the open popup stands out. Tooltips are unchanged. ([#22](https://github.com/roquerodrigo/ha-anthropic-theme/pull/22))

### Improvements

- Icon tiles in Settings, System, About and the search dialog now use the theme's rounded corners, matching entity icons, and search results follow the theme's colors. ([#24](https://github.com/roquerodrigo/ha-anthropic-theme/pull/24))

### Bug fixes

- Chart labels, legends and tooltips, and code editor completion details and search fields, now use the theme's font instead of Roboto. ([#25](https://github.com/roquerodrigo/ha-anthropic-theme/pull/25))

## 1.0.0 (2026-11-07)

### New features

- Adds the HA Themes integration with the Anthropic theme in light and dark modes, installed and reloaded automatically; requires Home Assistant 2026.11.0 or later.
