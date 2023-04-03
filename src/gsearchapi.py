import webbrowser
from bs4 import BeautifulSoup
import requests
import json
import lxml


def googleSearch(query: str) -> object:
    params = {
        "q": query,          # query example
        "hl": "en",          # language
        "gl": "uk",          # country of the search, UK -> United Kingdom
        "start": 0,          # number page by default up to 0
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.147 Safari/537.36"
    }

    page_limit = 1          # page limit if you don't need to fetch everything
    page_num = 0

    data = []

    while True:
        page_num += 1
        print(f"page: {page_num}")

        html = requests.get("https://www.google.com/search",
                            params=params, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, 'lxml')

        for result in soup.select(".tF2Cxc"):
            title = result.select_one(".DKV0Md").text
            try:
                snippet = result.select_one(".lEBKkf span").text
            except:
                snippet = None
                links = result.select_one(".yuRUbf a")["href"]

            data.append({
                "title": title,
                "links": links
            })

        # stop loop due to page limit condition
        if page_num == page_limit:
            break
        # stop the loop on the absence of the next page
        if soup.select_one(".d6cvqb a[id=pnnext]"):
            params["start"] += 10
        else:
            break
    return data[0]

'''
Thanks to the stackoverflow post : <https://stackoverflow.com/a/75606545/16439338>
'''