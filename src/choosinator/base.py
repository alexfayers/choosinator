"""The main functionality of `choosinator`."""

import logging

from .helpers import Config


class BaseClass:
    """Everything in the project comes back to here."""

    def __init__(self, config_file: str):
        """Initialises the base class for `choosinator` by loading the config and setting up a logger.

        Args:
            config_file (str): Path to a config file containing settings for the class.
        """
        self.logger = logging.getLogger(__name__).getChild(self.__class__.__qualname__)

        self.config = Config(config_file)

        package_logger = logging.getLogger("choosinator")
        if self.config.DEBUG.ENABLED:
            package_logger.setLevel(logging.DEBUG)
        else:
            package_logger.setLevel(logging.INFO)
