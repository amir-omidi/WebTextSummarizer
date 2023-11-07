# WebTextSummarizer
A Python tool for quick and easy web page text extraction and summarization. Ideal for generating concise summaries from web articles.

```markdown
# Text Summarization from Web Pages

This Python script allows you to extract and summarize text content from web pages. It uses the `newspaper3k` library for web scraping and article extraction and provides an option for more comprehensive output by including the article's title, publication date, and source URL.

## Features

- Extract text content from a web page using a URL.
- Summarize the extracted text into a specified number of sentences.
- Display additional information, such as the article title, publication date, and source URL.

## Prerequisites

- Python 3.x
- Install required libraries:
  - `newspaper3k`
  - `nltk`
  - `requests`
  - `beautifulsoup4`

You can install the necessary libraries using `pip`:

```bash
pip install newspaper3k nltk requests beautifulsoup4
```

## Usage

1. Clone the repository or download the code files to your local machine.
2. Run the script and provide the URL of the web page you want to summarize.
3. The script will extract the text content, summarize it, and display the result, including additional information if available.

Example usage:

```bash
python summarize_webpage.py https://example.com
```

## Configuration

You can configure the summarization settings by adjusting the `num_sentences` parameter in the script to control the length of the summary.

## Acknowledgments

- [newspaper3k](https://github.com/codelucas/newspaper) - Used for web scraping and article extraction.
- [nltk](https://www.nltk.org/) - Used for natural language processing and text summarization.

## Author

Amirhossein Omidi

## Contact
65mirhossein@gmail.com
```
