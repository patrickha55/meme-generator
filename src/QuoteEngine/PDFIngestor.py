from typing import List
from IngestorInterface import IngestorInterface
from Quote import Quote
from IngestorException import IngestorException

import subprocess
import pandas


class PDFIngestor(IngestorInterface):
    """Ingestor for extracting text from a PDF file and transform into Quote models.add()

    Args:
        IngestorInterface (class): Ingestor ABC.

    Raises:
        IngestorException: Custom exception for handling un-ingestable file.
    """
    extensions = ['.pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        try:
            temp_text_file = 'tmp/pdf_text.txt'

            if not cls.can_ingest(path):
                raise IngestorException('Cannot ingest exception.')

            subprocess.run(
                ['pdftotext', path, temp_text_file], shell=True)

            quotes = []
            df = pandas.readcsv(temp_text_file, header=0)

            for index, row in df.iterrows():
                new_quote = Quote(row[0], row[1])
                quotes.append(new_quote)

            subprocess.run(['rm', temp_text_file], shell=True)

            return quotes
        except FileExistsError as err:
            print(err)
            raise
        except Exception as err:
            print(err)
            raise
