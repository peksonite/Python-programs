from sys import argv

import requests

API_KEY = "0683e8206b7c4b45a9c350b4a39f31ee"

URL = "https://newsapi.org/v2/top-headlines?"


def get_artciles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "pl",
        "apiKey": API_KEY,
    }
    return _get_articles(query_parameters)


def get_artciles_by_query(query):
    query_parameters = {"q": query, "sortBy": "top", "country": "pl", "apiKey": API_KEY}
    return _get_articles(query_parameters)


def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()["articles"]

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result["title"])
        print(result["url"])
        print("")


def get_sources_by_category(category):
    url = "https://newsapi.org/v2/top-headlines/sources"
    query_parameters = {"category": category, "language": "pl", "apiKey": API_KEY}

    response = requests.get(url, params=query_parameters)

    sources = response.json()["sources"]

    for source in sources:
        print(source["name"])
        print(source["url"])


if __name__ == "__main__":
    print(f"Getting news for {argv[1]}...\n")
    get_artciles_by_category(argv[1])
    print(f"Successfully retrieved top {argv[1]} headlines")
    # get_artciles_by_query("Liz Truss"))
    # print_sources_by_category("technology")
