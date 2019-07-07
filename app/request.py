from .models import Quote
import urllib.request, json

# Getting the quote base url
base_url = None


def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']


def get_quote():
    get_quote_url = base_url

    with urllib.request.urlopen(get_quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        quote_object = []
        if quote_response:

            quote = quote_response
            random_quote = process_results(quote)

    return random_quote


def process_results(quote):

        random_quote = []
        id = quote['id']
        author = quote['author']
        quote = quote['quote']

        random_quote.append(Quote(id, author, quote))
        return random_quote
