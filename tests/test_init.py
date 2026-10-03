import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.ha_target_temperatures.const import DOMAIN
from homeassistant.helpers.area_registry import async_get as async_get_area_registry

@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    yield

async def test_setup_and_unload_entry(hass):
    """Test setting up and unloading config entry."""
    area_registry = async_get_area_registry(hass)
    area_registry.async_get_or_create("living_room")

    config_entry = MockConfigEntry(domain=DOMAIN, title="Target Temperatures", data={})
    config_entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    # Check that number entity state was created
    state = hass.states.get("number.living_room_target_temperature")
    assert state is not None
    assert state.state == "15"

    # Test setting native value via service call
    await hass.services.async_call(
        "number",
        "set_value",
        {"entity_id": "number.living_room_target_temperature", "value": 21.5},
        blocking=True,
    )
    state = hass.states.get("number.living_room_target_temperature")
    assert state.state == "21.5"

    assert await hass.config_entries.async_unload(config_entry.entry_id)
    await hass.async_block_till_done()
