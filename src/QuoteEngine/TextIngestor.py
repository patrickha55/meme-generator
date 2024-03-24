from typing import List
from QuoteEngine.IngestorException import IngestorException
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.Quote import Quote


class TextIngestor(IngestorInterface):
    """Ingest a text file and generate quotes.

    Args:
        IngestorInterface (_type_): Interface for creating ingestors to consume different file type and generate quotes
    """

    extensions = ['.txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        try:
            if not cls.can_ingest(path):
                raise IngestorException('Cannot ingest exception.')
            quotes = []

            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    temp = [l.strip() for l in line.rstrip().split('-')]
                    new_quote = Quote(temp[0], temp[1])
                    quotes.append(new_quote)

            return quotes
        except FileExistsError as err:
            print(err)
            raise
        except Exception as err:
            print(err)
            raise
