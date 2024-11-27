"""Ngenic Node Status model."""

import logging

from .base import NgenicBase

_LOGGER = logging.getLogger(__name__)


class NodeStatus(NgenicBase):
    """Ngenic API node status model."""

    def __init__(self, session, json_data, node) -> None:
        """Initialize the node status model."""
        self._parentNode = node

        super().__init__(session=session, json_data=json_data)

    def battery_percentage(self):
        """Get the battery percentage."""
        if self["maxBattery"] == 0:
            # not using batteries
            _LOGGER.debug("Node %s is not using batteries", self._parentNode.uuid())
            return 100

        return int((self["battery"] / self["maxBattery"]) * 100)

    def radio_signal_percentage(self):
        """Get the radio signal percentage."""
        if self["maxRadioStatus"] == 0:
            # shouldn't happen as of now (always maxRadioStatus is always 4)
            return 100

        return int((self["radioStatus"] / self["maxRadioStatus"]) * 100)
