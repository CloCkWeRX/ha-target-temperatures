from homeassistant.helpers.entity import DeviceInfo
from homeassistant.components.input_number import InputNumberEntity
from homeassistant.helpers.area_registry import async_get as async_get_area_registry

from .const import DOMAIN, HELPERS

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Area Helpers from a config entry."""
    area_registry = async_get_area_registry(hass)
    areas = area_registry.async_list_areas()

    entities = [
        AreaHelper(area, helper)
        for area in areas
        for helper in HELPERS
    ]

    async_add_entities(entities)

class AreaHelper(InputNumberEntity):
    """Representation of an Area Helper."""

    def __init__(self, area, helper):
        """Initialize the Area Helper."""
        self._area = area
        self._helper = helper
        self._attr_unique_id = f"{area.id}_{helper['name'].lower().replace(' ', '_')}"
        self._attr_name = f"{area.name} {helper['name']}"
        self._attr_icon = helper["icon"]
        self._attr_unit_of_measurement = helper["unit_of_measurement"]
        self._attr_min_value = helper["min_value"]
        self._attr_max_value = helper["max_value"]
        self._attr_step = helper["step"]
        self._attr_value = helper["min_value"]
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, area.id)},
            name=f"{area.name} Helpers",
            manufacturer="Area Helpers",
        )

    async def async_set_value(self, value):
        """Set new value."""
        self._attr_value = value
        self.async_write_ha_state()
