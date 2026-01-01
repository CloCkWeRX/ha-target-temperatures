"""Tests for the Target Temperatures integration."""
from unittest.mock import MagicMock, patch

from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.ha_target_temperatures.const import DOMAIN


async def test_async_setup_entry(hass: HomeAssistant):
    """Test that the component sets up correctly."""
    assert await async_setup_component(hass, "number", {})
    await hass.async_block_till_done()

    entry = MockConfigEntry(domain=DOMAIN, data={})
    entry.add_to_hass(hass)

    with patch(
        "homeassistant.helpers.area_registry.async_get"
    ) as mock_async_get_area_registry:
        mock_area_registry = MagicMock()
        mock_area_registry.async_list_areas.return_value = []
        mock_async_get_area_registry.return_value = mock_area_registry

        assert await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()

    assert entry.state is ConfigEntryState.LOADED
