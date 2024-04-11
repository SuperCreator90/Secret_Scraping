"""Exceptions raised by SecretScraper."""


class SecretScraperException(Exception):
    """Global exception raised by SecretScraper"""

    pass


class AsyncPoolException(SecretScraperException):
    """Exception raised by coroutine module"""

    pass


class HandlerException(SecretScraperException):
    """Exception raised by handlers module"""
    pass
