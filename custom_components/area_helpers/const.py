DOMAIN = "area_helpers"

HELPERS = [
    {
        "name": "Target Temperature",
        "icon": "mdi:thermometer",
        "unit_of_measurement": "°C",
        "min_value": 15,
        "max_value": 30,
        "step": 0.5,
    },
    {
        "name": "Target Humidity",
        "icon": "mdi:water-percent",
        "unit_of_measurement": "%",
        "min_value": 30,
        "max_value": 80,
        "step": 1,
    },
    {
        "name": "Target PM 2.5",
        "icon": "mdi:blur",
        "unit_of_measurement": "µg/m³",
        "min_value": 0,
        "max_value": 100,
        "step": 1,
    },
    {
        "name": "Target PM 10",
        "icon": "mdi:blur",
        "unit_of_measurement": "µg/m³",
        "min_value": 0,
        "max_value": 100,
        "step": 1,
    },
    {
        "name": "Target Lux",
        "icon": "mdi:weather-sunny",
        "unit_of_measurement": "lx",
        "min_value": 0,
        "max_value": 1000,
        "step": 10,
    },
]
