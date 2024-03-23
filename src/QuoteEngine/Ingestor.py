from abc import abstractmethod
from typing import List
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DOCXIngestor import DOCXIngestor
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.Quote import Quote
from QuoteEngine.TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Primary ingestor for client's usage. 
    Can automatically choose the supported ingestor using the provided file's extension.

    Args:
        IngestorInterface (class): Ingestor ABC.
    """

    # Supported ingestors
    ingestors = [PDFIngestor, CSVIngestor, DOCXIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
