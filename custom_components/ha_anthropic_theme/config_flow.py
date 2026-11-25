"""Config flow for ha_anthropic_theme."""

from __future__ import annotations

from typing import TYPE_CHECKING

import probatio
from homeassistant import config_entries

from .const import DOMAIN

if TYPE_CHECKING:
    from collections.abc import Mapping


class HaAnthropicThemeFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Anthropic Theme: one confirmation, nothing to configure."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: Mapping[str, str] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Confirm installing the themes."""
        if user_input is not None:
            return self.async_create_entry(title="Anthropic Theme", data={})
        return self.async_show_form(step_id="user", data_schema=probatio.Schema({}))
