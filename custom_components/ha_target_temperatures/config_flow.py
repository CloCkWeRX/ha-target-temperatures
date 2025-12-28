from homeassistant import config_entries
from .const import DOMAIN

class TargetTemperaturesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Target Temperatures config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle a flow initiated by the user."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="Target Temperatures", data={})

        return self.async_show_form(step_id="user")
