import random
import os
import requests
from typing import List
from flask import Flask, render_template, abort, request

from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine.Quote import Quote
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup() -> tuple[List[Quote] | None, List[str] | None]:
    """Load all resources for random meme generation.

    Returns:
        tuple[List[Quote] | None, List[str] | None]: List of quotes and images urls.
    """

    try:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']

        # quote_files variable
        quotes: List[Quote] = []

        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        images_path = "./_data/photos/dog/"

        # images within the images images_path directory
        imgs: List[str] = []

        for image_path in os.listdir(images_path):
            imgs.append(f'{images_path}{image_path}')

        return quotes, imgs
    except Exception as err:
        print(err)

    return None, None


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme. """

    img = imgs[random.randint(0, len(imgs) - 1)]
    quote = quotes[random.randint(0, len(quotes) - 1)]

    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    response = requests.get(img_url)

    img_path = MemeEngine.reading_from_binary(response.content)

    path = meme.make_meme(img_path, body, author)

    os.remove(img_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
