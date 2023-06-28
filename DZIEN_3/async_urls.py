import concurrent.futures
import urllib.request

URLS = [
    "https://www.foxnews.com/",
    "https://edition.cnn.com/",
    "https://www.bbc.com/",
    "https://www.wp.pl/",
    "https://www.gov.pl/web/obrona-narodowa",
    "https://mil.ru/"
]

def load_url(url,timeout):
    with urllib.request.urlopen(url,timeout=timeout) as conn:
        return conn.read()
    
