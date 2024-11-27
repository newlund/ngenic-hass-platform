"""Room model for Ngenic Tune API."""

from ..const import API_PATH  # noqa: TID252
from .base import NgenicBase


class Room(NgenicBase):
    """Ngenic API room model."""

    def __init__(self, session, json_data, tune) -> None:
        """Initialize the room model."""
        self._parentTune = tune

        super().__init__(session=session, json_data=json_data)

    def update(self):
        """Update this room with its current values."""
        roomUuid = self["uuid"]

        url = API_PATH["rooms"].format(
            tuneUuid=self._parentTune.uuid(), roomUuid=roomUuid
        )
        self._put(url, data=self.json())

    async def async_update(self):
        """Update this room with its current values (async)."""
        roomUuid = self["uuid"]

        url = API_PATH["rooms"].format(
            tuneUuid=self._parentTune.uuid(), roomUuid=roomUuid
        )
        await self._async_put(url, data=self.json())
