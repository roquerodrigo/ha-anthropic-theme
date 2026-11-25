# Anthropic Theme

<!-- ha-marketplace:exclude-start -->
[![CI](https://github.com/roquerodrigo/ha-anthropic-theme/actions/workflows/ci.yml/badge.svg)](https://github.com/roquerodrigo/ha-anthropic-theme/actions/workflows/ci.yml)
[![GitHub release](https://img.shields.io/github/v/release/roquerodrigo/ha-anthropic-theme)](https://github.com/roquerodrigo/ha-anthropic-theme/releases/latest)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-db61a2?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/roquerodrigo)

[![Open your Home Assistant instance and open a repository in the Marketplace.](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=roquerodrigo&repository=ha-anthropic-theme&category=integration)
<!-- ha-marketplace:exclude-end -->

Give Home Assistant the Anthropic theme: warm paper tones, a clay accent and the font of your operating system, in light and dark mode. The theme is made for the current Home Assistant interface, so it also restyles what a regular theme cannot reach, such as the font of every screen, the form fields, the menus and the generic integration icons. It installs itself and updates with the integration.

| Light | Dark |
| --- | --- |
| ![Anthropic theme on a dashboard, light mode](previews/anthropic/dashboard-light.png) | ![Anthropic theme on a dashboard, dark mode](previews/anthropic/dashboard-dark.png) |
| ![Anthropic theme on the Settings page, light mode](previews/anthropic/settings-light.png) | ![Anthropic theme on the Settings page, dark mode](previews/anthropic/settings-dark.png) |

## Features

- A light and a dark mode that follow the dark mode choice in your profile.
- A calm, flat look: the sidebar and header share the page color, there are no shadows, and the dashboard header, cards and dialogs are slightly translucent with a blur behind them.
- Form fields drawn as outlined boxes, and the same small rounded corner on cards, dialogs, buttons, badges and fields.
- Entity colors restyled to sit well with the theme in both modes, while each state keeps its usual color. Chart colors stay easy to tell apart, also for people with red and green color blindness.
- The theme font on every screen, including the sidebar, the charts, the map and the code editor.
- The flat blue icons of integrations without a logo, and the colored icon tiles on the Settings, System and About pages, take the theme's colors.
- Other themes look exactly as before: the extra styling only runs while the Anthropic theme is in use.

## Requirements

- Home Assistant 2026.11.0 or newer.
- `configuration.yaml` loads themes from the `themes` folder. New installations already have this. If yours does not, add:

  ```yaml
  frontend:
    themes: !include_dir_merge_named themes
  ```

<!-- ha-marketplace:exclude-start -->
## Installation

### Home Assistant Marketplace (recommended)

1. Select the **Open your Home Assistant instance** button above, or go to **Settings → Marketplace**, select **Add from link** in the upper-right corner, enter `roquerodrigo/ha-anthropic-theme` and select **Add**.
2. Select **Install**.
3. Restart Home Assistant.

### Manual

1. Download `ha_anthropic_theme.zip` from the [latest release](https://github.com/roquerodrigo/ha-anthropic-theme/releases/latest).
2. Extract it into `config/custom_components/ha_anthropic_theme/`.
3. Restart Home Assistant.
<!-- ha-marketplace:exclude-end -->

### Upgrading from HA Themes

This integration used to be published as **HA Themes** (`roquerodrigo/ha-themes`, domain `ha_themes`). The domain changed, so it does not update in place:

1. Delete the **HA Themes** entry under **Settings → Devices & services**. This removes its theme files.
2. Uninstall HA Themes.
3. Install Anthropic Theme from `roquerodrigo/ha-anthropic-theme`, restart Home Assistant and add the integration as described under Configuration.

The theme keeps its name, **Anthropic**, so profiles, views and cards that use it keep it. If you set it as the default theme with the `frontend.set_theme` action, run that action again. Custom themes that set `ha-themes-*` variables must rename them to `ha-anthropic-theme-*`. If theme files from HA Themes are left in `themes/ha_themes/`, Anthropic Theme deletes that folder when it starts, so the old copy of the theme cannot replace the new one.

## Configuration

Go to **Settings → Devices & services → Add integration**, search for **Anthropic Theme** and confirm. There is nothing to fill in, and you can add the integration only once.

Then pick the theme: open your profile (your name at the bottom of the sidebar) and choose **Anthropic** under **Theme**. You can also set it on a single dashboard view or card with its `theme` option, or for everyone with the `frontend.set_theme` action.

## How it works

The integration copies the theme into the `themes/ha_anthropic_theme/` folder of your configuration each time Home Assistant starts, and reloads the themes when the files changed. After an update, the new version of the theme appears with the next restart.

It also loads a small script on every page of the interface. That script applies the theme font everywhere and restyles the fields, menus and icons listed under Features. It does nothing while you use another theme, and becomes active as soon as the Anthropic theme is applied to the whole interface, a view or a card.

The Anthropic theme uses the font already on your device, so the interface makes no request to a font service. Everything stays inside Home Assistant.

## Troubleshooting

**A repair says "Anthropic Theme cannot load its themes".** Your `configuration.yaml` does not load themes from the `themes` folder. Add the lines shown under Requirements, then reload the themes in **Developer tools → YAML → Themes** or restart Home Assistant. The repair goes away on its own.

**A repair says "Anthropic Theme could not reload the themes".** Home Assistant refused to reload the themes, usually because of an error in `configuration.yaml` or in another theme file. The repair shows the error. Fix it and reload the themes in **Developer tools → YAML → Themes**.

**A theme file I put in `themes/ha_anthropic_theme/` disappeared.** That folder belongs to the integration, which removes any other `.yaml` file from it. Keep your own themes in another folder under `themes/`, and do not name one of them **Anthropic**: Home Assistant keeps only one theme per name.

**Setup fails with "Failed to install the themes".** Home Assistant could not write to the `themes` folder. The message names the folder and the error. Check that the disk has space and that the folder is writable.

**The theme is still listed after I uninstalled Anthropic Theme.** The integration was uninstalled before its entry was deleted, so it could not clean up. Delete the leftover **Anthropic Theme** entry under **Settings → Devices & services**, delete the `themes/ha_anthropic_theme/` folder, and reload the themes in **Developer tools → YAML → Themes**.

**Something else is wrong.** Download the diagnostics from the integration's menu and attach them to an [issue](https://github.com/roquerodrigo/ha-anthropic-theme/issues). They list the installed themes, which of them Home Assistant loaded, and the themes folder.

## Known limitations

- The theme files are removed only when you delete the integration entry, so delete it under **Settings → Devices & services** before you uninstall Anthropic Theme.
- While the integration is disabled, the theme stays selectable but loses the extra styling: the default font returns in the sidebar and charts, and fields, menus and icons go back to their usual look.
- When the theme is set on a single view or card instead of in your profile, the sidebar and the header keep the default font.

## Support

This integration is built and maintained on personal time. If it is useful to you, consider [sponsoring the work](https://github.com/sponsors/roquerodrigo). It keeps the fixes, the testing and the releases coming.

Report bugs and request features in the [issue tracker](https://github.com/roquerodrigo/ha-anthropic-theme/issues).

## Trademarks

This is an independent community project, not affiliated with or endorsed by Anthropic. Anthropic, the Anthropic symbol and the Anthropic wordmark are trademarks of Anthropic PBC.

<!-- ha-marketplace:exclude-start -->
## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development setup and workflow, and [CODE_STYLE.md](CODE_STYLE.md) for the code conventions. To build a theme of your own, start with [docs/creating-a-theme.md](docs/creating-a-theme.md). [docs/theming-guide.md](docs/theming-guide.md) explains how themes work in the current frontend.

## License

[MIT](LICENSE)
<!-- ha-marketplace:exclude-end -->
