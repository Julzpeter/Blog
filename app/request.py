# from .models import Quote
import urllib.request, json

# Getting the quote base url
base_url = None


# def configure_request(app):
#     global base_url
#     base_url = app.config['QUOTE_API_BASE_URL']




def get_quotes():
    get_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quote_url) as url:
        quotes = url.read()
        get_quotes_response= json.loads(quotes)

    return get_quotes_response

#         # quote_object = []
#         # if quote_response:

#         #     quote = quote_response
#         #     random_quote = process_results(quote)

#     return quote_response


# def process_results(quote_response):

#         random_quote = []
#         id = quote_response['id']
#         author = quote_response['author']
#         quote = quote_response['quote']

#         random_quote.append(Quote(id, author, quote))
#         return random_quote
