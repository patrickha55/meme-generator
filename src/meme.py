import os
import random
import argparse

from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.Quote import Quote


def generate_meme(path: str = None, body: str = None, author: str = None) -> str | None:
    """Generate a meme given an path and a quote.

    Args:
        path (str, optional): Image's path. Defaults to None.
        body (str, optional): Quote body to display. Defaults to None.
        author (str, optional): Author of a quote. Defaults to None.

    Raises:
        Exception: General Error.

    Returns:
        str | None: The generated meme's (image) path. None if encounters an error.
    """
    try:
        img: str = ''
        quote: Quote = None

        if path is None:
            images = "./_data/photos/dog/"
            imgs = []
            for root, dirs, files in os.walk(images):
                imgs = [os.path.join(root, name) for name in files]

            img = random.choice(imgs)
        else:
            img = path

        if body is None:
            quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                           './_data/DogQuotes/DogQuotesDOCX.docx',
                           './_data/DogQuotes/DogQuotesPDF.pdf',
                           './_data/DogQuotes/DogQuotesCSV.csv']
            quotes = []
            for f in quote_files:
                quotes.extend(Ingestor.parse(f))

            quote = random.choice(quotes)
        else:
            if author is None:
                raise Exception('Author Required if Body is Used')
            quote = Quote(body, author)

        meme = MemeEngine('./static')
        path = meme.make_meme(img, quote.body, quote.author)
        return path
    except Exception as err:
        print(err)

    return None


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()

        parser.add_argument('-p', '--path', type=str,
                            help='The image path use for generating a meme.')
        parser.add_argument('-b', '--body', type=str,
                            help='The quote to display inside a meme.')

        parser.add_argument('-a', '--author', type=str,
                            help='The author to display under a quote.')

        args = parser.parse_args()

        print(generate_meme(args.path, args.body, args.author))
    except Exception as err:
        print(err)
