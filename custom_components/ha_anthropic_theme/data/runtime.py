"""Runtime data stored on entry.runtime_data."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..frontend_module import HaAnthropicThemeFrontendModule
    from ..theme_installer import HaAnthropicThemeInstaller


@dataclass
class HaAnthropicThemeData:
    """Data stored on entry.runtime_data for Anthropic Theme."""

    theme_installer: HaAnthropicThemeInstaller
    frontend_module: HaAnthropicThemeFrontendModule
    installed_themes: tuple[str, ...]
