"""Room model for Ngenic Tune API."""

from typing import Any

import httpx

from ..const import API_PATH  # noqa: TID252
from .base import NgenicBase


class Room(NgenicBase):
    """Ngenic API room model."""

    def __init__(
        self, session: httpx.AsyncClient, json_data: dict[str, Any], tuneUuid: str
    ) -> None:
        """Initialize the room model."""
        self._parentTuneUuid = tuneUuid

        super().__init__(session=session, json_data=json_data)

    async def async_update(self) -> None:
        """Update this room with its current values (async)."""

        url = API_PATH["rooms"].format(
            tuneUuid=self._parentTuneUuid, roomUuid=self.uuid()
        )
        await self._async_put(url, data=self.json())
