import os
from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.Quote import Quote
from QuoteEngine.IngestorException import IngestorException

import subprocess


class PDFIngestor(IngestorInterface):
    """Ingestor for extracting text from a PDF file and transform into Quote models.

    Args:
        IngestorInterface (class): Ingestor ABC.

    Raises:
        IngestorException: Custom exception for handling un-ingestable file.
    """
    extensions = ['.pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        try:
            temp_text_file = './QuoteEngine/tmp/pdf_text.txt'

            if not cls.can_ingest(path):
                raise IngestorException('Cannot ingest exception.')

            subprocess.run(
                ['pdftotext', '-layout',  path, temp_text_file], shell=True)

            quotes = []
            with open(temp_text_file, 'r') as f:
                lines = f.readlines()

                for line in lines:
                    if line != '' and line != '\x0c':
                        split_line = [l.strip().strip('"')
                                      for l in line.split('-')]
                        new_quote = Quote(split_line[0], split_line[1])
                        quotes.append(new_quote)

            os.remove(temp_text_file)

            return quotes
        except FileExistsError as err:
            print(err)
            raise
        except Exception as err:
            print(err)
            raise
