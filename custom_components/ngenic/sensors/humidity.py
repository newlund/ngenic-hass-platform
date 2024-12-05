"""Ngenic Humidity Sensor."""

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass

from .base import NgenicSensor


class NgenicHumiditySensor(NgenicSensor):
    """Representation of an Ngenic Humidity Sensor."""

    device_class = SensorDeviceClass.HUMIDITY
    state_class = SensorStateClass.MEASUREMENT

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "%"
