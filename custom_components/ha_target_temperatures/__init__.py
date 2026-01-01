from .const import DOMAIN


async def async_setup_entry(hass, entry):
    """Set up Area Helpers from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, ["number"])
    return True


async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unloads(
        entry, ["number"]
    )
