"""Custom types for ha_anthropic_theme."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .diagnostics_payload import HaAnthropicThemeDiagnosticsPayload
from .runtime import HaAnthropicThemeData

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry


type HaAnthropicThemeConfigEntry = ConfigEntry[HaAnthropicThemeData]

__all__ = [
    "HaAnthropicThemeConfigEntry",
    "HaAnthropicThemeData",
    "HaAnthropicThemeDiagnosticsPayload",
]
