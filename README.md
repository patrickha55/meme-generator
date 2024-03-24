# MEME Generator App

## Description

Author: Phat Ha
Source: Udacity

Generate a meme by combining images with different quotes and authors.

## How To Use

### Install

#### Prerequisites:

- Python 3.
- Virtual Environment

#### Install virtualenv:

- Launch your shell app.
- Run `python -m pip install --user virtualenv`

#### Initialize The Project:

- Clone the repo.
- Launch your shell app.
- CD into src.
- Activate the environment (Windows):
  - `.\env\Scripts\Activate.ps1`
- Install all packages:
  - `pip install -r requirements.txt`

### Usage

Before using, make sure to follow the Install steps above.

For CLI execution:

- Launch your shell app.
- CD into src.
- Run: `python -m meme`
- There are 3 optional arguments:
  - '-path': Path to an image for generating a meme.
  - '-body': The quote to display.
  - '-author': The quote's author.

For Web App usage:

- Launch your shell app.
- CD into src.
- Run: `python -m app`
- Click on the endpoint to launch the website.

### For Developer

This repository contains two major components:

- The MemeGenerator.
- The QuoteEngine.

#### MemeGenerator

- GeneratorInterface: Abstract base class for creating a meme generator class.
- GeneratorException: Custom exception for Meme Generator.
- MemeEngine: Class for meme generation and image processing.

Instruction:

- Can generate a meme by using the **make_meme** method inside the MemeEngine.
- Can save an image to disk by calling the **reading_from_binary** method and providing an image's binary file.

#### QuoteEngine

- IngestorInterface: Interface for creating ingestors to consume different file type and generate quotes.
- GeneratorException: Custom exception for ingestion job.
- Quote: Quote model for saving a body and author.
- Ingestor: Primary ingestor for client's usage using the [strategy design pattern](https://refactoring.guru/design-patterns/strategy).
  Can automatically choose the supported ingestor using the provided file's extension.
- CSVIngestor: Ingestor for extracting text from a CSV file and transform into Quote models.
- DOCXIngestor: Ingestor for extracting text from a DOCX file and transform into Quote models.
- PDFIngestor: Ingestor for extracting text from a PDF file and transform into Quote models.
- TextIngestor: Ingest a text file and generate quotes.

Instruction:

- Import the Ingestor module.
- Using the **parse** method and pass in a file. This method will check and see if it can parse the file.
  - Will raises an error when receives an unsupported file type.
  - Return a tuple containing a list of **Quotes**.
