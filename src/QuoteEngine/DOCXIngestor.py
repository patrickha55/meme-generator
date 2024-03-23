from typing import List
from IngestorInterface import IngestorInterface
from Quote import Quote
from IngestorException import IngestorException
from docx import Document


class DOCXIngestor(IngestorInterface):
    """Ingestor for extracting text from a DOCX file and transform into Quote models.add()

    Args:
        IngestorInterface (class): Ingestor ABC.

    Raises:
        IngestorException: Custom exception for handling un-ingestable file.
    """
    extensions = ['.docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        try:
            if not cls.can_ingest(path):
                raise IngestorException('Cannot ingest exception.')

            quotes: List[Quote] = []
            content = Document(path).paragraphs

            for c in content:
                if c.text != '':
                    temp: List[str] = [c.strip().strip('"')
                                       for c in c.text.split('-')]
                    new_quote = Quote(temp[0], temp[1])
                    quotes.append(new_quote)

            return quotes
        except FileExistsError as err:
            print(err)
            raise
        except Exception as err:
            print(err)
            raise
