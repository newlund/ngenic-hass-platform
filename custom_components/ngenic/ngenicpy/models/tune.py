"""Tune model."""

from ..const import API_PATH  # noqa: TID252
from .base import NgenicBase
from .node import Node
from .room import Room


class Tune(NgenicBase):
    """Ngenic API Tune model."""

    def __init__(self, session, json_data) -> None:
        """Initialize the tune model."""
        super().__init__(session=session, json_data=json_data)

    def uuid(self):
        """Get the tune UUID."""

        # If a tune was fetched with the list API, it contains "tuneUuid"
        # If it was fetched directly (with UUID), it contains "uuid"
        try:
            return self["tuneUuid"]
        except AttributeError:
            return super().uuid()

    async def async_rooms(self):
        """List all Rooms associated with a Tune (async). A Room contains an indoor sensor.

        :return:
            a list of rooms
        :rtype:
            `list(~ngenic.models.room.Room)`
        """
        url = API_PATH["rooms"].format(tuneUuid=self.uuid(), roomUuid="")
        return await self._async_parse_new_instance(url, Room, tune=self)

    async def async_room(self, roomUuid):
        """Get data about a Room (async). A Room contains an indoor sensor.

        :param str roomUuid:
            (required) room UUID
        :return:
            the room
        :rtype:
            `~ngenic.models.room.Room`
        """
        url = API_PATH["rooms"].format(tuneUuid=self.uuid(), roomUuid=roomUuid)
        return await self._async_parse_new_instance(url, Room, tune=self)

    async def async_nodes(self):
        """List all Nodes associated with a Tune (async). A Node is a logical network entity.

        :return:
            a list of nodes
        :rtype:
            `list(~ngenic.models.node.Node)`
        """
        url = API_PATH["nodes"].format(tuneUuid=self.uuid(), nodeUuid="")
        return await self._async_parse_new_instance(url, Node, tune=self)

    async def async_node(self, nodeUuid):
        """Get data about a Node (async). A Node is a logical network entity.

        :param str nodeUuid:
            (required) node UUID
        :return:
            the node
        :rtype:
            `~ngenic.models.node.Node`
        """
        url = API_PATH["nodes"].format(tuneUuid=self.uuid(), nodeUuid=nodeUuid)
        return await self._async_parse_new_instance(url, Node, tune=self)
