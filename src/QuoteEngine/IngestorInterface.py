from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.Quote import Quote

import os


class IngestorInterface(ABC):
    """Interface for creating ingestors to consume different file type and generate quotes.

    Args:
        ABC (class): Helper
    """
    extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Checking a file and see it can be ingest by using the file's extension and see the ext exist in the extension collection.

        Args:
            path (str): Path of a file containing quotes.

        Returns:
            bool: True if can be ingest, otherwise false.
        """
        _, file_ext = os.path.splitext(path)

        return file_ext in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """Handling parsing data from a file and transform it into a list of Quote models.

        Args:
            path (str): The file path.

        Returns:
            List[Quote]: A list of Quote models.
        """
        pass
