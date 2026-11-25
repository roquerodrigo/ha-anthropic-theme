"""Constants for ha_anthropic_theme."""

from __future__ import annotations

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "ha_anthropic_theme"
PREVIOUS_DOMAIN = "ha_themes"

THEMES_DIRECTORY = "themes"
STATIC_URL_PATH = f"/{DOMAIN}"
FRONTEND_MODULE_FILENAME = "ha-anthropic-theme.js"

ISSUE_THEMES_NOT_LOADED = "themes_not_loaded"
ISSUE_THEMES_RELOAD_FAILED = "themes_reload_failed"
