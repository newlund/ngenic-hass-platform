"""Ngenic API measurement model."""

from enum import Enum

from .base import NgenicBase


class MeasurementType(Enum):
    """Measurement type enumeration.

    Undocumented in API.
    """

    UNKNOWN = "unknown"
    TEMPERATURE = "temperature_C"
    TARGET_TEMPERATURE = "target_temperature_C"
    HUMIDITY = "humidity_relative_percent"
    CONTROL_VALUE = "control_value_C"
    POWER_KW = "power_kW"
    ENERGY_KWH = "energy_kWH"
    FLOW = "flow_litre_per_hour"
    INLET_FLOW_TEMPERATURE = "inlet_flow_temperature_C"
    RETURN_TEMPERATURE = "return_temperature_C"

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


class Measurement(NgenicBase):
    """Ngenic API measurement model."""

    def __init__(self, session, json_data, node, measurement_type) -> None:
        """Initialize the measurement model."""
        self._parentNode = node
        self._measurementType = measurement_type

        super().__init__(session=session, json_data=json_data)

    def get_type(self):
        """Get the measurement type.

        :return:
            measurement type
        :rtype:
            `~ngenic.models.measurement.MeasurementType`
        """
        return self._measurementType
