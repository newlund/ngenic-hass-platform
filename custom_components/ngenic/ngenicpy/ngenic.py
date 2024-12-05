"""Module containing the main interfaces to the API."""

import logging
import ssl

import httpx

from .const import API_PATH
from .models import NgenicBase, Tune

LOG = logging.getLogger(__package__)

# 30sec for connect, 10sec elsewhere.
timeout = httpx.Timeout(10.0, connect=20.0)


def _create_local_ssl_context() -> ssl.SSLContext:
    """Create SSL context."""

    return ssl.create_default_context()


# The default SSLContext objects are created at import time
SSL_CONTEXT_LOCAL_API = _create_local_ssl_context()


class BaseClient(NgenicBase):
    """Base class for the Ngenic API client."""

    async def async_tunes(self) -> list[Tune]:
        """Fetch all tunes (async).

        :return:
            a list of tunes
        :rtype:
            `list(~ngenic.models.tune.Tune)`
        """
        url = API_PATH["tunes"].format(tuneUuid="")
        return await self._async_parse_new_instance(url, Tune)

    def async_tune(self, tuneUuid: str) -> Tune:
        """Fetch a single tune.

        :param str tuneUUid:
            (required) tune UUID
        :return:
            the tune
        :rtype:
            `~ngenic.models.tune.Tune`
        """
        url = API_PATH["tunes"].format(tuneUuid=tuneUuid)
        return self._async_parse_new_instance(url, Tune)


class AsyncNgenic(BaseClient):
    """Ngenic API client."""

    def __init__(self, token) -> None:
        """Initialize an async ngenic object.

        :param token:
            (required) OAuth2 bearer token
        """

        # this will be added to the HTTP Authorization header for each request
        self._token = token

        # this header will be added to each HTTP request
        self._auth_headers = {"Authorization": f"Bearer {self._token}"}

        session = httpx.AsyncClient(
            headers=self._auth_headers,
            timeout=timeout,
            verify=SSL_CONTEXT_LOCAL_API,
        )

        # initializing this doesn't require a session or json
        super().__init__(session=session)

    async def __aenter__(self):
        """Enter the context manager."""
        return self

    async def __aexit__(self, *args):
        """Exit the context manager."""
        await self.async_close()

    async def async_close(self):
        """Close the session if it was not created as a context manager."""
        await self._session.aclose()
