from typing import List
from QuoteEngine.IngestorException import IngestorException
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.Quote import Quote

import pandas


class CSVIngestor(IngestorInterface):
    """Ingestor for extracting text from a CSV file and transform into Quote models.add()

    Args:
        IngestorInterface (class): Ingestor ABC.

    Raises:
        IngestorException: Custom exception for handling un-ingestable file.
    """
    extensions = ['.csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        try:
            if not cls.can_ingest(path):
                raise IngestorException('Cannot ingest exception.')

            quotes: List[Quote] = []
            df = pandas.read_csv(path)

            for index, row in df.iterrows():
                new_quote = Quote(row[0], row[1])
                quotes.append(new_quote)

            return quotes
        except FileExistsError as err:
            print(err)
            raise
        except Exception as err:
            print(err)
            raise
